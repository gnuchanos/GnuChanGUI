from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
Themecolors().GnuChanOS

gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]

screen = [[gc.GText(title="", value="screen", xStretch=True, position="center")]]

buttons = [
    [gc.GButton(title="Play", font="Sans, 20", xStretch=True),
     gc.GButton(title="Stop", font="Sans, 20", xStretch=True),
     gc.GButton(title="Music Folder", font="Sans, 20", xStretch=True),
     gc.GButton(title="Clear List", font="Sans, 20", xStretch=True)] ]

playList = [
    [gc.GListBox(value="playlist", font="Sans, 20", position="center", xStretch=True, yStretch=True)],
    [gc.GText(title="Beta 0.1", font="Sans, 20", xStretch=True)] ]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GColumn(winColumn=screen, xStretch=True)],
    [gc.GColumn(winColumn=buttons, xStretch=True)],
    [gc.GColumn(winColumn=playList, xStretch=True, yStretch=True)]
    
    ]

gc.GWindow(mainWindow=layout)
gc.GListBoxBorderSize(value="playlist", border=0)

def update():
    # gnuchanos pages
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")


gc.update(GUpdate=update)
