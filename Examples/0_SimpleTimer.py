"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard
from GnuChanGUI import GTimer


# Extra Lib


#Thread(target=DownloadVideo, args=[]).start()
class SimpleTimer:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title="Simple Timer!", Size=(700, 228), resizable=False, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # VAR


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GC.GText(SetValue="timer", xStretch=True, BColor=self.CGC.SColors0, TPosition="center", TFont="Sans, 60")],
            [
                self.GC.GButton(Text="Start Timer", SetValue="start", xStretch=True),
                self.GC.GButton(Text="Stop Timer", SetValue="stop", xStretch=True),
                self.GC.GButton(Text="Clear Timer", SetValue="clear", xStretch=True),
            ],
            [self.GC.GText(SetText="This Is Simple Timer Example", xStretch=True, yStretch=True, TPosition="center")]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        # Call Function Here
        self.StartTimer = GTimer(GetWindow=self.GC.GetWindow, SetValue="timer")
        self.IsClear = False

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        
        if self.GC.GetEvent == "start":
            self.StartTimer.RecordUpdateTRUE = True
            self.IsClear = False
        elif self.GC.GetEvent == "stop":
            self.StartTimer.RecordUpdateTRUE = False
        elif self.GC.GetValues == "clear":
            self.IsClear = True

        self.StartTimer.Start

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    SimpleTimer()
