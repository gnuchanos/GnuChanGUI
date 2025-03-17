"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard, GMessage



# Extra Lib

gc = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
gc.font = "Sans, 20"
Themecolors().GnuChanOS

c = GColors()

tab1 = [
        [gc.GText(SetText="Top Layer",    TPosition="center", TFont="Sans, 20",    BColor=c.blue1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
    ]

tab2 = [
        [gc.GText(SetText="Middle Left",  TPosition="center", TFont="Sans, 20",  BColor=c.pink1, xStretch=True, yStretch=True, EmptySpace=(0,0))]
    ]

layout = [
        [gc.GTabGroup(TabGroupLayout=[
            [gc.GTab(Text="test1", TabLayout=tab1, SetValue="tab1")],
            [gc.GTab(Text="test2", TabLayout=tab2, SetValue="tab2")],
        ], SetValue="tabG")]
    ]

gc.GWindow(SetMainWindowLayout_List=layout)
keyboard = GKeyboard(window=gc)

test = GMessage()

def update():
    if "bb" == gc.GetEvent:
        if len(gc.GetValues["input"]) > 0:
            gc.GetWindow["text"].update(gc.GetValues["input"])
            gc.GetWindow["input"].update("")


def beforeExit():
    pass

gc.SetUpdate(Update=update, exitBEFORE=beforeExit, TimeOUT=1)
