import os
import codecs
import json
import datetime


# Script Information
ScriptName = "GoSleep"
Description = "Bot will send voice message in chat at selected time."
Website =  "https://github.com/fydeszzz"
Creator = "tristia"
Version = "1.0.0"

# Global Settings
settings = {}
count = 0

# init start 
def Init():
    global settings, voicepath, volume
    work_dir = os.path.dirname(__file__)
    voicepath = work_dir + "\\voiceFiles"

    try:
        with codecs.open(os.path.join(work_dir, "settings.json"), encoding='utf-8-sig') as file:
            settings = json.load(file, encoding='utf-8-sig')
    except:
        settings = {
            "liveOnly": False,
            "response": "error!"
        }

    volume = settings["volume"] / 100.0
    return

# main process
# send TTS message at selected local time
def Execute(data):

    thehour = datetime.datetime.now().hour
    theminute = datetime.datetime.now().minute

    global count

    while count <1:
        if thehour == settings["hour"] and theminute == settings["minutes"]:
            send_message(settings["response"])
            voicemessage = voicepath + "\\gosleep.mp3" 
            Parent.PlaySound(voicemessage, volume)
            count += 1

    return 


# send message to chat
def send_message(message):
    Parent.SendStreamMessage(message)
    return


# update settings when press "reload" button in script
def ReloadSettings(jsonData):
    Init()
    return

# do not remove this 
def Tick():
    return

