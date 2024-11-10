"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard


# Extra Lib

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
