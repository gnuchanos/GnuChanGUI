from GnuChanGUI import *

"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(300, 200), resizable=False, finalize=True)
    Themecolors().GnuChanOS

    layout = [ [gc.GText(title="test", xStretch=True, position="center")] ]

    gc.GWindow(mainWindow=layout)

    def update():
        pass

    gc.update(GUpdate=update)