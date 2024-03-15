"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(900, 600), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [
            gc.Push,
            gc.GButton(title="Open Folder"), gc.GButton(title="Open Directory"), 
            gc.GButton(title="<"), gc.GButton(title="+"), gc.GButton(title="-"),  gc.GButton(title=">"), 
            gc.GButton(title="Close Image"),
            gc.Push 
        ],
        [gc.Push, gc.GImage(value="img"), gc.Push],


               ]



    gc.GWindow(mainWindow=layout)

    gc.window["img"].update("/home/archkubi/gnuchan_Beta.png")

    def update():
        pass


    gc.update(GUpdate=update)