"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
#Thread(target=DownloadVideo, args=[]).start()

"""

# Music Download
yt-dlp --extract-audio --audio-format mp3 -o "/path/to/output_folder/%(title)s.%(ext)s" <YouTube_URL>

# Video Download
yt-dlp -f "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]" -o "/path/to/output_folder/%(title)s_1080p.mp4" <YouTube_URL>

yt-dlp -f "bestvideo[ext=mp4][height=720]+bestaudio[ext=m4a]/best[ext=mp4][height=720]" -o "/path/to/output_folder/%(title)s_720p.mp4" <YouTube_URL>

yt-dlp -f "bestvideo[ext=mp4][height=480]+bestaudio[ext=m4a]/best[ext=mp4][height=480]" -o "/path/to/output_folder/%(title)s_480p.mp4" <YouTube_URL>

yt-dlp -f "bestvideo[ext=mp4][height=240]+bestaudio[ext=m4a]/best[ext=mp4][height=240]" -o "/path/to/output_folder/%(title)s_240p.mp4" <YouTube_URL>

"""


class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS
        self.C = GnuChanOSColor() 
        
        self.yt = "yt-dlp"

        # Video Quality
        self._1080 = "-f 'bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]'"
        

        self.VideoDownload = [
            [self.GC.GText(title="Video Download Settings", position="center", xStretch=True, bcolor=self.C.colors0)],
            [
                self.GC.GText("Link:", EmptySpace=(0, 0)),
                self.GC.GInput(xStretch=True, value="vlink", EmptySpace=(0, 0))
            ],

            [self.GC.GText(title="Video Quality Settings", xStretch=True, position="center", bcolor=self.C.colors0)],
            [self.GC.hsep(self.C.colors5)],
            [
                self.GC.Push(self.C.colors1),
                self.GC.GRadio(title="Very High(1080)", groupID="video", value="1080"),
                self.GC.GRadio(title="High(720)",       groupID="video", value="720"),
                self.GC.GRadio(title="Medium(480)",     groupID="video", value="480"),
                self.GC.GRadio(title="LOW(240)",        groupID="video", value="240"),
                self.GC.Push(self.C.colors1),
            ],
            [self.GC.hsep(self.C.colors5)],
            [
                self.GC.GButton(title="Select Output Dir"),
                self.GC.GButton(title="Download")
            ],
            [self.GC.GText(title="Output Dir Path Empty!", xStretch=True, bcolor=self.C.colors2, tcolor=self.C.colors0)],
            [self.GC.hsep(self.C.colors5)],
            [self.GC.GListBox(value="out", xStretch=True, yStretch=True)]
        ]

        self.MusicDownload = [
            [self.GC.GText(title="Music Download Settings", position="center", xStretch=True)]
        ]

        self.Layout = [
            [self.GC.GTabGroup(TabGroupLayout=[
                [self.GC.GTab(title="Video Download", TabLayout=self.VideoDownload, value="tab1")],
                [self.GC.GTab(title="Music Download", TabLayout=self.MusicDownload, value="tab2")],
            ], value="tabG")]
        ]

        # Create Window -> self.GC.window[]
        self.GC.GWindow(mainWindow=self.Layout)

        # Extra Lib
        self.KYB = GKeyboard(window=self.GC)

        # Settings
        self.GC.AddNewBorderWithColor(ThisWindow=self.GC.window, Value="out", Color="red", BorderSize=0)

        # Call Func
        self.GC.update(GUpdate=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        pass

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
