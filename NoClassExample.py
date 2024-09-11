from GnuChanGUI import *

"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(640, 360), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS


    buttons = [
        [
            gc.Push,
            gc.GButton(title="Press Button"),
            gc.GButton(title="Remove"),
            gc.Push
        ],
    ]

    layout = [
            [gc.GPin(
                gc.GText(title="This is Text", value="text", font="Sans, 20", xStretch=True)
            )],
            [gc.GPin(
                gc.GInput(value="input", font="Sans, 20", xStretch=True)
            )],
            [
                gc.Push,
                gc.GPin( gc.GColumn(winColumn=buttons) ),
                gc.Push
            
            ],
            [gc.GListBox(value="list", font="Sans, 20", xStretch=True, yStretch=True)]
    ]

    gc.GWindow(mainWindow=layout)
    _Keyboard = GKeyboard(gc.window)

    gc.GListBoxBorderSize(border=0, windowValue="list")

    ShowList = []
    def update():
        if gc.event == "Press Button" or gc.event == _Keyboard.Return:
            if gc.GFocus("input"):
                print("yes")
            # Get Input Value
            text = gc.GetValues["input"]
            # Update ListBox
            ShowList.append(text)
            gc.window["list"].update(ShowList)
            # Update Text Box
            gc.window["text"].update(text)
            # Update Input Box
            gc.window["input"].update("")

        elif gc.event == "Remove":
            ShowList.remove(str(gc.GetValues["list"]).strip("['']"))
            gc.window["list"].update(ShowList)

    def beforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=beforeExit, timeout=0)
