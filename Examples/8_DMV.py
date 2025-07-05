"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, Themecolors

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


class SimpleVideoAndMusicDownload(GnuChanGUI):
    def __init__(self, Title = "Defaul Title", Size = (1600, 900), resizable = False, finalize = True, winPosX = 1920 / 2, winPosY = 1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS
        self.C = GnuChanOSColor()
        
        self.yt = "yt-dlp"

        # Video Quality Note: This Place must update
        self.y1080 = "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]"
        self.y720  = "bestvideo[ext=mp4][height=720]+bestaudio[ext=m4a]/best[ext=mp4][height=720]"
        self.y480  = "bestvideo[ext=mp4][height=480]+bestaudio[ext=m4a]/best[ext=mp4][height=480]"
        self.y360  = "bestvideo[ext=mp4][height=360]+bestaudio[ext=m4a]/best[ext=mp4][height=360]"
        self.y240  = "bestvideo[ext=mp4][height=240]+bestaudio[ext=m4a]/best[ext=mp4][height=240]"

        self.Quality = ""
        self.Path    = ""
        self.Link    = ""
        
        self.VideoSettingsLayout = [
            [self.GText(SetText="Video Quality Settings", xStretch=True, TPosition="center", BColor=self.C.FColors1)],
            [self.GText(SetText="Warning If Video Don't Have 1080 You can't Download Please Open In Terminal For Control Error Log!", xStretch=True, TFont="Sans, 15")],
            [
                self.GPush(),
                self.GRadio(RText="Very High(1080)", groupID="video", SetValue="1080"),
                self.GRadio(RText="High(720)",       groupID="video", SetValue="720"),
                self.GRadio(RText="Medium(480)",     groupID="video", SetValue="480"),
                self.GRadio(RText="Medium(360)",     groupID="video", SetValue="360"),
                self.GRadio(RText="LOW(240)",        groupID="video", SetValue="240"),
                self.GPush(),
            ],
            [
                self.GPush(),
                self.GButton(Text="Select Output Dir", SetValue="path_video"),
                self.GButton(Text="Refresh List", SetValue="refrest_video"),
                self.GPush()
            ]
        ]

        self.VideoDownload = [
            [self.GText(SetText="Output Dir Path Empty!", xStretch=True, BColor=self.C.FColors2, TColor=self.C.TColor, SetValue="video_pathStr", TPosition="center", EmptySpace=(0, 0))],
            [
                self.GText(SetText="Link:", EmptySpace=(0, 0), BColor=self.C.FColors0),
                self.GInput(SetValue="vlink_video", xStretch=True, EmptySpace=(0, 0), BColor=self.C.FColors0)
            ],
            [self.GColumn(winColumnLayout_List=self.VideoSettingsLayout, xStretch=True)],
            [self.GHSep(self.C.FColors5)],
            [self.GListBox(SetValue="out_video", xStretch=True, yStretch=True)],
            [self.GHSep(self.C.FColors5)],
            [self.GButton(Text="Download",          SetValue="Download_Video"),],
            [self.GHSep(self.C.FColors5)],
        ]

        self.MusicDownload = [
            [
                self.GText(SetText="Link:", EmptySpace=(0, 0), BColor=self.C.FColors0),
                self.GInput(SetValue="vlink_music", xStretch=True, EmptySpace=(0, 0), BColor=self.C.FColors0)
            ],
            [self.GText(SetText="Output Dir Path Empty!", xStretch=True, BColor=self.C.FColors2, TColor=self.C.TColor, SetValue="music_pathStr", TPosition="center", EmptySpace=(0, 0))],
            [
                self.GButton(Text="Select Output Directory", SetValue="path_mp3"),
                self.GButton(Text="Refrest Music List", SetValue="rmusic")
            ],
            [self.GHSep(self.C.FColors5)],
            [self.GListBox(SetValue="out_music", xStretch=True, yStretch=True)],
            [self.GButton(Text="Download",          SetValue="Download_mp3")],
            [self.GHSep(self.C.FColors5)],
        ]

        self.Layout = [
            [self.GTabGroup(TabGroupLayout=[
                [self.GTab(Text="Video Download", TabLayout=self.VideoDownload, SetValue="tab1")],
                [self.GTab(Text="Music Download", TabLayout=self.MusicDownload, SetValue="tab2")],
            ], SetValue="tabG")]
        ]

        # Create Window -> self.GC.window[]
        self.GWindow(SetMainWindowLayout_List=self.Layout)

        # Settings
        self.GListBoxBorderSize(WindowValue="out_video", Border=0)
        self.GListBoxBorderSize(WindowValue="out_music", Border=0)

        # Call Func
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)
    
    def DownloadVideo(self, Download: str):
        os.system(Download)
        os.popen("notify-send -t 3500 -u low \"Video Download Finish Control Output Dir..!\"")
        self.GetWindow["vlink_video"].update("")

    def DownloadMusic(self, Download: str):
        os.system(Download)
        os.popen("notify-send -t 3500 -u low \"Video Download Finish Control Output Dir..!\"")
        self.GetWindow["vlink_music"].update("")

    def Update(self):
        # Download Video
        if self.GetEvent in ("1080", "720", "480", "360", "240"):
            self.Quality = self.GetEvent

        elif self.GetEvent == "path_video":
            try:
                self.Path = self.GetFolderPath(defaultPATH=f"{os.path.expanduser("~")}", noWindow=True, noTitleBar=True)
                if len(self.Path) > 0:
                    self.GetWindow["video_pathStr"].update(self.Path)
                    _list = os.listdir(self.Path)
                    _videoList = []
                    if _list != []:
                        for i in _list:
                            if str(i).endswith(".mp4"):
                                _videoList.append(i)
                        self.GetWindow["out_video"].update(_videoList)
            except Exception as ERR:
                print("ERR: ", ERR)

        elif self.GetEvent == "refrest_video":
            # update video file list
            if len(self.Path) > 0:
                _list = os.listdir(self.Path)
                _videoList = []
                if _list != []:
                    for i in _list:
                        if str(i).endswith(".mp4"):
                            _videoList.append(i)
                _videoList.sort()
                self.GetWindow["out_video"].update(_videoList)

        elif self.GetEvent == "Download_Video":
            try:
                if len(self.Quality) > 0:
                    self.Link = f"{self.GetValues["vlink_video"]}"
                    _DownloadThis = ""
                    if len(self.Path) > 0:
                        if len(self.Path) > 0:
                            if self.Quality == "1080":
                                _DownloadThis = self.y1080
                            elif self.Quality == "720":
                                _DownloadThis = self.y720
                            elif self.Quality == "480":
                                _DownloadThis = self.y480
                            elif self.Quality == "360":
                                _DownloadThis = self.y360
                            elif self.Quality == "240":
                                _DownloadThis = self.y240
                            
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
        elif self.GetEvent == "path_mp3":
            try:
                self.Path = self.GetFolderPath(defaultPATH=f"{os.path.expanduser("~")}", noWindow=True, noTitleBar=True)
                if len(self.Path) > 0:
                    self.GetWindow["music_pathStr"].update(self.Path)
                    _list = os.listdir(self.Path)
                    _musicList = []
                    if _list != []:
                        for i in _list:
                            if str(i).endswith(".mp3"):
                                _musicList.append(i)
                        self.GetWindow["out_music"].update(_musicList)
            except Exception as ERR:
                print(ERR)

        elif self.GetEvent == "Download_mp3":
            _dwn = self.GetValues["vlink_music"]
            if len(_dwn) > 0:
                _flags = "--extract-audio --audio-format mp3 -o"
                _Path        = f"{self.Path}/%(title)s.%(ext)s.mp3"
                _link        = _dwn
                _DownloadNow = f"{self.yt} {_flags} '{_Path}' '{_link}'"
                Thread(target=self.DownloadMusic, args=[_DownloadNow]).start()
                os.popen("notify-send -t 7000 -u low \"Music Download Starting..! Maybe Check Terminal\"")
                print(_DownloadNow)

        
        elif self.GetEvent == "rmusic":
            if len(self.Path) > 0:
                _list = os.listdir(self.Path)
                _musicList = []
                if _list != []:
                    for i in _list:
                        if str(i).endswith(".mp3"):
                            _musicList.append(i)
                    _musicList.sort()
                    self.GetWindow["out_music"].update(_musicList)

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleVideoAndMusicDownload()
