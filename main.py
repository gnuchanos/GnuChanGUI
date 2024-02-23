from GnuChanGUI import *

"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(250, 600), resizable=False, finalize=True)
    Themecolors().GnuChanOS

    layout = [ [gc.GText(value="text", xStretch=True, position="center")],
               [gc.GInput(value="user_input", xStretch=True)],
               [gc.GButton(title="change text", font="Sans, 20", xStretch=True)],
               [gc.GListBox(value="listbox", xStretch=True, yStretch=True, position="center")]
               ]

    gc.GWindow(mainWindow=layout)

    listboxList = []
    def update():
        global listboxList

        if gc.event == "change text":
            gc.window["text"].update(gc.GetValues["user_input"])
            gc.window["user_input"].update("")

            listboxList.append(gc.GetValues["user_input"])
            gc.window["listbox"].update(listboxList)

    gc.update(GUpdate=update)