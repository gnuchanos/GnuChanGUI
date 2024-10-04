"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
#Thread(target=DownloadVideo, args=[]).start()


class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS




        tab1 = [
            [self.GC.GText(title="First Tab", xStretch=True, value="textvalue0", position="center", font="Sans, 20", bcolor=GColors().purple8)]
        ]
        
        tab2 = [
            [self.GC.GText(title="Second Tab", xStretch=True, value="textvalue1", position="center", font="Sans, 20", bcolor=GColors().LightPurple7)]
        ]








        self.Layout = [
            [
                self.GC.GPin(self.GC.GText(title="test", yStretch=True, xStretch=True, size=(10, None))),
                self.GC.GTabGroup(TabGroupLayout=[
                    [self.GC.GTab(title="test1", TabLayout=tab1, value="tab1")],
                    [self.GC.GTab(title="test2", TabLayout=tab2, value="tab2")],
                ], value="tabG")
            ]
        ]

        self.GC.GWindow(mainWindow=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        self.GC.update(GUpdate=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        pass

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
