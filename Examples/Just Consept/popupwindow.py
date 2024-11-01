"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
import screeninfo
#Thread(target=DownloadVideo, args=[]).start()

class GMessage:
    def __init__(self,
                 WindowText = "EKMEK ALMAYA GİTTİM ABONE OL PİLİS", WindowTextFont = "Sans", WindowTextFontSize = 20,
                 WindowTBC = GnuChanOSColor().FColors1, ButtonLBC = GnuChanOSColor().FColors5,
                 WindowTitle="Default Title", WindowSize=(600, 300), WindowResizable = False
        ) -> None:


        self.GC = GnuChanGUI(Title=WindowTitle, Size=WindowSize, resizable=WindowResizable, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color

        self.WindowTitle = WindowTitle
        self.TextFont = f"{WindowTextFont}, {WindowTextFontSize}"
        self.WindowTextBackgroundColor = WindowTBC
        self.ButtonLayoutBackgroundColor = ButtonLBC

        # main window layout you can use column and frame in here
        self.button = [
            [
                self.GC.GPush(GnuChanOSColor().FColors11),
                self.GC.GButton(Text = "Exit"),
                self.GC.GPush(GnuChanOSColor().FColors11),
            ]
        ]

        self.Layout = [
            [self.GC.GMultiline(
                InText=WindowText, TFont=self.TextFont, TPosition="center", 
                xStretch=True, yStretch=True, BColor=self.WindowTextBackgroundColor, ReadOnly=True
            )],
            [self.GC.GColumn(winColumnLayout_List=self.button, BColor=self.ButtonLayoutBackgroundColor, xStretch=True)]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout, locationX=1024/2-300, locationY=768/2-150)
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.GC.GetEvent == "exit":
            self.GC.closeWindow = True

    def BeforeExit(self):
        print(f"{self.WindowTitle} is closed")

if __name__ == "__main__":
    GMessage()
