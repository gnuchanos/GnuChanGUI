from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=True)
Themecolors().Black

c = GColors()

layout = [ 
    [gc.GText(title="This is long text", font="Sans, 20", position="right", bcolor=c.red1, xStretch=True, yStretch=True), 
     gc.GButton(title="Button", xStretch=True, yStretch=True)],
     
    [gc.GText(title="This is long text", font="Sans, 20", position="right", bcolor=c.red1, xStretch=True)],
 ]


gc.GWindow(mainWindow=layout)

def update():
    pass

gc.update(GUpdate=update)
