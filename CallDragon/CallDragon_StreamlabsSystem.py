import os
import codecs
import json
import random


# Script Information
ScriptName = "Call Dragon"
Description = "When users used command at specified times, dragon will appear in chat and give users prize."
Website = "https://github.com/fydeszzz/StreamBotScripts"
Creator = "tristia"
Version = "1.0.0"

# Global Settings
settings = {}
userList = []
nameList = []
rewardList = []
count = 0


def ScriptToggled(state):
    return


# init start
def Init():
    global settings, work_dir
    work_dir = os.path.dirname(__file__)

    try:
        with codecs.open(os.path.join(work_dir, "settings.json"), encoding="utf-8-sig") as file:
            settings = json.load(file, encoding="utf-8-sig")

    except:
        settings = {
            "liveOnly": True,
            "command": "!calldragon",
            "permission": "Everyone",
            "count" : 5,
            "usecooldown": True,
            "useusercooldown": True,
            "cooldown": 3600,           # sec
            "cooldownmessage": "the $command is still on cooldown for $cd mins!",
            "usercooldown": 3600,       # sec
            "usercooldownmessage": "$user has already used the $command!",
            "currency": 10,
            "joinmessage": "$username has successfully called dragon! (progress: $progress)",
            "rewardmessage": "Congrats for following users: $rewardlist",
            "restartmessage": "Dragon is coming! Use $connand to call dragon."
        }

    return


# main process
def Execute(data):
    username = data.UserName
    userid = data.User
    cdmessage = ""
    progressmessage = ""

    global userList, nameList, rewardList, count

# check whether live is on or not, and permission
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(userid, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):

        # check whether command is on cooldown or not
        if Parent.IsOnCooldown(ScriptName, settings["command"]):
            cdi = Parent.GetCooldownDuration(ScriptName, settings["command"])
            cd = str(cdi / 60) + ":" + str(cdi % 60).zfill(2)    # min
            cdmessage = settings["cooldownmessage"]
            cdmessage = cdmessage.replace("$cd", cd)
            send_message(cdmessage)

        
        else:
            if Parent.IsOnUserCooldown(ScriptName, settings["command"], userid):
                usercdmessage = settings["usercooldownmessage"]
                usercdmessage = usercdmessage.replace("$username", username)
                send_message(usercdmessage)

            else:
                userList.append(userid)
                nameList.append(username)
                progress = str(len(userList)) + "/" + str(settings["count"])  # progress of calling dragon
                progressmessage = (" " + settings["joinmessage"])
                progressmessage = progressmessage.replace("$username", username)
                progressmessage = progressmessage.replace("$progress", progress)
                send_message(progressmessage)

            # add usercooldown for command
                if settings["useusercooldown"]:
                    Parent.AddUserCooldown(ScriptName, settings["command"], userid, settings["usercooldown"])

            # when command has used settings["count"] times
                if len(userList) == settings["count"]:

                    for i in range(settings["count"]):
                        randnum = random.randint(1, 3)   # random rate for prize bonus
                        reward = (settings["currency"] * randnum)
                        Parent.AddPoints(userList[i], nameList[i], reward)
                        rewardList.append(nameList[i] + "(" + str(reward) + ")")

                        rewardname = ", ".join(rewardList)
                         
                rewardmessage = settings["rewardmessage"]
                rewardmessage = rewardmessage.replace("$rewardlist", rewardname)
                send_message(rewardmessage)

            # clear all list & add cooldown for command
                userList = []
                nameList = []
                rewardList = []
                
                if settings["usecooldown"]:
                    Parent.AddCooldown(ScriptName, settings["command"], settings["cooldown"])
                    count = 0
    
    else:
        if Parent.GetCooldownDuration(ScriptName, settings["command"]) == 0 and len(userList) == 0 and count<1:
            restartmessage = settings["restartmessage"]
            restartmessage = restartmessage.replace("$command", settings["command"])
            send_message(restartmessage)
            count = 1

    return


def send_message(message):
    Parent.SendStreamMessage(message)
    return


def ReloadSettings(jsonData):
    Init()
    return


def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.txt")
	os.startfile(location)
	return


# do not remove this
def Tick():
    return
