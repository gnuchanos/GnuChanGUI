"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, GTime
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GMessage
from GnuChanGUI import GKeyboard_Winows, GTime

# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample(GnuChanGUI):
    def __init__(self, Title="Defaul Title", Size=(280, 60), resizable=False, finalize=True, winPosX=280/2+10, winPosY=50):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # old keyboard event
        self.Key = GKeyboard_Winows()


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GText(SetText="MIC OPEN", TPosition='c', xStretch=True, yStretch=True, SetValue="text", BColor=self.CGC.SColors1, TFont="Sans, 30")],
        ]

        self.MicON = True
        self.TimeOut = 1
        self.TimeOutReady = False
        self.Delta = GTime()

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        # Call Function Here

        self.WindowONTOP(0.6)

        # update window/getvalue

        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)
        
        #GMessage(WindowTitle="Warning", WindowText="Missing exitBEFORE Fuction in .update()")
        #GMessage(WindowTitle="Warning", WindowText="Missing exitBEFORE Fuction in .update()")

    def Update(self):
        #self.GetEvent == "event" -> window event
        #self.GetWindow["text"].update("this text") -> update window objects

        if self.Key.Numpad1 == self.CurrentKey:
            self.closeWindow = True

        

        if self.Key.NumpadAdd == self.CurrentKey and self.MicON and not self.TimeOutReady:
                self.GetWindow["text"].Update("MIC CLOSE")
                self.MicON = False
                self.TimeOutReady = True
        elif self.Key.NumpadAdd == self.CurrentKey and not self.MicON and not self.TimeOutReady:
                self.GetWindow["text"].Update("MIC OPEN")
                self.MicON = True
                self.TimeOutReady = True

        if self.TimeOutReady:
            if self.TimeOut > 0:
                self.TimeOut -= 1 * self.Delta.DeltaTime()
                print(self.TimeOut)
            else:
                self.TimeOut = 1
                self.TimeOutReady = False
                self.Delta.Ready()
                  

        self.StillONTOP_UnderUpdate()

    def BeforeExit(self):
        for i in range(30):
             print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
