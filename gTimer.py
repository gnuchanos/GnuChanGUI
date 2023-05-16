from GnuChanGUI import *

def main():
    default = GnuChanGUI(Title="GnuChan Program Runner", Size=(650,600), resizable=False)
    default.Theme()

    defaultFont = "Sans, 20"
    timerStart = False
    timerInfo = ""
    second = minute = hour = 0
    timeLog = ""


    topWin = [
        [default.GText(title=timerInfo, font=defaultFont, value="time", xStretch=True, border=0, position="center", bColor="#10011f")],
        [default.GText(title=timeLog, font=defaultFont, value="tinfo", xStretch=True, border=0, position="center", bColor="#220242")],
    ]

    middleWin1 = [
        [default.GButton("Start", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("Stop", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("Add Laps", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("Clear", xStretch=True, yStretch=True, font=defaultFont)],
    ]

    bottomWin = [
        [default.GMultiline(font=defaultFont, xStretch=True, yStretch=True, value="tlog", size=(40,None), position="center", readonly=True)]
    ]

    gMenu = [
        ["Log File", ["Open Log File", "Save Log File"]],
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]

    ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GColumn(winColumn=topWin, xStretch=True, bcolor="#10011f")],
        [default.GColumn(winColumn=middleWin1, xStretch=True, yStretch=True, bcolor="#10011f")],
        [default.GColumn(bottomWin, xStretch=True, yStretch=True, bcolor="#10011f")]
    ]

    default.GWindow(mainWindow=layout)


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


    default.window.close()
if __name__ == "__main__":
    main()