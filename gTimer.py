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
        [default.GMultiline(font=defaultFont, xStretch=True, yStretch=True, value="tlog", size=(40,None))]
    ]

    gMenu = [
        ["Log File", ["Open Log File", "Save Log File"]],
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]]

    ]

    layout = [
        [default.GMenu(winMenu=gMenu)],
        [default.GColumn(winColumn=topWin, xStretch=True)],
        [default.GColumn(winColumn=middleWin1, xStretch=True, yStretch=True)],
        [default.GColumn(bottomWin, xStretch=True, yStretch=True)]
    ]

    default.GWindow(mainWindow=layout)


    while True:
        event, GetValues = default.window.read()
        if event == WIN_CLOSED:
            break


    default.window.close()
if __name__ == "__main__":
    main()