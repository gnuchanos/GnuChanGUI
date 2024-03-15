"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *

if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(250, 600), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
               ]

    gc.GWindow(mainWindow=layout)

    def update():
        pass


    gc.update(GUpdate=update)