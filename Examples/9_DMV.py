"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, Themecolors
from GnuChanGUI import GKeyboard

# Extra Lib
#Thread(target=DownloadVideo, args=[]).start()

"""

# Music Download
yt-dlp --extract-audio --audio-format mp3 -o "/path/to/output_folder/%(title)s.%(ext)s" <YouTube_URL>

# Video Download
yt-dlp -f "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]" -o "/path/to/output_folder/%(title)s_1080p.mp4" <YouTube_URL>

yt-dlp -f "bestvideo[ext=mp4][height=720]+bestaudio[ext=m4a]/best[ext=mp4][height=720]"   -o "/path/to/output_folder/%(title)s_720p.mp4" <YouTube_URL>

yt-dlp -f "bestvideo[ext=mp4][height=480]+bestaudio[ext=m4a]/best[ext=mp4][height=480]"   -o "/path/to/output_folder/%(title)s_480p.mp4" <YouTube_URL>

yt-dlp -f "bestvideo[ext=mp4][height=240]+bestaudio[ext=m4a]/best[ext=mp4][height=240]"   -o "/path/to/output_folder/%(title)s_240p.mp4" <YouTube_URL>

"""


class SimpleVideoAndMusicDownload:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS
        self.C = GnuChanOSColor()
        
        self.yt = "yt-dlp"

        # Video Quality
        self.y1080 = "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]"
        self.y720  = "bestvideo[ext=mp4][height=720]+bestaudio[ext=m4a]/best[ext=mp4][height=720]"
        self.y480  = "bestvideo[ext=mp4][height=480]+bestaudio[ext=m4a]/best[ext=mp4][height=480]"
        self.y240  = "bestvideo[ext=mp4][height=240]+bestaudio[ext=m4a]/best[ext=mp4][height=240]"

        self.Quality = ""
        self.Path    = ""
        self.Link    = ""
        
        self.VideoSettingsLayout = [
            [self.GC.GText(SetText="Video Quality Settings", xStretch=True, TPosition="center", BColor=self.C.FColors1)],
            [self.GC.GText(SetText="Warning If Video Don't Have 1080 You can't Download Please Open In Terminal For Control Error Log!", xStretch=True, TFont="Sans, 15")],
            [
                self.GC.GPush(),
                self.GC.GRadio(RText="Very High(1080)", groupID="video", SetValue="1080"),
                self.GC.GRadio(RText="High(720)",       groupID="video", SetValue="720"),
                self.GC.GRadio(RText="Medium(480)",     groupID="video", SetValue="480"),
                self.GC.GRadio(RText="LOW(240)",        groupID="video", SetValue="240"),
                self.GC.GPush(),
            ],
            [
                self.GC.GPush(),
                self.GC.GButton(Text="Select Output Dir", SetValue="path_video"),
                self.GC.GButton(Text="Refresh List", SetValue="refrest_video"),
                self.GC.GPush()
            ]
        ]

        self.VideoDownload = [
            [self.GC.GText(SetText="Output Dir Path Empty!", xStretch=True, BColor=self.C.FColors2, TColor=self.C.TColor, SetValue="video_pathStr", TPosition="center", EmptySpace=(0, 0))],
            [
                self.GC.GText(SetText="Link:", EmptySpace=(0, 0), BColor=self.C.FColors0),
                self.GC.GInput(SetValue="vlink_video", xStretch=True, EmptySpace=(0, 0), BColor=self.C.FColors0)
            ],
            [self.GC.GColumn(winColumnLayout_List=self.VideoSettingsLayout, xStretch=True)],
            [self.GC.GHSep(self.C.FColors5)],
            [self.GC.GListBox(SetValue="out_video", xStretch=True, yStretch=True)],
            [self.GC.GHSep(self.C.FColors5)],
            [self.GC.GButton(Text="Download",          SetValue="Download_Video"),],
            [self.GC.GHSep(self.C.FColors5)],
        ]

        self.MusicDownload = [
            [
                self.GC.GText(SetText="Link:", EmptySpace=(0, 0), BColor=self.C.FColors0),
                self.GC.GInput(SetValue="vlink_music", xStretch=True, EmptySpace=(0, 0), BColor=self.C.FColors0)
            ],
            [self.GC.GText(SetText="Output Dir Path Empty!", xStretch=True, BColor=self.C.FColors2, TColor=self.C.TColor, SetValue="music_pathStr", TPosition="center", EmptySpace=(0, 0))],
            [
                self.GC.GButton(Text="Select Output Directory", SetValue="path_mp3"),
                self.GC.GButton(Text="Refrest Music List", SetValue="rmusic")
            ],
            [self.GC.GHSep(self.C.FColors5)],
            [self.GC.GListBox(SetValue="out_music", xStretch=True, yStretch=True)],
            [self.GC.GButton(Text="Download",          SetValue="Download_mp3")],
            [self.GC.GHSep(self.C.FColors5)],
        ]

        self.Layout = [
            [self.GC.GTabGroup(TabGroupLayout=[
                [self.GC.GTab(Text="Video Download", TabLayout=self.VideoDownload, SetValue="tab1")],
                [self.GC.GTab(Text="Music Download", TabLayout=self.MusicDownload, SetValue="tab2")],
            ], SetValue="tabG")]
        ]

        # Create Window -> self.GC.window[]
        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)

        # Extra Lib
        self.KYB = GKeyboard(window=self.GC)

        # Settings
        self.GC.GListBoxBorderSize(WindowValue="out_video", Border=0)
        self.GC.GListBoxBorderSize(WindowValue="out_music", Border=0)

        # Call Func
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)
    
    def DownloadVideo(self, Download: str):
        os.system(Download)
        os.popen("notify-send -t 3500 -u low \"Video Download Finish Control Output Dir..!\"")
        self.GC.GetWindow["vlink_video"].update("")

    def DownloadMusic(self, Download: str):
        os.system(Download)
        os.popen("notify-send -t 3500 -u low \"Video Download Finish Control Output Dir..!\"")
        self.GC.GetWindow["music_pathStr"].update("")

    def Update(self):
        # Download Video
        if self.GC.GetEvent in ("1080", "720", "480", "240"):
            self.Quality = self.GC.GetEvent

        elif self.GC.GetEvent == "path_video":
            try:
                self.Path = self.GC.GetFolderPath(defaultPATH=f"{os.path.expanduser("~")}", noWindow=True, noTitleBar=True)
                if len(self.Path) > 0:
                    self.GC.GetWindow["video_pathStr"].update(self.Path)
                    _list = os.listdir(self.Path)
                    _videoList = []
                    if _list != []:
                        for i in _list:
                            if str(i).endswith(".mp4"):
                                _videoList.append(i)
                        self.GC.GetWindow["out_video"].update(_videoList)
            except Exception as ERR:
                print("ERR: ", ERR)

        elif self.GC.GetEvent == "refrest_video":
            # update video file list
            if len(self.Path) > 0:
                _list = os.listdir(self.Path)
                _videoList = []
                if _list != []:
                    for i in _list:
                        if str(i).endswith(".mp4"):
                            _videoList.append(i)
                _videoList.sort()
                self.GC.GetWindow["out_video"].update(_videoList)

        elif self.GC.GetEvent == "Download_Video":
            try:
                if len(self.Quality) > 0:
                    self.Link = f"{self.GC.GetValues["vlink_video"]}"
                    _DownloadThis = ""
                    if len(self.Path) > 0:
                        if len(self.Path) > 0:
                            if self.Quality == "1080":
                                _DownloadThis = f"{self.y1080}"
                            elif self.Quality == "720":
                                _DownloadThis = f"{self.y720}"
                            elif self.Quality == "480":
                                _DownloadThis = f"{self.y480}"
                            elif self.Quality == "240":
                                _DownloadThis = f"{self.y240}"
                            
                            if len(self.Link) > 0:
                                _DownloadNow = f"{self.yt} -f '{_DownloadThis}' -o '{self.Path}/%(title)s_{self.Quality}p.mp4' '{self.Link}'"
                                Thread(target=self.DownloadVideo, args=[_DownloadNow]).start()
                                os.popen("notify-send -t 7000 -u low \"Video Download Starting..! Maybe Check Terminal\"")
                                print(_DownloadNow)
                    else:
                        print("Empy Path")
            except Exception as ERR:
                print(ERR)
        
        # Music Download
        elif self.GC.GetEvent == "path_mp3":
            try:
                self.Path = self.GC.GetFolderPath(defaultPATH=f"{os.path.expanduser("~")}", noWindow=True, noTitleBar=True)
                if len(self.Path) > 0:
                    self.GC.GetWindow["music_pathStr"].update(self.Path)
                    _list = os.listdir(self.Path)
                    _musicList = []
                    if _list != []:
                        for i in _list:
                            if str(i).endswith(".mp3"):
                                _musicList.append(i)
                        self.GC.GetWindow["out_music"].update(_musicList)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Download_mp3":
            _dwn = self.GC.GetValues["vlink_music"]
            if len(_dwn) > 0:
                _flags = "--extract-audio --audio-format mp3 -o"
                _Path        = f"{self.Path}/%(title)s.%(ext)s.mp3"
                _link        = _dwn
                _DownloadNow = f"{self.yt} {_flags} '{_Path}' '{_link}'"
                Thread(target=self.DownloadMusic, args=[_DownloadNow]).start()
                os.popen("notify-send -t 7000 -u low \"Music Download Starting..! Maybe Check Terminal\"")
                print(_DownloadNow)

        
        elif self.GC.GetEvent == "rmusic":
            if len(self.Path) > 0:
                _list = os.listdir(self.Path)
                _musicList = []
                if _list != []:
                    for i in _list:
                        if str(i).endswith(".mp3"):
                            _musicList.append(i)
                    _musicList.sort()
                    self.GC.GetWindow["out_music"].update(_musicList)

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    SimpleVideoAndMusicDownload()
