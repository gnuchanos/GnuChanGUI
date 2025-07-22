"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, GTime
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GMessage
from GnuChanGUI import GKeyboard as GK

# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample(GnuChanGUI):
    def __init__(self, Title="Defaul Title", Size=(300, 300), resizable=False, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # old keyboard event
        self.Key = GK()


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text")],
            [
                self.GHSep(),
                self.GButton(Text="button", SetValue="click"),
                self.GHSep()
            ]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        # Call Function Here

        # update window/getvalue

        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #if self.KYB.Return == self.GC.GetEvent -> Press key
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects

        # keyboard example
        if self.Key.Return == self.GetEvent:
            GMessage(WindowTitle="old version keyboard event", WindowText="message YEY")
        
        if self.CurrentKey == self.space:
            GMessage(WindowTitle="new version keyboard event", WindowText="message YEY")

        # button and change text example
        if "click" == self.GetEvent:
            self.GetWindow["text"].update("button pressed")


    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
