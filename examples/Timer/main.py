"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *



if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(550, 150), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    second = minute = hour = 0
    timerStart = False

    layout = [
        [gc.hsep],
        [gc.GText(value="timer", font="Sans, 30", xStretch=True, position="center", bcolor=GnuChanOSColor().colors5)],
        [gc.hsep],

        [gc.Push], [gc.Push], [gc.Push],

        [gc.hsep],
        [gc.GButton(title="Start Timer", xStretch=True), 
         gc.GButton(title="Stop Timer", xStretch=True), 
         gc.GButton(title="Clear Timer", xStretch=True)],
        [gc.hsep] ]

    gc.GWindow(mainWindow=layout)

    def update():
        global second, minute, hour, timerStart

        # Buttons
        if gc.event == "Start Timer":
            if not timerStart:
                timerStart = True
        if gc.event == "Stop Timer":
            if timerStart:
                timerStart = False
        if gc.event == "Clear Timer":
            second = minute = hour = 0
            timerStart = False
            gc.window["timer"].update("")

        # timer
        if timerStart:
            if second < 60:
                second += 1 * gc.dt
            else:
                second = 0
                minute += 1
                if minute == 60:
                    hour += 1
                    minute = 0
                

            gc.window["timer"].update(f"{hour}:{minute}:{int(second)}")


    gc.update(GUpdate=update)