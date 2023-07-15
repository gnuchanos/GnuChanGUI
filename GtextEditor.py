from GnuChanGUI import *


gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
gc.Theme()

gMenu = [
    ["File", ["Open File", "Save As", "Save"]],
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]

filePath = "Open File or save File"
textEdit = [
    [gc.GMultiline(value="multiLineText", focus="Sans, 25", xStretch=True, yStretch=True)],
    [gc.GText(title="File Path", font=gc.font), gc.GText(title=filePath, font=gc.font, value="textPath")]

]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GColumn(winColumn=textEdit, xStretch=True, yStretch=True)]
    
]

gc.GWindow(mainWindow=layout)
gc.GMultilineSpaceFixer(value="multiLineText")

textOpen = FileSave(getValue="multiLineText", value="multiLineText", filepath="textPath", window=gc.window)
def update():
    if gc.event == "Open File":
        textOpen.Open
    elif gc.event == "Save As":
        textOpen.SaveAs
    elif gc.event == "Save":
        textOpen.save
        print(gc.font, " | ", len(textOpen.filepath))

gc.update(GUpdate=update)
gc.close
