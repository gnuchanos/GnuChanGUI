"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""



from GnuChanGUI import *


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(300, 457), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    simpleMenu = [
        ["Help", ["Little Help"]],
    ]

    layout = [
        [gc.GMenuForTheme(winMenu=simpleMenu)],
        [gc.hsep],
        [gc.GText(value="math", xStretch=True, position="center", bcolor=GnuChanOSColor().colors5)],
        [gc.hsep],

        [gc.Push],

        [gc.hsep],
        [gc.GButton(title="1", xStretch=True), gc.GButton(title="2", xStretch=True), gc.GButton(title="2", xStretch=True)],
        [gc.GButton(title="3", xStretch=True), gc.GButton(title="4", xStretch=True), gc.GButton(title="5", xStretch=True)],
        [gc.GButton(title="6", xStretch=True), gc.GButton(title="7", xStretch=True), gc.GButton(title="8", xStretch=True)],
        [gc.GButton(title=".", xStretch=True), gc.GButton(title="0", xStretch=True), gc.GButton(title="<", xStretch=True)],
        [gc.hsep],

        [gc.Push],

        [gc.hsep],
        [gc.GButton(title="+", xStretch=True), gc.GButton(title="*", xStretch=True), gc.GButton(title="/", xStretch=True)],
        [gc.GButton(title="-", xStretch=True), gc.GButton(title="C", xStretch=True), gc.GButton(title="G", xStretch=True)],

        [gc.hsep],



               ]

    gc.GWindow(mainWindow=layout)

    def update():
        pass


    gc.update(GUpdate=update)