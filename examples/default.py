"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread


#Thread(target=DownloadVideo, args=[]).start()

if __name__ == "__main__":
    gc = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [   gc.GMultiline(value="out", xStretch=True, yStretch=True, font="Sans, 20")   ],
        [   gc.GInput(value="in", xStretch=True, font="Sans, 20")   ]
    ]

    gc.GWindow(mainWindow=layout)

    def PrintThis():
        print("Works!")

    def update():
        gd = GKeyboard(window=gc.window, event=gc.event)

        control = gd.SingleKeyPressCheck(gd.Return)
        if control:PrintThis()

    def beforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=beforeExit, timeout=1)