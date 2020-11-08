import json
import os
import codecs
import datetime

ScriptName = "Clock Notify"
Website = "https://www.twitch.tv/tristia"
Description = "Clock Notify for Streamlabs Bot"
Creator = "Salify"
Version = "1.0.0"
volume = 1
voicepath = ""
settings = {}

def Init():
    global volume, voicepath, settings
    work_dir = os.path.dirname(__file__)
    voicepath = work_dir + "\\voice"

    try:
        with codecs.open(os.path.join(work_dir, "settings.json"), encoding='utf-8-sig') as file:
            settings = json.load(file, encoding='utf-8-sig')
    except:
        settings = {
            "liveOnly": False,
            "command": "!when",
            "permission": "Everyone",
            "response": "whatever you want to say."
        }

    volume = settings["volume"] / 100.0
    return

# main program    
def Execute(data):

    if data.IsChatMessage() and data.GetParam(0) == settings["command"]:

        username = data.UserName    # username in chat
        nowtime = datetime.datetime.now().strftime('%H:%M:%S')

        if datetime.datetime.now().hour == 20:
            send_message(settings["response1"])
            voice8Pm = voicepath + "\\" + "8pm.mp3"
            Parent.PlaySound(voice8Pm , volume)

        elif datetime.datetime.now().hour == 22:
            send_message(settings["response2"])
            voice10Pm = voicepath + "\\" + "10pm.mp3"
            Parent.PlaySound(voice10Pm , volume)
            
        elif datetime.datetime.now().hour == 23:
            send_message(settings["response3"])
            voice11Pm = voicepath + "\\" + "11pm.mp3"
            Parent.PlaySound(voice11Pm , volume)
            
        elif datetime.datetime.now().hour == 0 or datetime.datetime.now().hour == 1:
            send_message(settings["response4"])
            voice12Pm = voicepath + "\\" + "12pm.mp3"
            Parent.PlaySound(voice12Pm , volume)

        elif datetime.datetime.now().hour == 18 or datetime.datetime.now().hour == 19:
            send_message(settings["response5"])
            voice6Pm = voicepath + "\\" + "6pm.mp3"
            Parent.PlaySound(voice6Pm , volume)
      
        else:
            send_message(username + ", " + settings["response"] + nowtime)
            voiceOtherPm = voicepath + "\\" + "otherpm.mp3"
            Parent.PlaySound(voiceOtherPm , volume)
       
        return

def send_message(message):         # bot send message
    Parent.SendStreamMessage(message)
    return


def ReloadSettings(jsonData):      # init when press "reload" in script
    Init()
    return


def Tick():
    return