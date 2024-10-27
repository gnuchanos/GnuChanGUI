"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *

gc = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
gc.font = "Sans, 20"
Themecolors().GnuChanOS

layout = [ 

]

gc.GWindow(mainWindow=layout)
keyboard = GKeyboard(window=gc.window)

def update():
    pass

def beforeExit():
    pass

gc.update(GUpdate=update, exitBEFORE=beforeExit, timeout=1)
