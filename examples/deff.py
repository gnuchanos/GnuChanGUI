from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
Themecolors().Green

gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]


layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    
    ]

gc.GWindow(mainWindow=layout)

def update():
    # gnuchanos pages
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")


gc.update(GUpdate=update)
