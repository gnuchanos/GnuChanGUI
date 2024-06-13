"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread


#Thread(target=DownloadVideo, args=[]).start()


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(1012, 900), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [ gc.GText(title="Input File: "), gc.GText(value="InputFile",  xStretch=True,  position="center") ],
        [ gc.GText(title="Output File: "), gc.GText(value="OutputFile", xStretch=True, position="center") ],
        [
            gc.GText(xStretch=True),
            gc.GButton(title="Select Input Folder"),
            gc.GButton(title="Select Output Folder"),
            gc.GButton(title="Start Convert"),
            gc.GText(xStretch=True),
        ],
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(value="mp4List", xStretch=True, yStretch=True, noScroolBar=True) ],
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(value="mp3List", xStretch=True, yStretch=True, noScroolBar=True) ],
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
    ]

    gc.GWindow(mainWindow=layout)

    gc.GListBoxBorderSize(value="mp3List", border=0)
    gc.GListBoxBorderSize(value="mp4List", border=0)

    def update():
        pass


    gc.update(GUpdate=update)