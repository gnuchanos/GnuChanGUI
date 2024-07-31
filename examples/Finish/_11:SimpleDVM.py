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

        self.text = ""

        self.ly = [
            [self.GC.GText(title="Download Folder", xStretch=True)],
            [
                self.GC.Push,
                self.GC.GButton(title="Select Download folder"),
                self.GC.Push,
            ],
            [
                self.GC.Push,
                self.GC.GRadio(title="Music", groupID="yt_type", value="music"),
                self.GC.GRadio(title="Video", groupID="yt_type", value="video"),
                self.GC.Push,
            ],
            [
                self.GC.Push,
                self.GC.GRadio(title="Single Video", groupID="yt_list", value="singlelist"),
                self.GC.GRadio(title="PlayList Videos", groupID="yt_list", value="playlist"),
                self.GC.Push,
            ],
            [
                self.GC.GText(title="Link"),
                self.GC.GInput(value="link", xStretch=True, size=(20, None)),
                self.GC.GButton(title="Save Link")
            ],
            [
                self.GC.Push,
                self.GC.GButton(title="Download"),
                self.GC.Push,
            ]
        ]

        self.Layout = [
            [
                self.GC.vsep,
                self.GC.GColumn(winColumn=self.ly, xStretch=True, yStretch=True),
                self.GC.vsep,
            ]
        ]

        self.GC.GWindow(mainWindow=self.Layout)
        self.GC.update(GUpdate=self.Update, exitBEFORE=self.BeforeExit)
        self.KYB = GKeyboard(window=self.GC)

        self.FileType = ""
        self.listType = ""

    def Update(self):
        if self.GC.event in ["video", "music"]:
            self.FileType = self.GC.event
        elif self.GC.event in ["singlelist", "playlist"]:
            self.listType = self.GC.event

        
        if self.GC.event == "Download":
            if self.FileType != "" and self.listType != "":
                pass

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()