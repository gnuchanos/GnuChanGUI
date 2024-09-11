"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
import time


if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Timer!", Size=(700, 228), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    second = 0
    minute = 0
    hour = 0
    timeLog = f"{int(hour)}:{int(minute)}:{second}"
    timerStart = False
    StartTime = 0



    win = [
        [gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0)],
        [
            gc.GText(title=timeLog, value="time", EmptySpace=(0,0), xStretch=True, position="center", font="Sans, 60"),
        ],

        [
            gc.GButton(title="Start Timer", xStretch=True),
            gc.GButton(title="Stop Timer", xStretch=True),
            gc.GButton(title="Clear Timer", xStretch=True),
        ],
        [gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0)],
    ]

    layout = [ 
        [
            gc.vsep,
            gc.GColumn(winColumn=win, xStretch=True, yStretch=True),
            gc.vsep,
        ]
               ]
    
    def timerStart_func():
        global second, minute, hour, timeLog, timerStart, StartTime
        if gc.event == "Start Timer":
            timerStart = True
        if gc.event == "Stop Timer":
            timerStart = False
        if gc.event == "Clear Timer":
            timerStart = False
            second = minute = hour = 0
            timeLog = f"{int(hour)}:{int(minute)}:{int(second)}"    
            gc.window["time"].update(timeLog)           

        if timerStart:
            if second < 60:
                second += gc.dt
            else:
                second = 0
                minute += 1
                if minute == 60:
                    hour += 1
                    minute = 0
            timeLog = f"{int(hour)}:{int(minute)}:{int(second)}"    
            gc.window["time"].update(timeLog)

    gc.GWindow(mainWindow=layout)

    def update():
        timerStart_func()

    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)

