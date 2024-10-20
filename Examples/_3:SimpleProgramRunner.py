"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
import subprocess

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Very Simple Program Runner Like Rofi and dmenu", Size=(500, 700), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS


    mySoftwareList = [
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
        "StartBlender",
    ]

    middleThings = [
        [ 
            gc.GText(SetText="> ", BColor=GnuChanOSColor().colors0, EmptySpace=(0, 0)), 
            gc.GInput(WindowValue="input",  xStretch=True, BColor=GnuChanOSColor().colors0, EmptySpace=(0, 0)) 
        ],
        [
            gc.GPush(GnuChanOSColor().colors1),
            gc.GButton(Text="Run Program", TFont="Sans, 20"),
            gc.GPush(GnuChanOSColor().colors1),
        ],
        [ gc.GHSep(Color=GnuChanOSColor().colors3) ],
        [ gc.GListBox(WindowValue="software", LFont="Sans, 14", LPosition="center", xStretch=True, yStretch=True, noScroolBar=True) ],
        [ gc.GHSep(Color=GnuChanOSColor().colors3) ],
    ]

    layout = [ 
        [ gc.GText(xStretch=True) ],
        [ gc.GColumn(winColumnLayout_List=middleThings, xStretch=True, yStretch=True)],
        [ gc.GText(SetText="", TFont="Sans, 20", xStretch=True) ]
    ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    gc.GListBoxBorderSize(WindowValue="software", Border=0)
    keyboard = GKeyboard(window=gc.GetWindow)

    drawFinish = False
    SoftwareListActive = []

    # Control Program if install
    _ReadyPrograms = []
    _SoftwareList = os.listdir("/usr/bin")
    for i in _SoftwareList:
        if i in mySoftwareList:
            if not i in _ReadyPrograms:
                _ReadyPrograms.append(i)
    _ReadyPrograms.sort()
    gc.GetWindow["software"].update(_ReadyPrograms)
    

    def RunThis(commandInput):
        try:
            subprocess.run([commandInput], check=True, shell=True)
        except subprocess.CalledProcessError as e:
            os.system("clear")
            print(f"there is no like this program -> {gc.GetValues["input"]}")

    def update():
        global mySoftwareList, drawFinish, drawTime
        _Input = str(gc.GetValues["input"]).strip("")

        # Run Program In Line
        if gc.GetEvent == "Return:36":
            _commandInput = str(gc.GetValues["input"])
            if len(_commandInput) > 0:
                Thread(target=RunThis, args=[_commandInput]).start()
            gc.closeWindow = True

        # Run Program In List
        elif gc.GetEvent == "Run Program":
            _Select = str(gc.GetValues["software"]).strip("[]''")
            if _Select != "":
                Thread(target=RunThis, args=[_Select]).start()
                gc.closeWindow = True

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)


