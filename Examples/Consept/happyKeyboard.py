"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, time
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard


# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()


class Key:
    def __init__(self, timepp, key):
        self.timepp = timepp
        self.key = key
        self.works = False

    def press_key(self):
        while True:
            if self.works:
                time.sleep(self.timepp)
                os.popen(f"xdotool key {self.key}")
            else:
                break

class Timer:
    def __init__(self):
        pass


class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(300, 450), resizable=False, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        self.happy = 0

        self.happykey0 = Key(0.1, "grave")
        self.happykey0.works = False
        self.happyEvent = None
        

        self.buttonArea = [
            [
                self.GC.GPush(BColor=self.CGC.SColors0),
                self.GC.GButton(SetValue="rmutlu", xStretch=True),
                self.GC.GPush(BColor=self.CGC.SColors0),
            ],

            [
                self.GC.GPush(BColor=self.CGC.SColors0),
                self.GC.GButton(Text="+ Mutlu", SetValue="+", xStretch=True),
                self.GC.GButton(Text="- Mutlu", SetValue="-", xStretch=True),
                self.GC.GPush(BColor=self.CGC.SColors0),
            ],
        ]

        self.InsideWindow = [
            [self.GC.GText(SetText="Mutlu Pencere", xStretch=True, TPosition="center")],
            [self.GC.GColumn(winColumnLayout_List=self.buttonArea, xStretch=True, BColor=self.CGC.SColors0)],
            [self.GC.GText(SetText=f"Happy Point: {self.happy}", SetValue="happy", xStretch=True, BColor=self.C.purple5)],
            [self.GC.GMultiline(xStretch=True, yStretch=True, SetValue="mtext", ReadOnly=True, TFont="sans, 20", BColor=self.C.purple8)]
        ]

        # main window layout you can use column and frame in here
        self.Layout = [
            [
                self.GC.GPush(),
                self.GC.GColumn(winColumnLayout_List=self.InsideWindow, xStretch=True, yStretch=True),
            ],
            [self.GC.GButton(Text="DIE", xStretch=True)]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        # Call Function Here

        self.GC.GetWindow["mtext"].update("Evet canım, sıkıldığı için böyle bir program yazdım. Abone ol!")
        self.GC.GetWindow["happy"].update(f"Happy Point: {self.happy}")
        self.GC.GetWindow["rmutlu"].update("Mutlu Button 0")

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        if "rmutlu" == self.GC.GetEvent:
            if not self.happykey0.works:
                self.happykey0.works = True
                self.GC.GetWindow["rmutlu"].update("Mutlu Button 1")
                self.happyEvent = Thread(target=self.happykey0.press_key)
                self.happyEvent.start()
            else:
                self.happykey0.works = False
                self.happyEvent.join()
                self.GC.GetWindow["rmutlu"].update("Mutlu Button 0")

        elif "DIE" == self.GC.GetEvent:
            self.GC.closeWindow = True

        elif "+" == self.GC.GetEvent:
            self.happy += 1
            self.GC.GetWindow["happy"].update(f"Happy Point: {self.happy}")
        elif "-" == self.GC.GetEvent:
            self.happy -= 1
            self.GC.GetWindow["happy"].update(f"Happy Point: {self.happy}")


    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
