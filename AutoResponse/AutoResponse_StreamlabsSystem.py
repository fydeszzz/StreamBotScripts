import os
import codecs
import json
import io
import datetime
import re


# script information
ScriptName = "Auto Response"
Description = "Bot will automatically reply when users input keywords in chat."
Website = "https://github.com/fydeszzz/StreamBotScripts"
Creator = "tristia"
Version = "1.0.0"


# Global Settings
settings = {}
keywordList = []
keywordMap = {}
emoteList = ""
tempList = []

# init start
def Init():

    global settings, keywordList, keywordMap, emoteList, tempList
    work_dir = os.path.dirname(__file__)
    keywordList = codecs.open(os.path.join(work_dir,"keywordlist.txt"), encoding="utf-8")
    tempList = keywordList.readlines()

    try:
        with codecs.open(os.path.join(work_dir, "settings.json"), encoding="utf-8") as file:
            settings = json.load(file, encoding="UTF-8")

    except:
        settings = {
            "liveOnly": True,
            "permission": "Everyone",
            "cooldown": 100,
            "emoteList": "DxCat, CoolCat, InuyoFace, GlitchCat, StinkyCheese, BloodTrail",
            "response": "ERROR! Please try again!"
        }
    
    # exclude "\n" in .txt file
    for i in range(len(tempList)):
        tempList[i] = tempList[i].replace("\n", "").split(",")
        newkeyword = tempList[i][0]
        response = tempList[i][1]
        keywordMap[newkeyword] = response

    emoteList = settings["emoteList"].replace(" ","").split(",")
    emoteList = list(set(emoteList))

    return


# main process
def Execute(data):

    global keywordMap
    userid = data.User
    username = data.UserName

    # check whether live is on or not, and permission
    if Parent.HasPermission(userid, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):

        # bot response with random emote
        line = str(data.IsChatMessage() and data.GetParam(0))

        # line = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a)])","",line)   # user inputs must totally match Chinese keywords
        line = re.sub(u"([^\u4e00-\u9fa5)])","",line)                                            # with Chinese keywords, English letters and numbers as suffix

        if line in keywordMap:
            message = keywordMap[line]
            rannum = Parent.GetRandom(0, len(emoteList))
            emote = " " + emoteList[rannum] + " "

            message = message.replace("$username", username)

            now = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)
            message = message.replace("$now", now)

            send_message(message + "" + emote)

        return


def send_message(message):
    Parent.SendStreamMessage(message)
    return


def OpenKeywordList():
    filepath = os.path.join(os.path.dirname(__file__), "keywordlist.txt")
    os.startfile(filepath)
    return


def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return


def ReloadSettings(jsonData):
    Init()
    return


# do not remove this
def Tick():
    return