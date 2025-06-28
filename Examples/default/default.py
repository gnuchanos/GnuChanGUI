"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GCanvas, GVector2
from GnuChanGUI import GKeyboard as GK

# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GC.GCanvas(SetValue="canvas", xStretch=True, yStretch=True)]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        # Call Function Here

        self.Canvas = GCanvas(CanvasValue="canvas", Window=self.GC.GetWindow)
        self.player = self.Canvas.AddRectangleObject( "player",  GVector2(100, 100), GVector2(50, 50), self.C.blue1, self.C.yellow1, True )



        self.Canvas.Start()

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #if self.KYB.Return == self.GC.GetEvent -> Press key
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        
        if  self.GC.w == self.GC.CurrentKey:
            self.Canvas.MoveObject(self.player, 150, 'u', 'y')

        if self.GC.s == self.GC.CurrentKey:
            self.Canvas.MoveObject(self.player, 150, 'd', 'y')
        
        if self.GC.a == self.GC.CurrentKey:
            self.Canvas.MoveObject(self.player, 150, 'l', 'x')

        if self.GC.d == self.GC.CurrentKey:
            self.Canvas.MoveObject(self.player, 150, 'r', 'x')


        print(self.GC.CurrentKey)


    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
