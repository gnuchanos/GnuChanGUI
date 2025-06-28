"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, time
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors




# Extra Lib
from datetime import datetime



#gpu-screen-recorder -w DVI-D-0 -k h264 -ac aac -c flv -a "default_input|$(pactl get-default-sink).monitor" -f 30 -q medium -ab 256 -o /home/archkubi/Videos/test-2024-12-22_9-15-38.mkv



#Thread(target=DownloadVideo, args=[]).start()
class SimpleRecordAndLivestream:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        # VAR
        self.GC.font = "Sans, 12"

        self.Rtmp = "rtmp://a.rtmp.youtube.com/live2"
        self.Key = ""
        self.StreamKey = ""
        self.VideoPath = self.VideoName = ""
        self.StartRS = False
        self.DesktopID = "DVI-D-0 "
        self.MonutorID = "$(pactl get-default-sink).monitor\""
        self.MicrophoneName = "\"default_input|"
        self.DisableMicrophone = False
        self.GSR          = "gpu-screen-recorder "
        self.Codecs       = "-k h264 -ac aac -c flv "
        self.Fps          = "-f 30 "
        self.VideoQuality      = "-q medium "
        self.SoundQuality = "-ab 256 "

        # VAR



        self.QualitySettings = [
            [
                self.GC.GPush(BColor=self.CGC.FColors2),
                self.GC.GRadio(SetValue="14",  groupID="fps", RText="14-FPS",  BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="24",  groupID="fps", RText="24-FPS",  BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="30",  groupID="fps", RText="30-FPS",  BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="60",  groupID="fps", RText="60-FPS",  BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="120", groupID="fps", RText="120-FPS", BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GPush(BColor=self.CGC.FColors2),
            ],
            [
                self.GC.GText(SetText="Video FPS: ", BColor=self.CGC.FColors2),
                self.GC.GText(SetText=self.Fps, SetValue="fps_log", xStretch=True, TPosition="center", BColor=self.C.purple6)
            ]
        ]

        self.SoundQualitySettings = [
            [
                self.GC.GPush(BColor=self.CGC.FColors2),
                self.GC.GRadio(SetValue="128", groupID="Kbps", RText="128 Kbps", BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="192", groupID="Kbps", RText="192 Kbps", BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="256", groupID="Kbps", RText="256 Kbps", BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="320", groupID="Kbps", RText="320 Kbps", BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GPush(BColor=self.CGC.FColors2),
            ],
            [
                self.GC.GText(SetText="Sound Quality: ", BColor=self.CGC.FColors2),
                self.GC.GText(SetText=self.SoundQuality, SetValue="sound_log", xStretch=True, TPosition="center", BColor=self.C.purple6)
            ]
        ]

        self.VideoQualitySettings = [
            [
                self.GC.GPush(BColor=self.CGC.FColors2),
                self.GC.GRadio(SetValue="Medium",    groupID="quality", RText="Medium",    BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="High",      groupID="quality", RText="High",      BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="Very_High", groupID="quality", RText="Very High", BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GRadio(SetValue="Ultra",     groupID="quality", RText="Ultra",     BColor=self.CGC.FColors2, TFont=self.GC.font),
                self.GC.GPush(BColor=self.CGC.FColors2),
            ],
            [
                self.GC.GText(SetText="Video Quality: ", BColor=self.CGC.FColors2),
                self.GC.GText(SetText=self.VideoQuality, SetValue="video_log", xStretch=True, TPosition="center", BColor=self.CGC.FColors2)
            ]
        ]

        self.SettingsWindow = [
            [   
                self.GC.GText(SetText=" Monutor ID 'xrandr here': ", TFont=self.GC.font, BColor=self.CGC.FColors2),
                self.GC.GInput(SetValue="mID", xStretch=True, Size=(20, None), TFont=self.GC.font, BColor=self.C.purple6)
            ],
        ]

        self.DisableAndEnable = [
            [
                self.GC.GPush(BColor=self.CGC.FColors2),
                self.GC.GButton(Text="Disable Microphone", SetValue="md"),
                self.GC.GPush(BColor=self.CGC.FColors2)
            ]
        ]

        self.SettingsTab = [
            [self.GC.GText(SetText="Settings Tab", xStretch=True, TPosition="center", BColor=self.CGC.FColors5, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.SettingsWindow, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Video FPS",    xStretch=True, TPosition="center", BColor=self.CGC.FColors5, TFont=self.GC.font, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.QualitySettings, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Sound Quality",    xStretch=True, TPosition="center", BColor=self.CGC.FColors5, TFont=self.GC.font, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.SoundQualitySettings, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Video Quality",    xStretch=True, TPosition="center", BColor=self.CGC.FColors5, TFont=self.GC.font, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.VideoQualitySettings, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Open or Close Microphone", xStretch=True, TPosition="center", BColor=self.CGC.FColors5, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.DisableAndEnable, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))]
        ]

        self.ScreenRecordParts = [
            [   
                self.GC.GText(SetText="RTMP URL: ", TFont=self.GC.font, BColor=self.CGC.FColors2),
                self.GC.GInput(SetValue="rtmp", xStretch=True, Size=(20, None), TFont=self.GC.font, BColor=self.C.purple6)
            ],
            [   
                self.GC.GText(SetText="Stream key: ", TFont=self.GC.font, BColor=self.CGC.FColors2),
                self.GC.GInput(SetValue="skey", xStretch=True, HidePassword="*", Size=(20, None), TFont=self.GC.font, BColor=self.C.purple6)
            ],
            [self.GC.GText(SetText="Don't Forget Save Stream key", SetValue="ready", TFont=self.GC.font, BColor=self.CGC.FColors2)],
            [   
                self.GC.GPush(BColor=self.CGC.FColors2),
                self.GC.GButton(Text="Save Stream Key", TFont=self.GC.font),
                self.GC.GButton(Text="Start Live Stream", TFont=self.GC.font), 
                self.GC.GButton(Text="Stop Live Stream", TFont=self.GC.font),
                self.GC.GPush(BColor=self.CGC.FColors2),
            ],
        ]

        self.ScreenRecordPartsTab = [
            [self.GC.GText(SetText="Screen Live Stream Tab", xStretch=True, TPosition="center", BColor=self.CGC.FColors5, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.ScreenRecordParts, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
        ]

        self.InputAndButtonsVideoRecord = [
            [   
                self.GC.GText(SetText="Video Name: ", TFont=self.GC.font, BColor=self.CGC.FColors2), 
                self.GC.GInput(SetValue="vname", Size=(20, None), xStretch=True, TFont=self.GC.font, BColor=self.C.purple6)   
            ],
            [
                self.GC.GPush(BColor=self.CGC.FColors2),
                    self.GC.GButton(Text="Select Video Directory", TFont=self.GC.font),
                    self.GC.GButton(Text="Video Name Save", TFont=self.GC.font),
                    self.GC.GButton(Text="Start Record", TFont=self.GC.font),
                    self.GC.GButton(Text="Stop Record", TFont=self.GC.font),
                    self.GC.GButton(Text="Refresh Video List", TFont=self.GC.font),
                    self.GC.GButton(Text="Remove Video", TFont=self.GC.font),
                self.GC.GPush(BColor=self.CGC.FColors2),
            ],
        ]

        self.ScreenRecordTabPart = [
            [self.GC.GText(SetText="File Path Here!", SetValue="path", xStretch=True, BColor=self.CGC.FColors2, TFont=self.GC.font, EmptySpace=(0, 0))],
            [
                self.GC.GText(SetText="Video Name: ", EmptySpace=(0, 0), BColor=self.CGC.FColors2),
                self.GC.GText(SetText="Start Record Video", SetValue="video_name", EmptySpace=(0, 0), BColor=self.CGC.FColors2)
            ],
            [self.GC.GColumn(winColumnLayout_List=self.InputAndButtonsVideoRecord, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Directory Video List", xStretch=True, TPosition="center", BColor=self.CGC.FColors5, EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="videos", xStretch=True, yStretch=True, noScroolBar=True, BColor=self.CGC.FColors0, LPosition="center", EmptySpace=(0, 0))]
        ]

        self.ScreenRecordTab = [
            [self.GC.GText(SetText="Screen Record Tab", xStretch=True, TPosition="center", BColor=self.CGC.FColors5, EmptySpace=(0, 0))],
            [self.GC.GColumn(winColumnLayout_List=self.ScreenRecordTabPart, xStretch=True, yStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))],
        ]


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GC.GTabGroup(TabGroupLayout=[
                [self.GC.GTab(Text="Settings", TabLayout=self.SettingsTab, SetValue="tab1")],
                [self.GC.GTab(Text="Screen Stream", TabLayout=self.ScreenRecordPartsTab, SetValue="tab2")],
                [self.GC.GTab(Text="Screen Record", TabLayout=self.ScreenRecordTab, SetValue="tab3")],
            ], SetValue="tabG")],
            [self.GC.GText(SetText=" Second Version Base on 'Gpu-Screen-Recorder' GUI", xStretch=True, TFont="Sans, 15", BColor=self.CGC.FColors0, EmptySpace=(0, 0))]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)



        # Call Function Here
        self.GC.GListBoxBorderSize(WindowValue="videos", Border=0)

        # Timer for Record and Livestream
        self.StartRecordORStream = False
        self.VideoPath = ""
        self.IsProgramRunning = False

        # update window element
        self.GC.GetWindow["rtmp"].update("rtmp://a.rtmp.youtube.com/live2")
        self.GC.GetWindow["mID"].update(self.DesktopID)

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def StartScreenRecord(self, Command: str):
        os.system(Command)
        os.popen("notify-send -t 7500 'Record Starting Now!!' ")
        os.popen("gpu-screen-recorder && notify-send -t 7500 -u low \"Screen Recording Is Starting Now!\"")

    def StartLiveStream(self, Command: str):
        os.system(Command)
        os.popen("notify-send -t 7500 'Live Stream Starting Now!!'")
        os.popen("gpu-screen-recorder && notify-send -t 7500 -u low \"LiveStream Is Starting Now!\"")

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects

        # Settings
        if self.GC.GetEvent in ("14", "24", "30", "60", "120"):
            self.Fps = f"-f {self.GC.GetEvent}"
            self.GC.GetWindow["fps_log"].update(self.Fps)

        elif self.GC.GetEvent in ("Medium", "High", "Very_High", "Ultra"):
            self.VideoQuality = f"-q {str(self.GC.GetEvent).lower()}"
            self.GC.GetWindow["video_log"].update(self.VideoQuality)

        elif self.GC.GetEvent in ("128", "192", "256", "320"):
            self.SoundQuality = f"-ab {self.GC.GetEvent}"
            self.GC.GetWindow["sound_log"].update(self.SoundQuality)

        elif self.GC.GetEvent == "md":
            if not self.DisableMicrophone:
                self.DisableMicrophone = True
                self.GC.GetWindow["md"].update("Enable Microphone")
                print(f"Microphone is Disable -> Self.DisableMicrophone={self.DisableMicrophone}")
            else:
                self.DisableMicrophone = False
                self.GC.GetWindow["md"].update("Disable Microphone")
                print(f"Microphone is Enable  -> Self.DisableMicrophone={self.DisableMicrophone}")
        
        # Screen Record
        elif self.GC.GetEvent == "Video Name Save":
            if len(self.GC.GetValues["vname"]) > 0:
                self.VideoName = self.GC.GetValues["vname"]
                if len(self.VideoPath) > 0:
                    self.GC.GetWindow["path"].update(f"{self.VideoPath}/{self.VideoName}")
                else:
                    self.GC.GetWindow["path"].update(f"missing path/{self.VideoName}")

        elif self.GC.GetEvent == "Select Video Directory":
            self.VideoPath = self.GC.GetFolderPath(defaultPATH=os.path.expanduser("~"))
            if len(self.VideoPath) > 0:
                self.VideoName = self.GC.GetValues["vname"]
                if len(self.VideoName) > 0:
                    self.GC.GetWindow["path"].update(f"{self.VideoPath}/{self.VideoName}")
                else:
                    self.GC.GetWindow["path"].update(f"{self.VideoPath}/missing video name")
            
            if len(self.VideoPath) > 0:
                if os.path.exists(self.VideoPath):
                    _listfiles = os.listdir(self.VideoPath)
                    _videosList = []
                    for i in _listfiles:
                        if str(i).endswith(".mp4") or str(i).endswith(".mkv"):
                            _videosList.append(i)
                    _videosList.sort()
                    self.GC.GetWindow["videos"].update(_videosList)
        
        elif self.GC.GetEvent == "Refresh Video List":
            if os.path.exists(self.VideoPath):
                _listfiles = os.listdir(self.VideoPath)
                _videosList = []
                for i in _listfiles:
                    if str(i).endswith(".mp4") or str(i).endswith(".mkv"):
                        _videosList.append(i)
                _videosList.sort()
                self.GC.GetWindow["videos"].update(_videosList)

        elif self.GC.GetEvent == "Remove Video":
            try:
                if os.path.exists(f"{self.VideoPath}/{self.GC.GetValues["videos"][0]}"):
                    if len(self.VideoPath) > 0:
                        os.remove(f"{self.VideoPath}/{self.GC.GetValues["videos"][0]}")
                        time.sleep(1) # time sleep for wait if video path exit refresh video list
                        _listfiles = os.listdir(self.VideoPath)
                        _videosList = []
                        for i in _listfiles:
                            if str(i).endswith(".mp4") or str(i).endswith(".mkv"):
                                _videosList.append(i)
                            _videosList.sort()
                        self.GC.GetWindow["videos"].update(_videosList)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Start Record":
            if not self.StartRecordORStream:
                if len(self.VideoPath) > 0 and len(self.VideoName) > 0:
                    if len(self.DesktopID) > 0 and len(self.MonutorID) > 0:
                        _now = datetime.now()
                        _Time = f"{_now.year}-{_now.month}-{_now.day}_{_now.hour}-{_now.minute}-{_now.second}"
                        _VideoPath = f"-o {self.VideoPath}/{str(self.VideoName).replace(" ", "\\ ")}-{_Time}.mkv"
                        _deskMic = f"-a {self.MicrophoneName}{self.MonutorID} "
                        _DesktopID = f"-w {self.GC.GetValues["mID"]}"

                        if self.DisableMicrophone:
                            _FullCommand = f"{self.GSR} {_DesktopID} {self.Codecs} -a $(pactl get-default-sink).monitor {self.Fps} {self.VideoQuality} {self.SoundQuality} {_VideoPath}"
                            Thread(target=self.StartScreenRecord, args=[_FullCommand]).start()
                            print(self.DisableMicrophone)
                        else:
                            _FullCommand = f"{self.GSR} {_DesktopID} {self.Codecs} {_deskMic} {self.Fps} {self.VideoQuality} {self.SoundQuality} {_VideoPath}"
                            Thread(target=self.StartScreenRecord, args=[_FullCommand]).start()
                            print(self.DisableMicrophone)

                        self.GC.GetWindow["video_name"].update(self.VideoName)
                        print(_FullCommand)                        

        elif self.GC.GetEvent == "Stop Record":
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 7500 -u low \"Work Is Finish!\"")
            self.GC.GetWindow["video_name"].update("Video Is Finish")
            self.StartRecordORStream = False

        # LiveStream
        elif self.GC.GetEvent == "Start Live Stream":
            if not self.StartRecordORStream:
                if len(self.Rtmp) > 0 and len(self.Key) > 0:
                    _deskMic = f"-a {self.MicrophoneName}{self.MonutorID} "
                    _DesktopID = f"-w {self.GC.GetValues["mID"]}"
                    _FullCommand = f"{self.GSR} {_DesktopID} {self.Codecs} {_deskMic} {self.Fps} {self.VideoQuality} {self.SoundQuality} {self.StreamKey}"
                    Thread(target=self.StartLiveStream, args=[_FullCommand]).start()
                    print(_FullCommand)

        elif self.GC.GetEvent == "Save Stream Key":
            self.Rtmp = self.GC.GetValues["rtmp"]
            self.Key = self.GC.GetValues["skey"]
            if len(self.Rtmp) > 0 and len(self.Key) > 0:
                self.StreamKey = f"-o {self.Rtmp}/{self.Key}"
            self.GC.GetWindow["ready"].update("Stream Ready To Start")

        elif self.GC.GetEvent == "Stop Live Stream":
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 7500 -u low \"LiveStream Is Finish!\"")
            self.StartRecordORStream = False

    def BeforeExit(self):
        os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 7500 -u low \"Record or LiveStream Is Finish!\"")

if __name__ == "__main__":
    SimpleRecordAndLivestream()
