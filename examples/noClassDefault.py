from GnuChanGUI import *

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