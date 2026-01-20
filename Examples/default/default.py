"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, GTime
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GMessage
from GnuChanGUI import GKeyboard_Winows as GK_Windolf

# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample(GnuChanGUI):
    def __init__(self, Title="Defaul Title", Size=(600, 300), resizable=False, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # old keyboard event
        self.Key_Windolf = GK_Windolf()


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text")],
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text2")],
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text3")],
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
        #self.GetEvent == "event" -> window event
        #self.GetWindow["text"].update("this text") -> update window objects

        # keyboard example
        if self.CurrentKey == self.Enter:
            GMessage(WindowTitle="old version keyboard event", WindowText="message YEY")

        # keyboard example WINDOLF
        if self.CurrentKey == self.Key_Windolf.NumpadAdd:
            GMessage(WindowTitle="old version keyboard event", WindowText="message YEY")


        print(self.CurrentKey, " : ", self.Key_Windolf.NumpadAdd)

      
        # button and change text example
        if "click" == self.GetEvent:
            self.GetWindow["text"].update("button pressed")


    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
