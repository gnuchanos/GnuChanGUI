"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *



if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(550, 600), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [gc.GText(value="music", xStretch=True, position="center", bcolor=GColors().purple8)],
        [gc.GButton(title="Play", xStretch=True), gc.GButton(title="Stop", xStretch=True), gc.GButton(title="Pause", xStretch=True)],
        [gc.GProgressBar(value="music_progress", direction="h", MaxValue=100)],
        [gc.GListBox(value="music_list", xStretch=True, yStretch=True)]


               ]

    musicPlay = False

    gc.GWindow(mainWindow=layout)

    def update():
        pass


    gc.update(GUpdate=update)
