"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread


#Thread(target=DownloadVideo, args=[]).start()


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(700, 110), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    second = 0
    minute = 0
    hour = 0
    timeLog = f"{int(hour)}:{int(minute)}:{second}"
    timerStart = False


    layout = [ 
        [
            gc.GText(title="|", EmptySpace=(0,0)),
            gc.GText(title="-"*30, EmptySpace=(0,0)),
            gc.GText(title="|", EmptySpace=(0,0)),

            gc.GText(title=timeLog, value="time", EmptySpace=(0,0), xStretch=True, position="center"),

            gc.GText(title="|", EmptySpace=(0,0)),
            gc.GText(title="-"*30, EmptySpace=(0,0)),
            gc.GText(title="|", EmptySpace=(0,0)),
        ],

        [
                gc.GText(title=" | ", xStretch=True),
            gc.GButton(title="Start Timer"),
                gc.GText(title=" | ", xStretch=True),
            gc.GButton(title="Stop Timer"),
                gc.GText(title=" | ", xStretch=True),
            gc.GButton(title="Clear Timer"),
                gc.GText(title=" | ", xStretch=True),       
        ],
               ]
    
    def timerStart_func():
        global second, minute, hour, timeLog, timerStart
        if gc.event == "Start Timer":
            timerStart = True
        if gc.event == "Stop Timer":
            timerStart = False
        if gc.event == "Clear Timer":
            timerStart = False
            second = minute = hour = 0

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

    gc.update(GUpdate=update)
