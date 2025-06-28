"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard, GMessage
import json, subprocess


# Extra Lib

class WineContainer:
    def __init__(self):
        self.WinePrefix = {}              # for prefix settings
        self.WinePrefixPathList = []      # for listbox
    
    def CreateWinePrefix(self, Path: str, PrefixName):
        self.WinePrefix[PrefixName] = {
            "Exe": "",
            "Path": Path,
            "prefixName": PrefixName,
            "Winetricks": []
        }
        
        if Path not in self.WinePrefixPathList:
            self.WinePrefixPathList.append(Path)

    def RemoveWinePrefix(self, Path: str):
        PrefixNameSplit = Path.split("/")
        PrefixName = PrefixNameSplit[-1]

        self.WinePrefixPathList.remove(Path)
        del self.WinePrefix[PrefixName]

    def WinePrefixInfo(self):
        return f"""
            WinePrefix Name: {self.WinePrefix["prefixName"]}
            WinePrefix Path: {self.WinePrefix["Path"]}
            Game .EXE Name:  {self.WinePrefix["Exe"]}
            WineTricks All Install Packages: {self.WinePrefix["Winetricks"]}
        """

# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()


class SimeWineAndLegandaryContainer:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title = " UwU ", Size = (1024, 655), resizable = True, finalize = True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        # Extra Value
        self.PlaceHolderPrefixPath: str = ""
        self.Gamemode: bool = True 
        self.MangoHUD: bool = True
        self.ThisWinePrefixContainers  = WineContainer()
        self.LEPath = ""

        self.CachyOSProton = ""
        self.DefaultWine   = ""



        self.HomePath = os.path.expanduser("~")
        if not os.path.exists(f"{self.HomePath}/.config/gnuchanGL"):
            os.mkdir(f"{self.HomePath}/.config/gnuchanGL")
        
        if not os.path.exists(f"{self.HomePath}/.config/gnuchanGL/settings.gc"):
            with open(f"{self.HomePath}/.config/gnuchanGL/settings.gc", "w") as file:
                json.dump(self.ThisWinePrefixContainers.WinePrefix, file)
        else:
            with open(f"{self.HomePath}/.config/gnuchanGL/settings.gc", "r") as file:
                self.ThisWinePrefixContainers.WinePrefix = json.load(file)
                for key in self.ThisWinePrefixContainers.WinePrefix:
                    path = self.ThisWinePrefixContainers.WinePrefix[key]["Path"]
                    self.ThisWinePrefixContainers.WinePrefixPathList.append(path)


        # Extra Value


        # Create
        self.CreateWineButtons = [
            [
                self.GC.GPush(BColor=self.C.purple8),

                self.GC.GText(SetText="WinePrefix Name: ", BColor=self.C.purple8),
                self.GC.GInput(SetValue="prefixName", xStretch=True),
                self.GC.GButton(Text="Select Dir Path", SetValue="sdpWine"),
                self.GC.GButton(Text="Create WinePrefix", SetValue="cWine"),

                self.GC.GPush(BColor=self.C.purple8)
            ]
        ]

        self.WinePrefix = [
            [self.GC.GText(SetText="Wine Prefix dir Path", BColor=self.C.purple6, xStretch=True, TPosition='c', EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="wlist0", xStretch=True, yStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0), LFont="Sans, 25", LPosition='c')],
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="Remove WinePrefix", SetValue="rWine"),
                self.GC.GPush(BColor=self.C.purple8),
            ],
        ]

        self.Winetricks = [
            [self.GC.GText(SetText="WineTricks All List", BColor=self.C.purple6, xStretch=True, TPosition='c', EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="winetricks", xStretch=True, yStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0), LFont="Sans, 25", LPosition='c')],
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="Install"),
                self.GC.GPush(BColor=self.C.purple8),
            ],
        ]

        self.Winetricks_Installed = [
            [self.GC.GText(SetText="WineTricks Install List", BColor=self.C.purple6, xStretch=True, TPosition='c', EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="winetricksInstalled", xStretch=True, yStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0), LFont="Sans, 25", LPosition='c')],
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="Refresh"),
                self.GC.GPush(BColor=self.C.purple8),
            ],
        ]


        self.CreateWine = [
            [self.GC.GFrame(InsideWindowLayout=self.CreateWineButtons, xStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="   ")],
            [
                self.GC.GText(SetText="   "),
                self.GC.GFrame(InsideWindowLayout=self.WinePrefix, xStretch=True, yStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0)),
                self.GC.GText(SetText="   "),
                self.GC.GFrame(InsideWindowLayout=self.Winetricks, xStretch=True, yStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0)),
                self.GC.GText(SetText="   "),
                self.GC.GFrame(InsideWindowLayout=self.Winetricks_Installed, xStretch=True, yStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0)),
                self.GC.GText(SetText="   "),
            ],
            [self.GC.GText(SetText="   ")],

        ]

        # Run
        self.RunWineButtons = [
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="Run .EXE", SetValue="rexe"),
                self.GC.GCheackBox(CText="Gamemode", SetValue="gamemode", BColor=self.C.purple8, Checked=True),
                self.GC.GCheackBox(CText="MangoHUD", SetValue="mangohud", BColor=self.C.purple8, Checked=True),
                self.GC.GPush(BColor=self.C.purple8)
            ]
        ]

        self.RunWineGames = [
            [self.GC.GFrame(InsideWindowLayout=self.RunWineButtons, xStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="   ")],
            [
                self.GC.GText(SetText="   "),
                self.GC.GListBox(SetValue="wlist1", xStretch=True, yStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0)),
                self.GC.GText(SetText="   "),
            ],
            [self.GC.GText(SetText="   ")],
        ]

        # Epic Games Install Process
        """
                legendary auth -> open new terminal and enter command wait login
                legendary list-games
                legendary install GameName --install-dir /mnt/games/fortnite ve legendary uninstall
                legendary list-installed
                legendary launch <oyun_adı> --wrapper "/path/to/proton" --no-wine
                legendary uninstall



                WINEPREFIX="{/SSD/www}" 
                legendary launch 
                '4656facc740742a39e265b026e13d075' 
                --wrapper 
                "/usr/share/steam/compatibilitytools.d/proton-cachyos/files/bin/wine" or /usr/bin/wine
                --no-wine


        """


        self.LegendaryRunButton = [
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="Login Epic Games Account", SetValue="login"),
                self.GC.GButton(Text="Play Game", SetValue="pgame"),
                self.GC.GButton(Text="Remove Game", SetValue="rgame"),
                self.GC.GButton(Text="Refresh Game List", SetValue="refgame"),
                self.GC.GCheackBox(CText="Gamemode", SetValue="lgamemode", BColor=self.C.purple8, Checked=True),
                self.GC.GCheackBox(CText="MangoHUD", SetValue="lmangohud", BColor=self.C.purple8, Checked=True),
                self.GC.GPush(BColor=self.C.purple8)
            ],
        ]

        self.LEInstallButtons = [
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="Select Dir", SetValue="ldpath"),
                self.GC.GButton(Text="Install Game", SetValue="linstall"),
                self.GC.GPush(BColor=self.C.purple8),
            ]
        ]

        self.LegendaryRun = [
            [self.GC.GFrame(InsideWindowLayout=self.LegendaryRunButton, xStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0))],
            [self.GC.GText(SetText="Installed All Epic Games", xStretch=True, BColor=self.C.purple7)],
            [self.GC.GListBox(SetValue="InstalledGames", xStretch=True, yStretch=True)],
            [self.GC.GText(SetText="All Epic Games", xStretch=True, BColor=self.C.purple7)],
            [self.GC.GListBox(SetValue="AllGames", xStretch=True, yStretch=True)],
            [self.GC.GFrame(InsideWindowLayout=self.LEInstallButtons, xStretch=True, Border=0, BColor=self.C.purple8, EmptySpace=(0, 0))],
        ]


        # help

        self.HelpLine = [
            [self.GC.GMultiline(SetValue="help", xStretch=True, yStretch=True, BColor=self.C.purple8, TFont="Sans. 25", ReadOnly=True)]
        ]



        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GC.GTabGroup(TabGroupLayout=[
                [self.GC.GTab(Text="Create WinePrefix HERE!", TabLayout=self.CreateWine, SetValue="cWineTab")],
                [self.GC.GTab(Text="Run Games HERE!", TabLayout=self.RunWineGames, SetValue="rWineTab")],
                [self.GC.GTab(Text="Legendary/Epic Games", TabLayout=self.LegendaryRun, SetValue="lgames")],
                [self.GC.GTab(Text="Help!", TabLayout=self.HelpLine, SetValue="help")],
            ], SetValue="tabG")]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)


        # Call Function Here

        self.ALLGListbox = ( "wlist0", "wlist1", "winetricks", "winetricksInstalled" )

        for i in self.ALLGListbox:
            self.GC.GListBoxBorderSize(WindowValue=i, Border=0)

        # load json
        self.GC.GetWindow["wlist0"].update(self.ThisWinePrefixContainers.WinePrefixPathList)
        self.GC.GetWindow["wlist1"].update(self.ThisWinePrefixContainers.WinePrefixPathList)

        self.allWineTrickPackages =  (
            "d3dx9", "directx9", "d3dx10", "d3dx11", "dxvk", "vkd3d", "cnc_ddraw",
            "vcrun6", "vcrun6sp6", "vcrun2008", "vcrun2010", "vcrun2015", "vcrun2019",
            "dotnet20", "dotnet40", "dotnet45", "dotnet48",
            "faudio", "icodecs", "quicktime72", "quicktime76",
            "wmp9", "wmp10", "msxml3", "mfc42", "wsh57", "devenum",
            "corefonts", "cjkfonts", "physx", "dxdiag", "dxdiagn"
        )
        self.GC.GetWindow["winetricks"].update(self.allWineTrickPackages)

        # Legendary Games
        

        self.LegendaryGamesInstalled = []
        self.LegendaryAllGames = []

        Thread(target=self.updateLEGListbox_Installed, args=[]).start()
        Thread(target=self.UpdateLEGlistbox_AllGames, args=[]).start()

        self.GC.GListBoxBorderSize(WindowValue="InstalledGames", Border=0)
        self.GC.GListBoxBorderSize(WindowValue="AllGames", Border=0)

        # Call Function Here















        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def UpdateLEGlistbox_AllGames(self):
        output = subprocess.check_output(["legendary", "list-games", "--json"], text=True)
        all_games = json.loads(output)

        for game in all_games:
            self.LegendaryAllGames.append(f"{game['app_title']}  -  {game['app_name']}")

        self.GC.GetWindow["AllGames"].update(self.LegendaryAllGames)

    def updateLEGListbox_Installed(self):
        self.LegendaryGamesInstalled = []
        output = subprocess.check_output(["legendary", "list-installed", "--json"], text=True)
        print(output, "\n\n")
        installed_games = json.loads(output)

        for game in installed_games:
            _game = f"{game['install_path']}  -  {game['app_name']}"
            if _game not in self.LegendaryGamesInstalled:
                self.LegendaryGamesInstalled.append(_game)

        self.GC.GetWindow["InstalledGames"].update(self.LegendaryGamesInstalled)

    def CreateWinePrefix(self, _prefixPath: str):
        os.popen(f"WINEPREFIX={_prefixPath} winecfg")

    def RemoveWinePrefix(self, _prefixPath: str):
        os.popen(f"rm -r {_prefixPath}")
    
    def RunExe(self, _prefixPath: str, GamePath: str):
        _gamemode = ""
        _mangohud = ""

        if self.GC.GetValues["gamemode"]: 
            _gamemode = "gamemoderun"
        if self.GC.GetValues["mangohud"]: 
            _mangohud = "mangohud --dlsym"

        cmd = f"{_gamemode} {_mangohud} WINEPREFIX='{_prefixPath}' wine '{GamePath}'"
        os.system(cmd)

    def WineTricksInstallPack(self, PrefixPath: str, PackName: str):
        cmd = f"WINEPREFIX='{PrefixPath}' winetricks '{PackName}'"
        os.system(cmd)
        self.GC.GetWindow["InstalledGames"].update(self.LegendaryGamesInstalled)
        print(cmd)
    
    def LEInstallGames(self, cmd: str):
        os.system(cmd)
        self.updateLEGListbox_Installed()
    
    def LERemoveGames(self, cmd: str):
        os.system(cmd)
        self.updateLEGListbox_Installed()

    def LERunGames(self, cmd: str):
        os.system(cmd)

    def Update(self):
        #if self.KYB.Return == self.GC.GetEvent -> Press key
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects


        if "sdpWine" == self.GC.GetEvent:
            try:
                self.PlaceHolderPrefixPath = self.GC.GetFolderPath()

            except Exception as ERR:
                GMessage(WindowTitle="Path Err", WindowText=ERR)

        elif "cWine" == self.GC.GetEvent:
            try:
                if len(self.GC.GetValues["prefixName"]) > 0:
                    PrefixName = self.GC.GetValues["prefixName"]
                    _prefixPath = os.path.join(self.PlaceHolderPrefixPath, PrefixName)
                    self.ThisWinePrefixContainers.CreateWinePrefix(Path=_prefixPath, PrefixName=PrefixName)

                    self.GC.GetWindow["wlist0"].update(self.ThisWinePrefixContainers.WinePrefixPathList)
                    self.GC.GetWindow["wlist1"].update(self.ThisWinePrefixContainers.WinePrefixPathList)

                    if not os.path.exists(_prefixPath):
                        Thread(target=self.CreateWinePrefix, args=[_prefixPath]).start()

            except Exception as ERR:
                GMessage(WindowTitle="Path Err", WindowText=ERR)

        elif "rWine" == self.GC.GetEvent:
            try:
                Path = str(self.GC.GetValues["wlist0"]).strip("['']")
                self.ThisWinePrefixContainers.RemoveWinePrefix(Path=Path)

                self.GC.GetWindow["wlist0"].update(self.ThisWinePrefixContainers.WinePrefixPathList)
                self.GC.GetWindow["wlist1"].update(self.ThisWinePrefixContainers.WinePrefixPathList)

                if os.path.exists(Path):
                    Thread(target=self.RemoveWinePrefix, args=[Path]).start()

            except Exception as ERR:
                GMessage(WindowTitle="Path Err", WindowText=ERR)

        elif "rexe" == self.GC.GetEvent:
            try:
                Path = str(self.GC.GetValues["wlist1"]).strip("['']")
                exePath = self.GC.GetFilePath(defaultPATH=Path)

                if os.path.exists(exePath):
                    Thread(target=self.RunExe, args=[Path, exePath]).start()

            except Exception as ERR:
                GMessage(WindowTitle="Path Err", WindowText="Select Game File?")

        elif "Refresh" == self.GC.GetEvent:
            try:
                Path = str(self.GC.GetValues["wlist0"]).strip("['']")
                _prefixName = Path.split("/")
                _AllInstalledList = self.ThisWinePrefixContainers.WinePrefix[_prefixName[-1]]["Winetricks"]
                self.GC.GetWindow["winetricksInstalled"].update(_AllInstalledList)
            
            except Exception as ERR:
                GMessage(WindowTitle="Path Err", WindowText=ERR)
        
        elif "Install" == self.GC.GetEvent:
            try:
                Path = str(self.GC.GetValues["wlist0"]).strip("['']")
                SelectPackage = str(self.GC.GetValues["winetricks"]).strip("['']")
                if len(Path) > 0 and len(SelectPackage) > 0:
                    _prefixName = Path.split("/")

                    # winetricksInstalled
                    if SelectPackage not in self.ThisWinePrefixContainers.WinePrefix[_prefixName[-1]]["Winetricks"]:
                        self.ThisWinePrefixContainers.WinePrefix[_prefixName[-1]]["Winetricks"].append(SelectPackage)
                        self.GC.GetWindow["winetricksInstalled"].update(self.ThisWinePrefixContainers.WinePrefix[_prefixName[-1]]["Winetricks"])

                        Thread(target=self.WineTricksInstallPack, args=[Path, SelectPackage]).start()
            except Exception as ERR:
                GMessage(WindowTitle="Path Err", WindowText=ERR)

        elif "login" == self.GC.GetEvent:
            subprocess.Popen( ['xterm', '-e', 'bash', '-c', 'legendary auth; exec bash'] )

        elif "pgame" == self.GC.GetEvent:
            getstr = str(self.GC.GetValues["InstalledGames"]).strip("['']")

            if len(self.GC.GetValues["InstalledGames"]) > 0:
                id     = getstr.split("  -  ")

                _GameID = ""
                _GamePath = ""

                try:
                    _GameID    = id[1]
                    _GamePath  = id[0]
                except Exception as ERR:
                    GMessage(WindowTitle="Warning", WindowText="What Game???")
                
                self.CurrentWine = ""
                if os.path.exists("/usr/share/steam/compatibilitytools.d/proton-cachyos/files/bin/wine"):
                    self.CurrentWine = "/usr/share/steam/compatibilitytools.d/proton-cachyos/files/bin/wine"
                elif os.path.exists("/usr/bin/wine"):
                    self.CurrentWine = "/usr/bin/wine"

                _GameMode = ""
                _Mangohud = ""
                    
                if self.GC.GetValues["lgamemode"]: 
                    _GameMode = "gamemoderun"
                if self.GC.GetValues["lmangohud"]: 
                    _Mangohud = "mangohud --dlsym"
                    
                self.Gamemode = self.GC.GetValues["gamemode"]

                if len(_GameID) > 0:
                    EpicGamesRun = f"{_GameMode} {_Mangohud} WINEPREFIX='{_GamePath}' legendary launch '{_GameID}' {self.CurrentWine} --no-wine"
                    Thread(target=self.LERunGames, args=[EpicGamesRun]).start()
                else:
                    GMessage(WindowTitle="Warning", WindowText="Path Is Not Real Dir Path")

            """
                WINEPREFIX="{/SSD/www}" 
                legendary launch 
                '4656facc740742a39e265b026e13d075' -> Game ID
                --wrapper 
                "/usr/share/steam/compatibilitytools.d/proton-cachyos/files/bin/wine" or /usr/bin/wine
                --no-wine
            """

        elif "ldpath" == self.GC.GetEvent:
            self.LEPath = self.GC.GetFolderPath()

        elif "linstall" == self.GC.GetEvent:
            if len(self.GC.GetValues["AllGames"]) > 0:
                _IDPath = str(self.GC.GetValues["AllGames"]).strip("['']")
                id      = _IDPath.split("  -  ")
                leGAMES = ""

                if len(self.LEPath) > 0:
                    if os.path.exists(self.LEPath):
                        leGAMES = f"legendary install '{id[1]}' --base-path '{self.LEPath}' -y".strip('\"')
                        Thread(target=self.LEInstallGames, args=[leGAMES]).start()
                        os.system(f"WINEPREFIX='{self.LEPath}' ")
                        print(leGAMES, "\n\n")
                    else:
                        GMessage(WindowTitle="Warning", WindowText="Install Dir '404'")
                else:
                    GMessage(WindowTitle="Warning", WindowText="First Select Install Dir")

            """
            legendary install {GameName} --install-dir {/mnt/games/fortnite}
            """
        elif "rgame" == self.GC.GetEvent:
            getstr = str(self.GC.GetValues["InstalledGames"]).strip("['']")

            if len(self.GC.GetValues["InstalledGames"]) > 0:
                id = getstr.split("  -  ")
                RemoveLEGame = f"legendary uninstall '{id[1]}' -y"
                os.system(f"rm -r {id[0]}")
                
                Thread(target=self.LERemoveGames, args=[RemoveLEGame]).start()

        elif "refgame" == self.GC.GetEvent:
            self.updateLEGListbox_Installed()


    def BeforeExit(self):
        with open(f"{self.HomePath}/.config/gnuchanGL/settings.gc", "w") as file:
            json.dump(self.ThisWinePrefixContainers.WinePrefix, file)

        print("Exit")

if __name__ == "__main__":
    gc = SimeWineAndLegandaryContainer()





