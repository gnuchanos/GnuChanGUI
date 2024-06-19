"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread


#Thread(target=DownloadVideo, args=[]).start()



if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(1024, 900), resizable=True, finalize=True)
    gc.font = "Sans, 12"
    Themecolors().GnuChanOS


    menu = [
        ["File", ["Open File", "Save File", "Save As File"]],
            ]

    leftTextPart = [ [ gc.GMultiline(value="text", xStretch=True, yStretch=True, font="Sans, 20") ] ]

    layout = [ 
        [ gc.GMenuForTheme(menu, font="Sans, 15") ],
        [ gc.GColumn(winColumn=leftTextPart, xStretch=True, yStretch=True) ],
               ]

    gc.GWindow(mainWindow=layout)


    textOpen = FileSave(value="text", window=gc.window)
    def update():
        if gc.event == "Open File":
            textOpen.Open
        if gc.event == "Save File":
            textOpen.Save
        if gc.event == "Save As File":
            textOpen.SaveAs


        if gc.event == "File Tree Hide":
            gc.window["fileTree_panel"].update(visible=False)
        if gc.event == "File Tree Show":
            gc.window["fileTree_panel"].update(visible=True)


    gc.update(GUpdate=update)
