from GnuChanGUI import *


gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
]

gc.GWindow(mainWindow=layout)

def update():
    pass

gc.update(GUpdate=update)
gc.close
