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

        self.second = 0

        self.Layout = [
            [self.GC.GText(title="Test")]
        ]

        self.GC.GWindow(mainWindow=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        self.GC.update(GUpdate=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        self.second += 1
        print(self.second)

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()