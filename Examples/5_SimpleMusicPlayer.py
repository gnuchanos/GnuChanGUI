"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GMixer

# Extra Lib



#Thread(target=DownloadVideo, args=[]).start()
class SimpleMusicPlayer(GnuChanGUI):
    def __init__(self, Title = "Defaul Title", Size = (1600, 900), resizable = False, finalize = True, winPosX = 1920 / 2, winPosY = 1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        self.Buttons = [
            [
                self.GPush(BColor=self.C.purple8),
                self.GButton(Text="Add Folder"),
                self.GButton(Text="<", SetValue="Previous Music"),
                self.GButton(Text="Play Music"),
                self.GButton(Text="Stop Music"),
                self.GButton(Text=">", SetValue="Next Music"),
                self.GPush(BColor=self.C.purple8)
            ],
        ]

        # main window layout you can use column and frame in here
        self.Layout = [
            [
                self.GText(SetText=f"{os.path.expanduser("~")}/", BColor=self.C.purple7, EmptySpace=(0, 0)), 
                self.GInput(SetValue="input", xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))
            ],
            [self.GColumn(winColumnLayout_List=self.Buttons, xStretch=True, BColor=self.C.purple8)],
            [ 
                self.GVSep(Color=self.CGC.FColors3),
                self.GListBox(SetValue="mp3", Size=(75, None), LFont="Sans, 15", xStretch=True, yStretch=True, BColor=self.CGC.FColors1, EmptySpace=(0, 0)),
                self.GVSep(Color=self.CGC.FColors3),
            ],
            [ 
                self.GText(SetText="Music: ", BColor=self.C.purple8, EmptySpace=(0, 0)), 
                self.GText(SetValue="musicName", TPosition="center",  BColor=self.C.purple8, xStretch=True, EmptySpace=(0, 0)) 
            ],
            [self.GSlider(MaxRange=(0, 10), DefaultValue=5, SDirection="h", SetValue="slider", xStretch=True, BColor=self.C.purple8)   ]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)




        # Call Function Here
        self.GetWindow["input"].update("Music")
        self.GListBoxBorderSize(WindowValue="mp3", Border=0)

        self.musicPlay = GMixer()

        self.dir = os.path.expanduser("~")
        self.path = ""
        self.volume = 5
        self.volume_slider = 5
        self.fileList = []
        self.musicList = []
        self.musicIndex = 0
        self.musicSelect = ""
        self.start = False

        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def MusicPlay(self):
        if self.GetEvent == "Add Folder":
            try:
                self.musicPlay.SoundFileList = []
                self.path = f"{self.dir}/{self.GetValues["input"]}"
                self.fileList = os.listdir(path=self.path)
                for i in self.fileList:
                    if i.endswith(".mp3"):
                        self.musicPlay.SoundFileList.append(f"{self.path}/{i}")
                self.musicPlay.SoundFileList.sort()
                self.GetWindow["mp3"].update(self.musicPlay.SoundFileList)
            except Exception as ERR:
                print (f"{ERR}")

        if self.GetEvent == "Play Music":
            if not self.start:
                self.musicPlay.PlaySound_SingleChannel(SoundPath=self.GetValues["mp3"][0])
                self.GetWindow["musicName"].update(self.GetValues["mp3"][0])

        elif self.GetEvent == "Stop Music":
            self.musicPlay.StopSound()

        elif self.GetEvent == "Next Music" or self.num1 == self.CurrentKey:
            if not self.start:
                _musicName = self.musicPlay.NextSound_SingleChannel()
                self.GetWindow["musicName"].update(self.musicPlay.MusicName)

        elif self.GetEvent == "Previous Music" or self.num2 == self.CurrentKey:
            if not self.start:
                _musicName = self.musicPlay.PreviousSound_SingleChannel()
                self.GetWindow["musicName"].update(self.musicPlay.MusicName)

    def volume_func(self):
        self.volume_slider = int(self.GetValues["slider"])
        if self.volume_slider != 10:
            self.volume = float(self.volume_slider)
        else:
            self.volume = 10

        self.musicPlay.VolumeChange_Gslider(self.volume)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        Thread(target=self.MusicPlay, args=[]).start()
        Thread(target=self.volume_func, args=[]).start()

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleMusicPlayer()
