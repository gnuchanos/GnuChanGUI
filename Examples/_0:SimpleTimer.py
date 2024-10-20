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
        [gc.GText(xStretch=True, BColor=GnuChanOSColor().colors0)],
        [
            gc.GText(SetText=timeLog, TextValue="time", EmptySpace=(0,0), xStretch=True, TPosition="center", TFont="Sans, 60"),
        ],

        [
            gc.GButton(Text="Start Timer", xStretch=True),
            gc.GButton(Text="Stop Timer", xStretch=True),
            gc.GButton(Text="Clear Timer", xStretch=True),
        ],
        [gc.GText(xStretch=True, BColor=GnuChanOSColor().colors0)],
    ]

    layout = [ 
        [
            gc.GVSep(Color=GnuChanOSColor().colors3),
            gc.GColumn(winColumnLayout_List=win, xStretch=True, yStretch=True),
            gc.GVSep(Color=GnuChanOSColor().colors3),
        ]
               ]
    
    def timerStart_func():
        global second, minute, hour, timeLog, timerStart, StartTime
        if gc.GetEvent == "Start Timer":
            timerStart = True
        if gc.GetEvent == "Stop Timer":
            timerStart = False
        if gc.GetEvent == "Clear Timer":
            timerStart = False
            second = minute = hour = 0
            timeLog = f"{int(hour)}:{int(minute)}:{int(second)}"    
            gc.GetWindow["time"].update(timeLog)           

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
            gc.GetWindow["time"].update(timeLog)

    gc.GWindow(SetMainWindowLayout_List=layout)

    def update():
        timerStart_func()

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)

