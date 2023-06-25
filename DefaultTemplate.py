from GnuChanGUI import *


gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]


import os
path = "C://Users//gnuchanos//Desktop"
dir_list = os.listdir(path)


mainWindow = [
    [gc.GButton(title="Files", font=gc.font), gc.GButton(title="Select", font=gc.font)],
    [gc.GText(title=path, value="path", font=gc.font, xStretch=True, position="center")],
    [gc.GListBox(list=dir_list, value="filesList", font=gc.font, xStretch=True, yStretch=True)],
    [gc.GImage(value="image", size=(5,5))]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GColumn(winColumn=mainWindow, xStretch=True, yStretch=True)]
]

gc.GWindow(mainWindow=layout)

imageOpener = OpenImage(imageListUpdate="filesList",
                        imageUpdate="image",
                        window=gc.window)

def GQ():
    global path
    if gc.event == "Files":
        imageOpener.OpenImageFolder
    if gc.event == "Select":
        imageOpener.ChooseImage(getValue=gc.GetValues)
gc.update(GUpdate=GQ)
gc.close
