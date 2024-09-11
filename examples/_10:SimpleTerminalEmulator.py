"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread

#Thread(target=DownloadVideo, args=[]).start()



if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Terminal Emulator", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    # var
    _output = ""

    win = [
        [   gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0)   ],
        [   gc.GMultiline(value="ou", xStretch=True, yStretch=True, readonly=True, bcolor=GColors().purple8)   ],
        [   gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0)   ],
        [   
            gc.GText(title="  Command:> ", EmptySpace=(0, 0)),
            gc.GInput(value="in", xStretch=True, EmptySpace=(0, 0), bcolor=GColors().purple7)
        ],
        [   gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0)   ],
    ]

    layout = [ 
        [
            gc.vsep,
            gc.GColumn(winColumn=win, xStretch=True, yStretch=True),
            gc.vsep,
        ]
    ]

    gc.GWindow(mainWindow=layout)

    def _PrintThis0():
        global _output
        _output += '-'*100 + "\n"
        _output += "Works Focus 0" + "\n"
        _output += '-'*100 + "\n"
        gc.window["ou"].update(_output)

    def _PrintThis1():
        global _output
        _output += '-'*100 + "\n"
        _output += "Works Focus 1" + "\n"
        _output += '-'*100 + "\n"
        gc.window["ou"].update(_output)


    cc = GKeyboard(gc.window)


    _command = _parameters = _path0 = _path1 = 0
    def update():
        global cc



    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)

