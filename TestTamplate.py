from GnuChanGUI import GnuChanGUI
import time

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GText(value="text", font=gc.font, xStretch=True, position="center")],
    [gc.GButton("Start Timer", font=gc.font, xStretch=True),
     gc.GButton("Stop Timer", font=gc.font, xStretch=True)],
    [gc.GMultiline(value="test")]
]

gc.GWindow(mainWindow=layout)

second = 0
timerStart = False


gc.window["text"].bind('<Shift>', ' Shift')



def GQ():
    global second, timerStart

    if gc.event == "Start Timer":
        timerStart = True
    elif gc.event == "Stop Timer":
        timerStart = False

    if timerStart == True:
        second += 1 * gc.dt
        gc.window["text"].update(str(second))
    else:
        pass

    

gc.update(GUpdate=GQ)

gc.window.close()
