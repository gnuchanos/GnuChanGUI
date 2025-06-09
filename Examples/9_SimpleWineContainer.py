"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard, GMessage, GCanvas, GVector2


# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()


class SimpleWineContainer:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        self.WineMainTab_Buttons = [
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GInput(SetValue="wi"),
                self.GC.GButton(Text="Create WinePrefix"),
                self.GC.GButton(Text="Remove WinePrefix"),
                self.GC.GPush(BColor=self.C.purple8)
            ]
        ]
        self.WineMainTab = [
            [self.GC.GFrame(InsideWindowLayout=self.WineMainTab_Buttons, xStretch=True, Border=0, BColor=self.C.purple8)],
            [self.GC.GText(SetText="All WinePrefix Here", TPosition='c', xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="wine0", xStretch=True, yStretch=True, EmptySpace=(0, 0), BColor=self.C.purple6)],
        ]

        # Create buttons / add winetriks package / install winetricks packages
        # Create 2 glistbox first all winetrick we need second is what we need install like select left list add right

        self.Winetricks_Buttons = [
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GInput(SetValue="wipack"),
                self.GC.GButton(Text="Add Winetrick Package", SetValue="addPack"),
                self.GC.GButton(Text="Install With Input", SetValue="InputInstall"),
                self.GC.GPush(BColor=self.C.purple8)
            ]
        ]


        self.LeftWinetricks = [
            [self.GC.GText(SetText="All WineTricks Package You Need", TPosition='c', xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="winetrikslist", xStretch=True, yStretch=True, EmptySpace=(0, 0), BColor=self.C.purple6)],
        ]

        self.RightWineTricks = [
            [self.GC.GText(SetText="You Ready To Install Now!", TPosition='c', xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="winetrikslist_install", xStretch=True, yStretch=True, EmptySpace=(0, 0), BColor=self.C.purple6)]
        ]

        self.WineSettingsTab = [
            [self.GC.GFrame(InsideWindowLayout=self.Winetricks_Buttons, xStretch=True, Border=0, BColor=self.C.purple8)],
            [
                self.GC.GVSep(Color=self.C.purple1),
                self.GC.GFrame(InsideWindowLayout=self.LeftWinetricks, xStretch=True, yStretch=True, Border=0),
                self.GC.GVSep(Color=self.C.purple1),
                self.GC.GFrame(InsideWindowLayout=self.RightWineTricks, xStretch=True, yStretch=True, Border=0),
                self.GC.GVSep(Color=self.C.purple1),
            ],
            [self.GC.GText(SetText="WinePrefix List", TPosition='c', xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="wine1", xStretch=True, yStretch=True, EmptySpace=(0, 0), BColor=self.C.purple6)],
            [self.GC.GButton(Text="Install Selected Winetrick Packages", SetValue="install")]

        ]


        self.WineGameRunButtons = [
            [
                self.GC.GPush(BColor=self.C.purple8),
                self.GC.GButton(Text="WineCFG", SetValue="winecfg"),
                self.GC.GButton(Text="Run .EXE", SetValue="runexe"),
                self.GC.GButton(Text="Run Game", SetValue="run"),
                self.GC.GPush(BColor=self.C.purple8)
            ]
        ]


        self.WineGameRunTab = [
            [self.GC.GFrame(InsideWindowLayout=self.WineGameRunButtons, xStretch=True, BColor=self.C.purple8, Border=0)],
            [self.GC.GText(SetText="Run Game or Installer.exe", TPosition='c', xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))],
            [self.GC.GListBox(SetValue="wine2", xStretch=True, yStretch=True, BColor=self.C.purple6, EmptySpace=(0, 0))]


        ]


        # main window layout you can use column and frame in here
        self.Layout = [

           [self.GC.GTabGroup(
                TabGroupLayout=[
                    [self.GC.GTab(Text="Wine Main Tab", TabLayout=self.WineMainTab)],
                    [self.GC.GTab(Text="Winetriks Install Tab", TabLayout=self.WineSettingsTab)],
                    [self.GC.GTab(Text="Wine Run", TabLayout=self.WineGameRunTab)]
                ],
                SetValue="WineTabs"
            )],
           [self.GC.GText(xStretch=True, BColor=self.C.purple7, EmptySpace=(0, 0))]

        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        # Call Function Here

        self.GlistBoxWindowValue = ( "wine0", "wine1", "wine2", "winetrikslist", "winetrikslist_install" )
        for i in self.GlistBoxWindowValue:
            self.GC.GListBoxBorderSize(WindowValue=i, Border=0)

        self.AllWineTrickPackages = (
            "d3dx9", "directx9", "d3dx10", "d3dx11", "dxvk", "vkd3d", "cnc_ddraw", 
            "vcrun6", "vcrun6sp6", "vcrun2008", "vcrun2010", "vcrun2015", "vcrun2019", 
            "dotnet20", "dotnet40", "dotnet45", "dotnet48", 
            "faudio", "icodecs", "quicktime72", "quicktime76", 
            "wmp9", "wmp10", "msxml3", "mfc42", "wsh57", 
            "devenum", "corefonts", "cjkfonts", "physx", "dxdiag", "dxdiagn"
        )

        self.PackageSelection = [
        ]

        # if dir not exist 
            # mkdir ~/.config/wineContainer/
            # touch ~/.config/wineContainer/settings.gc
        # if exist
            # read file

        self.GameSaveFile = {
            0: {
                "name":"hl.exe",
                "path":"/SSD/Game/Half\\ Life",
                "winetricks": []
            }
        }

        self.WinePrefixList = []
        self.WinePrefixList.append(self.GameSaveFile[0]["path"])
        self.GC.GetWindow["wine0"].update(self.WinePrefixList)

        
        # all winetricks packages
        self.GC.GetWindow["winetrikslist"].update(self.AllWineTrickPackages)

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)



    def Update(self):
        #if self.KYB.Return == self.GC.GetEvent -> Press key
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects

        pass

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    SimpleWineContainer()
