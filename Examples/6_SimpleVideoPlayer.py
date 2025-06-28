"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors





# Extra Lib
import vlc



#Thread(target=DownloadVideo, args=[]).start()
class SimpleVideoPlayer:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        self.vlc_instance = vlc.Instance()
        self.player = self.vlc_instance.media_player_new()

        self.vid = [
            [self.GC.GCanvas(SetValue="canvas", xStretch=True, yStretch=True, Size=(750, None), BColor=self.CGC.FColors1, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Open Video!", SetValue="video_name", xStretch=True, TPosition="center", EmptySpace=(0, 0))],
        ]

        self.left = [
            [self.GC.GListBox(SetValue="videos", LFont="Sans, 12", yStretch=True, xStretch=True, BColor=self.CGC.FColors2, noScroolBar=True)],
        ]


        # main window layout you can use column and frame in here
        self.Layout = [
            [
                self.GC.GPush(BColor=self.CGC.BGColor),
                self.GC.GButton(Text="<"),
                self.GC.GButton(Text="Open Video"),
                self.GC.GButton(Text="Open Video Folder"),
                self.GC.GButton(Text="Pause", SetValue="pPlay"),
                self.GC.GButton(Text=">"),
                self.GC.GPush(BColor=self.CGC.BGColor),
            ],
            [self.GC.GText(SetText="Volume Slider", xStretch=True, TPosition="center")],
            [self.GC.GSlider(SetValue="volume", xStretch=True, MaxRange=(0, 100), DefaultValue=80, BColor=self.CGC.FColors4)],
            [
                self.GC.GColumn(winColumnLayout_List=self.vid,  xStretch=True, yStretch=True, BColor=self.CGC.FColors8),
                self.GC.GColumn(winColumnLayout_List=self.left, xStretch=True, yStretch=True, BColor=self.CGC.FColors6, SetValue="filePath"),
            ],
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)




        # Call Function Here

        self.GC.GListBoxBorderSize(WindowValue="videos", Border=0)
        self.cans = self.GC.GetWindow["canvas"].Widget

        self.player.set_xwindow(self.cans.winfo_id()) # vscode can't auto-completed this .winfo_id()

        self._Pause = False
        self._videoFinish = False
        self._startVideo = False
        self._readyPlay = False
        self._folderPath = ""
        self.video = ""
        self.videos = []
        self._index = 0
        self.hideTree = False

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects

        try:
            if self.GC.enter == self.GC.CurrentKey:
                try:
                    self.video = self.vlc_instance.media_new(f"{self._folderPath}/{self.videos[self.videos.index(str(self.GC.GetValues["videos"]).strip("[]'"))]}")
                    self.player.set_media(self.video)
                    self.player.play()
                except Exception as ERR:
                    print(ERR, " Return Key Press ERR")

            if self.GC.GetEvent == "Open Video":
                self._startVideo = True
                self._Pause = False
                self._videoPath = self.GC.GetFilePath(defaultPATH=str(os.path.expanduser("~")), fileTypes=self.GC.VideoTypes)
                if os.path.exists(self._videoPath):
                    self.player.stop()
                    video = self.vlc_instance.media_new(self._videoPath)
                    self.player.set_media(video)
                    self.player.play()
                    self.GC.GetWindow["video_name"].update(self._videoPath)

            elif self.GC.GetEvent == "Open Video Folder":
                self._readyPlay = True
                self._startVideo = True
                self._Pause = False
                self._folderPath = self.GC.GetFolderPath(defaultPATH=str(os.path.expanduser("~")))
                self._defaultList = os.listdir(self._folderPath)
                for i in self._defaultList:
                    if str(i).endswith(".mp4") or str(i).endswith(".mkv"):
                        self.videos.append(i)

                self.GC.GetWindow["videos"].update(self.videos)
                _videoPath = f"{self._folderPath}/{self.videos[0]}"
                video = self.vlc_instance.media_new(_videoPath)
                self.player.set_media(video)
                self.player.play()
                self.GC.GetWindow["video_name"].update(_videoPath)

            elif self.GC.GetEvent == "pPlay":
                if self._startVideo:
                    if self._Pause:
                        self.player.play()
                        self.GC.GetWindow["pPlay"].update("Pause")
                        self._Pause = False
                    else:
                        self.player.pause()
                        self.GC.GetWindow["pPlay"].update("Play")
                        self._Pause = True

            if self.GC.GetEvent == "<":
                try:
                    if self._readyPlay:
                        if self._index > 0:
                            self._index -= 1
                            self.player.stop()

                            _path = f"{self._folderPath}/{self.videos[self._index]}"
                            if os.path.exists(_path):
                                print(_path)
                                self.video = self.vlc_instance.media_new(_path)
                                self.player.set_media(self.video)
                                self.player.play()

                except Exception as ERR:
                    print(ERR, " < button ERR")

            if self.GC.GetEvent == '>':
                if self._readyPlay:
                    if self._index < len(self.videos) - 1:
                        self._index += 1
                        self.player.stop()

                        _path = f"{self._folderPath}/{self.videos[self._index]}"
                        if os.path.exists(_path):
                            print(_path)
                            self.video = self.vlc_instance.media_new(_path)
                            self.player.set_media(self.video)
                            self.player.play()

            if self.GC.KeyPressed(Key=self.GC.h):
                print("hello")
                if not self.hideTree:
                    self.GC.GetWindow["filePath"].update(visible=False)
                    self.hideTree = True
                else:
                    self.GC.GetWindow["filePath"].update(visible=True)
                    self.hideTree = False

            self.player.audio_set_volume(int(self.GC.GetValues["volume"]))

        except Exception as ERR:
            print(ERR)

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleVideoPlayer()
