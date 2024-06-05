"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread





#Thread(target=DownloadVideo, args=[]).start()



if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(400, 600), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS
    clr = GnuChanOSColor()


    window = [
        [gc.GText(title="Let's Start Math", xStretch=True, position="center", bcolor=clr.colors0)],
        [gc.hsep],
            [ gc.GButton(title="1", xStretch=True), gc.GButton(title="2", xStretch=True), gc.GButton(title="3", xStretch=True), gc.GButton(title="+", xStretch=True) ],
            [ gc.GButton(title="4", xStretch=True), gc.GButton(title="5", xStretch=True), gc.GButton(title="6", xStretch=True), gc.GButton(title="-", xStretch=True) ],
            [ gc.GButton(title="7", xStretch=True), gc.GButton(title="8", xStretch=True), gc.GButton(title="9", xStretch=True), gc.GButton(title="*", xStretch=True) ],
            [ gc.GButton(title="<", xStretch=True), gc.GButton(title="0", xStretch=True), gc.GButton(title=".", xStretch=True), gc.GButton(title="/", xStretch=True) ],
        [gc.hsep],
            [gc.GText(bcolor=clr.colors0, xStretch=True)],
        [gc.hsep],
            [gc.GMultiline(value="console", xStretch=True, yStretch=True, readonly=True)],
        [gc.hsep],
    ]

    layout = [ 
        [ gc.GColumn(winColumn=window, xStretch=True, yStretch=True) ],
    ],

    gc.GWindow(mainWindow=layout)


    def update():
        pass


    gc.update(GUpdate=update)