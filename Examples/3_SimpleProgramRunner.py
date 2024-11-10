"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard


# Extra Lib


#Thread(target=DownloadVideo, args=[]).start()
class SimpleProgramRunner:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        
        self.mySoftwareList = [
            # for conten creators
            "kdenlive", "audacity", "shortcut", "openshot", "resolve", "pitivi",
            "blender", "obs", "simplescreenrecorder",
            # Web Browser
            "qutebrowser", "firefox", "chromium", "google-chrome", "brave: Browser",
            # Text Editors
            "gedit", "kate", "notepadqq", "leafpad",
            # Office Software
            "libreoffice: Office Program", "openoffice: Office Program",
            # Image Edit and Paint Software
            "gimp", "krita", "inkscape", "darktable", "mypaint", "pinta",
            # Video and Audio Players
            "vlc", "mpv", "rhythmbox", "smplayer", "audacious", "banshee", "clementine",
            # System tools
            "gnome-system-monitor", "kde-system-monitor", "bleachbit", "gparted", "timeshift",
            # File Managers
            "nautilus", "dolphin", "thunar", "pcmanfm", "nemo", "doublecmd",
            # Chat APP
            "discord", "vesktop", "telegram-desktop", "skype", "zoom",
            # Clouth APP
            "dropbox", "nextcloud", "megasync", "insync",
            # EMail APP
            "thunderbird", "geary", "evolution", "kmail",
            # Games
            "steam", "lutris", "heroic", "mgba-qt", "PPSSPPSDL", "duckstation-qt", "pcsx2-qt", "melonDS", "snes9x", "nestopia"
            # Sanal Makineler ve Emülatörler
            "virtualbox", "vmware-player", "gnome-boxes", "qemu",

            # Extra List
            "StartBlender", "vcode"
        ]


        self.middleThings = [
            [ 
                self.GC.GText(SetText="> ", BColor=self.CGC.FColors0, EmptySpace=(0, 0)), 
                self.GC.GInput(SetValue="input",  xStretch=True, BColor=self.CGC.FColors0, EmptySpace=(0, 0)) 
            ],
            [self.GC.GHSep(Color=self.CGC.FColors3)],
            [self.GC.GListBox(SetValue="software", LFont="Sans, 14", LPosition="center", xStretch=True, yStretch=True, noScroolBar=True)],
            [self.GC.GHSep(Color=self.CGC.FColors3)],
            [
                self.GC.GPush(self.CGC.BGColor),
                self.GC.GButton(Text="Run Program", TFont="Sans, 20"),
                self.GC.GPush(self.CGC.BGColor),
            ],
            [self.GC.GHSep(Color=self.CGC.FColors3)],
        ]

        self.Layout = [ 
            [self.GC.GColumn(winColumnLayout_List=self.middleThings, xStretch=True, yStretch=True)],
            [self.GC.GText(SetText="The program calls Linux commands, but there is no error message. Please check the Python file for more information.", TFont="Sans, 13", xStretch=True) ]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        # Call Function Here
        self.GC.GListBoxBorderSize(WindowValue="software", Border=0)

        self.SoftwareListActive = []

        # Control Program if install
        self._ReadyPrograms = []
        self._SoftwareList = os.listdir("/usr/bin")
        for i in self._SoftwareList:
            if i in self.mySoftwareList:
                if not i in self._ReadyPrograms:
                    self._ReadyPrograms.append(i)
        self._ReadyPrograms.sort()
        self.GC.GetWindow["software"].update(self._ReadyPrograms)


        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def RunThis(self, Command: str):
        os.system(Command)
        

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        
        # Run Program In Line
        if self.GC.GetEvent == "Return:36":
            _commandInput = str(self.GC.GetValues["input"])
            if len(_commandInput) > 0:
                Thread(target=self.RunThis, args=[_commandInput]).start()
                self.GC.closeWindow = True

        # Run Program In List
        elif self.GC.GetEvent == "Run Program":
            _Select = str(self.GC.GetValues["software"]).strip("[]''")
            if _Select != "":
                Thread(target=self.RunThis, args=[_Select]).start()
                self.GC.closeWindow = True

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    SimpleProgramRunner()
