"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GTimer


# Extra Lib


#Thread(target=DownloadVideo, args=[]).start()
class SimpleTimer(GnuChanGUI):
    def __init__(self, Title = "Defaul Title", Size = (600, 300), resizable = False, finalize = True, winPosX = 1920 / 2, winPosY = 1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)


        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # VAR


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GText(SetValue="timer", xStretch=True, BColor=self.CGC.SColors0, TPosition="center", TFont="Sans, 60")],
            [
                self.GButton(Text="Start Timer", SetValue="start", xStretch=True),
                self.GButton(Text="Clear Timer", SetValue="clear", xStretch=True),
            ],
            [self.GText(SetText="This Is Simple Timer Example", xStretch=True, yStretch=True, TPosition="center")]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)

        # Call Function Here
        self.StartTimer = GTimer()

        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        
        if self.GetEvent == "start":
            self.StartTimer.TimerStarts = True
        elif self.GetEvent == "clear":
            self.StartTimer.TimerStarts = False

        self.GetWindow["timer"].update(self.StartTimer.StringTime)



    def BeforeExit(self):
        print("Exit")
        self.StartTimer.TimerStarts = False
        self.StartTimer.KillThreads = True

if __name__ == "__main__":
    gc = SimpleTimer()
