from GnuChanGUI import *

def main():
    default = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024,600), resizable=True)
    default.Theme()

    defaultFont = "Sans, 20"
    timerStart = False
    timerInfo = ""
    second = minute = hour = 0
    timeLog = ""

    timeDick = {"reason":"", 
                "hour":0,
                "Minute":0,
                "second":0}

    timerlist = []

    middleWin1 = [
        [default.GText(title=timerInfo, font=defaultFont, value="time", xStretch=True, border=0, position="center", bColor="#10011f")],
        [default.GText(title=timeLog, font=defaultFont, value="tinfo", xStretch=True, border=0, position="center", bColor="#220242")],
        [default.GButton("Start", xStretch=True, font=defaultFont),
         default.GButton("Stop", xStretch=True, font=defaultFont),
         default.GButton("Add Laps", xStretch=True, font=defaultFont),
         default.GButton("Clear", xStretch=True, font=defaultFont)],
         [default.GMultiline(font=defaultFont, xStretch=True, yStretch=True, value="tlog", position="center", readonly=True)]
    ]


    middleWin2 = [
        [default.GText(title="Alarm", font=defaultFont, xStretch=True)],
        [default.GText(title="reason for alarm: ", font=defaultFont), default.GInput(value="alarmName", font=defaultFont)],
        [default.GText(title="Hour: ", font=defaultFont), default.GInput(value="hourTime", font=defaultFont)],
        [default.GText(title="Minute: ", font=defaultFont), default.GInput(value="hourMinute", font=defaultFont)],
        [default.GText(title="Second: ", font=defaultFont), default.GInput(value="hourSecond", font=defaultFont)],
        [default.GButton(title="Add New Timer", font=defaultFont, xStretch=True)],

    ]

    gMenu = [
        ["Log File", ["Open Log File", "Save Log File"]],
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]

    ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GColumn(winColumn=middleWin1, xStretch=True, yStretch=True, bcolor="#10011f"),
         default.GText(title=""),
         default.GColumn(winColumn=middleWin2, xStretch=True, yStretch=True, bcolor="#10011f")],
        [default.GText("", xStretch=True)],
        [default.GListBox(list=timerlist, value="timerAlarm", position="center", xStretch=True, yStretch=True, noScroolBar=True)]
    ]

    default.GWindow(mainWindow=layout)
    default.GListBoxFixer(value="timerAlarm", border=0)


    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED:
            break
        if event == "Exit":
            break



        if event == "Start":
            timerStart = True
            default.window["tinfo"].update("Timer Start")
        elif event == "Stop":
            timerStart = False
            default.window["tinfo"].update("Timer Stop")


        if event == "Clear":
            second = minute = hour = 0
            timerStart = False
            default.window["tinfo"].update("Timer Finish")
            default.window["tlog"].update("")
        if event == "Add Laps":
            newTimer = f"Hour-{hour} : Minute-{minute} : Second-{int(second)}" + "\n"
            timeLog += newTimer
            default.window["tlog"].update(timeLog)
        if timerStart == True:
            if second <= 60:
                second += 0.05
            else:
                minute += 1
                second = 0
        if minute == 60:
            hour += 1
            minute = 0
        newTimer = f"{hour}:{minute}:{int(second)}"
        default.window["time"].update(newTimer)


        if event == "Add New Timer":
            timeDick["reason"] = GetValues["alarmName"]
            timeDick["hour"] = GetValues["hourTime"]
            timeDick["Minute"] = GetValues["hourMinute"]
            timeDick["second"] = GetValues["hourSecond"]

            timerlist.append([f"Reason:{timeDick['reason']} : Hour:{timeDick['hour']} : Minute:{timeDick['Minute']} : Second:{timeDick['second']}", ])

        finished_timers = []
        for timer in timerlist:
            if timer[0].split(": Hour:")[1].split(" :")[0].strip() == str(hour) and timer[0].split(": Minute:")[1].split(" :")[0].strip() == str(minute) and timer[0].split(": Second:")[1].split(" :")[0].strip() == str(int(second)):
                finished_timers.append(timer)
        for finished_timer in finished_timers:
            timerlist.remove(finished_timer)
        default.window["timerAlarm"].update(timerlist)





    default.window.close()
if __name__ == "__main__":
    main()