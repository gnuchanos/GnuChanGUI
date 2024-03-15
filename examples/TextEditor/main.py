"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *



if __name__ == "__main__":
    ScreenW = 900; ScreenH = 600
    gc = GnuChanGUI(Title="", Size=(ScreenW, ScreenH), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    simpleMenu = [
        ["File", ["Open File", "Save File", "Save As File"]],
    ]

    leftList = [
        [gc.GText(title="Little Help", xStretch=True, position="center", bcolor=GnuChanOSColor().colors2)],
        [gc.GListBox(list=[1,2,3,4,5], value="dir", font="Sans, 12", xStretch=True, yStretch=True, noScroolBar=True, bcolor=GnuChanOSColor().colors1)],
    ]
    
    layout = [
        [gc.GMenuForTheme(winMenu=simpleMenu)],
        [gc.GMultiline(value="text", font="Sans, 18", xStretch=True, yStretch=True, noScroolBar=False),
         gc.GFrame(winLayout=leftList, xStretch=True, yStretch=True, border=0)],
    ]

    gc.GWindow(mainWindow=layout)

    gc.GListBoxBorderSize(value="dir", border=0)
    gc.GMultilineTabSpace(gMultilineValue="text", gMultilineFont="Sans, 18")

    textFile = FileSave(window=gc.window, value="text")

    def update():
        if gc.event == "Open File":
            textFile.Open
        if gc.event == "Save File":
            textFile.Save
        if gc.event == "Save As File":
            textFile.SaveAs


    gc.update(GUpdate=update)