"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from termios import TAB2
from turtle import color
from GnuChanGUI import *
from matplotlib.pyplot import yscale





if __name__ == "__main__":
    gc = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]
    defaultFont = "Sans, 20"


    layout = [
        [gc.GSlider(MaxRange=(0, 100), DefaultValue=20, SDirection="h", WindowValue="slider")],
        [gc.GProgressBar(MaxRange=100, WindowValue="pro", PDirection="h")],
        [gc.GText(SetText="Default", xStretch=True, TextValue="text")],
        [gc.GButton(Text="Press HERE!", xStretch=True, WindowValue="button")]
    ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    #gc.AddNewBorderWithColor(WindowValue="pro", Color="red", BorderSize=1)

    def update():
        if gc.GetEvent == "button":
            gc.GetWindow["text"].update(gc.GetValues["slider"])
        if gc.GetValues["slider"]:
            gc.GetWindow["pro"].update(gc.GetValues["slider"])

    def beforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=beforeExit, TimeOUT=1)
