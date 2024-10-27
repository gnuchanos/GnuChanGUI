"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
from gamelist import gamelist
#Thread(target=DownloadVideo, args=[]).start()


class SimpleWineManager:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # First Create Wine Container
        self.CreateWinePrefix = [
            [self.GC.GHSep(Color=self.CGC.colors5)],
            [   self.GC.GText(SetText="Wine Path Write Wine Dir Name", TPosition="center", xStretch=True, BColor=self.C.purple7)   
            ],
            [   
                self.GC.GText(SetText=f"{os.path.expanduser("~")}/Games/winePrefix/", EmptySpace=(0, 0), BColor=self.C.purple6),
                self.GC.GInput(SetValue="path_wine", xStretch=True, EmptySpace=(0, 0), BColor=self.C.purple6)
            ],
            [
                self.GC.GPush(BColor=self.C.purple7),
                self.GC.GRadio(SetValue="32bit", groupID="wine", RText="32Bit", BColor=self.C.purple7),
                self.GC.GRadio(SetValue="64bit", groupID="wine", RText="64Bit", BColor=self.C.purple7),
                self.GC.GPush(BColor=self.C.purple7)
            ],
            [   
                self.GC.GPush(BColor=self.C.purple7), 
                self.GC.GButton(Text="Create Prefix"), 
                self.GC.GPush(BColor=self.C.purple7)
            ],
            [   
                self.GC.GListBox(SetValue="gamelist_create", xStretch=True, yStretch=True, BColor=self.C.purple8),
            ],
            [   self.GC.GHSep(Color=self.CGC.colors5)   ],
        ]

        # Second Run Games 
        self.wineBody = [
            [self.GC.GHSep(Color=self.CGC.colors5)   ],
            [self.GC.GText(SetText="Select Wine prefix!", xStretch=True, TPosition="center", BColor=self.C.purple7)],
            [self.GC.GText(SetText="Don't use Empty Space'", BColor=self.C.purple5, xStretch=True, TPosition="center")],
            [self.GC.GText(SetText="Choose Youre Wine", xStretch=True, TPosition="center", BColor=self.C.purple7)],
            [   
                self.GC.GPush(BColor=self.C.purple7),
                self.GC.GButton(Text="WineTRICKS"),
                self.GC.GButton(Text="WineCFG"),
                self.GC.GButton(Text="Run .EXE"),
                self.GC.GButton(Text="Update Prefix"),
                self.GC.GButton(Text="Remove Prefix"),
                self.GC.GPush(BColor=self.C.purple7),
            ],
            [   
                self.GC.GListBox(SetValue="gamelist_run", xStretch=True, yStretch=True, BColor=self.C.purple8),
            ],
            [self.GC.GHSep(Color=self.CGC.colors5)],
        ]

        self.wine_Create = [
            [self.GC.GColumn(winColumnLayout_List=self.CreateWinePrefix, xStretch=True, yStretch=True, BColor=self.C.purple7)],
            [self.GC.GText(SetText="", xStretch=True)],
        ]

        self.wine_Run = [ 
            [   self.GC.GColumn(winColumnLayout_List=self.wineBody, xStretch=True, yStretch=True, BColor=self.C.purple7)],
            [   
                self.GC.GPush(self.CGC.colors1),
                    self.GC.GCheackBox(CText="Primusrun",   SetValue="primusrun", TFont="Sans, 15"),
                    self.GC.GRadio(RText="MangoHUD=OpenGL", groupID="mangohud", SetValue="dx", TFont="Sans, 15"),
                    self.GC.GRadio(RText="MangoHUD=Vulkan", groupID="mangohud", SetValue="gl", TFont="Sans, 15"),
                    self.GC.GCheackBox(CText="GameMode",    SetValue="game", TFont="Sans, 15"),
                self.GC.GPush(self.CGC.colors1)
            ]
        ]

        self.wine_debug = [
            [self.GC.GLog(xStretch=True, yStretch=True, BColor=self.CGC.colors0)]
        ]

        self.wine_triks = [
            [self.GC.GMultiline(SetValue="output", TFont="Sans, 12", xStretch=True, yStretch=True, ReadOnly=True, BColor=self.CGC.colors0)],
            [self.GC.GInput(SetValue="input", TFont="Sans, 15", xStretch=True, BColor=self.C.purple8)],
        ]

        # main window layout you can use column and frame in here
        self.Layout = [
            [
                self.GC.GTabGroup(
                    TabGroupLayout=[
                        #[self.GC.GTab(Text="Output", TabLayout=self.wine_debug, SetValue="tab0")],
                        [self.GC.GTab(Text="Help!", TabLayout=self.wine_triks, SetValue="tab1")],
                        [self.GC.GTab(Text="Create Wine", TabLayout=self.wine_Create, SetValue="tab2")],
                        [self.GC.GTab(Text="Run Wine", TabLayout=self.wine_Run, SetValue="tab3")],
                        ], 
                SetValue="tabG")
            ]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        # Call Function Here
        self.GC.GListBoxBorderSize(WindowValue="gamelist_create", Border=1)
        self.GC.GListBoxBorderSize(WindowValue="gamelist_run", Border=1)

        # update gamelist
        self.GC.GetWindow["gamelist_create"].update(gamelist)
        self.GC.GetWindow["gamelist_run"].update(gamelist)


        self.Path = f"{os.path.expanduser("~")}/Games/winePrefix/"
        self._PyFilePath = os.path.dirname(os.path.abspath(__file__))
        self.SelectDir = ""
        self.WineSystemBit = ""

        self.BumbleeTech = "primusrun"
        self.Mangohud  = ""
        self.GameMode  = ""


        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects


        if self.GC.GetEvent in ("32bit", "64bit"):
            if self.GC.GetEvent == "32bit":
                self.WineSystemBit = "win32"
            elif self.GC.GetEvent == "64bit":
                self.WineSystemBit = "win64"

        elif self.GC.GetEvent == "Create Prefix":
            """ WINEPREFIX=~/.wine WINEARCH=win32 wine winecfg | WINEPREFIX=~/.wine64 WINEARCH=win64 wine winecfg """
            if len(self.WineSystemBit) > 0:
                if len(self.GC.GetValues["path_wine"]) > 0:
                    _Wine = "wine winecfg"
                    _WinePath = f"{self.Path}{self.GC.GetValues["path_wine"]}"
                    _WineSystem = f"WINEARCH={self.WineSystemBit}"
                    _WinePrefixReady = f"WINEPREFIX={_WinePath}"
                    _ReadyWine = f"{_WinePrefixReady} {_WineSystem} {_Wine}"
                    print(_ReadyWine)

                    gamelist.append(_WinePath)
                    with open(file=f"{self._PyFilePath}/gamelist.py", mode="w") as file:
                        file.write(f"gamelist = {gamelist}")
                        self.GC.GetWindow["gamelist_create"].update(gamelist)
                        self.GC.GetWindow["gamelist_run"].update(gamelist)

        elif self.GC.GetEvent == "WineTRICKS":
            try:
                _SelectPath = str(self.GC.GetValues["gamelist_run"]).strip("[]")
                if len(_SelectPath) > 0:
                    _RunEXE = f"WINEPREFIX={_SelectPath} winetricks'"
                    print(_RunEXE)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "WineCFG":
            try:
                _SelectPath = str(self.GC.GetValues["gamelist_run"]).strip("[]")
                if len(_SelectPath) > 0:
                    _RunEXE = f"WINEPREFIX={_SelectPath} winecfg'"
                    print(_RunEXE)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Run .EXE":
            _primusrun = ""

            if self.GC.GetEvent in ("dx", "gl"):
                if self.GC.GetEvent == "dx":
                    self.Mangohud = "MANGOHUD=1"
                if self.GC.GetEvent == "gl":
                    self.Mangohud = "mangohud --dlsym"
            if self.GC.GetValues["game"]:
                self.GameMode = "gamemoderun"
            if self.GC.GetValues["primusrun"]:
                _primusrun = self.BumbleeTech

            try:
                _SelectPath = str(self.GC.GetValues["gamelist_run"]).strip("[]")
                if len(_SelectPath) > 0:
                    self.SelectEXE = self.GC.GetFilePath(defaultPATH=str(_SelectPath).strip("'"))
                    if len(self.SelectEXE) > 0:
                        # WINEPREFIX=/home/archkubi/.wine/ primusrun gamemoderun mangohud --dlsym wine falloutwHR.exe
                        _RunEXE = f"WINEPREFIX={_SelectPath} {_primusrun} {self.Mangohud} {self.GameMode} '{self.SelectEXE}'"
                        print(_RunEXE)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Update Prefix":
            try:
                _SelectPath = str(self.GC.GetValues["gamelist_run"]).strip("[]")
                if len(_SelectPath) > 0:
                    self.SelectEXE = self.GC.GetFilePath(defaultPATH=str(_SelectPath).strip("'"))
                    if len(self.SelectEXE) > 0:
                        _RunEXE = f"WINEPREFIX={_SelectPath} {_primusrun} {self.Mangohud} {self.GameMode} '{self.SelectEXE}'"
                        print(_RunEXE)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Remove Prefix":
            try:
                _SelectPath = str(self.GC.GetValues["gamelist_run"]).strip("[]")
                if len(_SelectPath) > 0:
                    gamelist.remove(self.GC.GetValues["gamelist_run"][0])
                    with open(file=f"{self._PyFilePath}./gamelist.py", mode="w") as file:
                        file.write(f"gamelist = {gamelist}")
                        self.GC.GetWindow["gamelist_create"].update(gamelist)
                        self.GC.GetWindow["gamelist_run"].update(gamelist)
            except Exception as ERR:
                print(ERR)


    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    SimpleWineManager()
