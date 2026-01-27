"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors


# Extra Lib
#Thread(target=DownloadVideo, args=[]).start()
class SimpleProgramRunner(GnuChanGUI):
    def __init__( self, Title="Followers Control Center", Size=(1600, 900), resizable=True, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2 ):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        
        self.mySoftwareList = [
            # for conten creators
            "kdenlive", "audacity", "shortcut", "openshot", "resolve", "pitivi",
            "blender", "obs", "simplescreenrecorder",
            
            # Web Browser
            "qutebrowser",  "chromium", 

            # Office Software
            "libreoffice",
            
            # Image Edit and Paint Software
            "gimp", "krita", "inkscape", "darktable", "mypaint", "pinta",
            
            # Video and Audio Players
            "vlc", "mpv",
            
            # System tools
            "gparted", "timeshift",
            
            # Games
            "steam", "mgba-qt", "PPSSPPSDL", "duckstation-qt", "pcsx2", "melonDS", "snes9x", "nestopia",
            
            # Sanal Makineler ve Emülatörler
            "gnome-boxes",

            # Extra List
            "code", "deluge", "fdm",
            "nemo",
        ]


        self.middleThings = [
            [ 
                self.GText(SetText="> ", BColor=self.CGC.FColors0, EmptySpace=(0, 0)), 
                self.GInput(SetValue="input",  xStretch=True, BColor=self.CGC.FColors0, EmptySpace=(0, 0)) 
            ],
            [self.GHSep(Color=self.CGC.FColors3)],
            [self.GListBox(SetValue="software", LFont="Sans, 30", LPosition="center", xStretch=True, yStretch=True, noScroolBar=True)],
            [self.GHSep(Color=self.CGC.FColors3)],
        ]

        self.Layout = [ 
            [self.GColumn(winColumnLayout_List=self.middleThings, xStretch=True, yStretch=True)],
            [self.GText(SetText="The program calls Linux commands, but there is no error message. Please check the Python file for more information.", TFont="Sans, 13", xStretch=True) ]
        ]
        

        self.GWindow(SetMainWindowLayout_List=self.Layout)


        # Call Function Here
        self.GBorder(WindowValue="software", Border=0, Color=self.C.black)

        self.SoftwareListActive = []

        # Control Program if install
        self._ReadyPrograms = []
        self._SoftwareList = os.listdir("/usr/bin")
        for i in self._SoftwareList:
            if i in self.mySoftwareList:
                if not i in self._ReadyPrograms:
                    self._ReadyPrograms.append(i)
        self._ReadyPrograms.sort()
        self.GetWindow["software"].update(self._ReadyPrograms)


        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def RunThis(self, Command: str):
        os.system(Command)
        

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        
        # Run Program In Line
        if self.Enter == self.CurrentKey:
            _commandInput = str(self.GetValues["input"])
            _Select = str(self.GetValues["software"]).strip("[]''")

            if len(_commandInput) > 0:
                if "brave" == _commandInput:
                    os.popen("brave --password-store=basic")
                else:
                    Thread(target=self.RunThis, args=[_commandInput]).start()
                self.closeWindow = True

            elif _Select != "":
                Thread(target=self.RunThis, args=[_Select]).start()
                self.closeWindow = True

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleProgramRunner()
