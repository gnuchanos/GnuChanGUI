from GnuChanGUI import *
import webbrowser

gc = GnuChanGUI(Title="GnuChan Simple Text Editor", Size=(1024, 600), resizable=True)
gc.Theme()

gMenu = [
    ["File", ["Open File", "Save As", "Save"]],
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Font +", "Font -", "Exit"]] ]

filePath = "Open File or save File"
textEdit = [
    [gc.GMultiline(value="multiLineText", font=gc.font, xStretch=True, yStretch=True)],
    [gc.GText(title="File Path |:", font=gc.font), gc.GText(title=filePath, font=gc.font, value="textPath")] ]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GColumn(winColumn=textEdit, xStretch=True, yStretch=True)] ]

gc.GWindow(mainWindow=layout)
gc.GMultilineSpaceFixer(value="multiLineText")

textOpen = FileSave(getValue="multiLineText", value="multiLineText", filepath="textPath", window=gc.window)

def update():
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.itch.io/")
    if gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/@GnuChanOS")
    if gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")

    if gc.event == "Open File":
        textOpen.Open
    elif gc.event == "Save As":
        textOpen.SaveAs
    elif gc.event == "Save":
        textOpen.Save

    if gc.event == "Font +":
        gc.fontSizePlus(windowValue="multiLineText")
    if gc.event == "Font -":
        gc.fontSizeMinus(windowValue="multiLineText")


gc.update(GUpdate=update)
gc.close
