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
        "kdenlive", "audacity", "shotcut", "openshot", "resolve", "pitivi",
        "blender", "obs", "simplescreenrecorder",
        # Web Browser
        "qutebrowser", "firefox", "chromium", "google-chrome", "brave",
        # Text Editors
        "gedit", "kate", "sublime-text", "code", "atom", "notepadqq",     
        # Office Software
        "libreoffice", "evince", "okular", "masterpdfeditor", "gnumeric", "openoffice",
        # Image Edit and Paint Software
        "gimp", "krita", "inkscape", "darktable", "mypaint", "pinta",
        # Video and Audio Players
        "vlc", "mpv", "rhythmbox", "smplayer", "audacious", "banshee", "clementine",
        # System tools
        "gnome-system-monitor", "kde-system-monitor", "bleachbit", "gparted", "timeshift",
        # File Managers
        "nautilus", "dolphin", "thunar", "pcmanfm", "nemo", "doublecmd",
        # Terminal Emulators
        "gnome-terminal", "konsole", "xfce4-terminal", "guake", "cool-retro-term", "alacritty",
        # Package Managers GUI
        "synaptic", "pamac", "gnome-software", "discover", "software-center",
        # Chat APP
        "discord", "vesktop", "telegram-desktop", "skype", "zoom",
        # Clouth APP
        "dropbox", "nextcloud", "megasync", "insync",
        # EMail APP
        "thunderbird", "geary", "evolution", "kmail",
        # Games
        "steam", "lutris", "heroic", "mgba-qt", "PPSSPPSDL", "duckstation-qt", "pcsx2-qt", "melonDS", "snes9x", "nestopia"
        # Sanal Makineler ve Emülatörler
        "virtualbox", "vmware-player", "gnome-boxes", "qemu"
    ]

    middleThings = [
        [ 
            gc.GText(title="> ", bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)), 
            gc.GInput(value="input",  xStretch=True, bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)) 
        ],
        [ gc.hsep ],
        [ gc.GListBox(value="software", font="Sans, 14", position="center", xStretch=True, yStretch=True, noScroolBar=True) ],
        [ gc.hsep ],
    ]

    layout = [ 
        [ gc.GText(xStretch=True) ],
        [ gc.GColumn(winColumn=middleThings, xStretch=True, yStretch=True)],
        [ gc.GText(title="Press left or right shift to refresh list", font="Sans, 20", xStretch=True) ]
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(windowValue="software", border=0)
    #Thread(target=DownloadVideo, args=[]).start()

    keyboard = GKeyboard(window=gc.window)

    drawFinish = False
    SoftwareListActive = []
    drawTime = 1 

    # Control Program if install
    _ReadyPrograms = []
    _SoftwareList = os.listdir("/usr/bin")
    for s in _SoftwareList:
        if s in mySoftwareList:
            if s not in _ReadyPrograms:
                _ReadyPrograms.append(s)
                gc.window["software"].update(_ReadyPrograms)

    def RunThis(commandInput):
        try:
            subprocess.run([commandInput], check=True, shell=True)
        except subprocess.CalledProcessError as e:
            os.system("clear")
            print(f"there is no like this program -> {gc.GetValues["input"]}")

    def update():
        global mySoftwareList, drawFinish, drawTime
        _Input = str(gc.GetValues["input"]).strip("")

        # refrest list with input
        if gc.event == keyboard.Shift_L or gc.event == keyboard.Shift_R:
            if len(_Input) > 0:
                _inputHere = []
                _SoftwareList = os.listdir("/usr/bin")
                if drawTime > 0:
                    drawTime -= gc.dt
                else:
                    for i in _SoftwareList:
                        if _Input in i:
                            _inputHere.append(i)
                            gc.window["software"].update(_inputHere)
                            drawTime = 1
                drawFinish = False
            else:
                if not drawFinish:
                    _ReadyPrograms = []
                    _SoftwareList = os.listdir("/usr/bin")
                    for s in _SoftwareList:
                        if s in mySoftwareList:
                            if s not in _ReadyPrograms:
                                _ReadyPrograms.append(s)
                    gc.window["software"].update(_ReadyPrograms)
                    drawFinish = True

        # Run Program In Line
        if gc.event == "Return:36":
            _commandInput = str(gc.GetValues["input"])
            if len(_commandInput) > 0:
                print(_commandInput)
                Thread(target=RunThis, args=[_commandInput]).start()
            gc.closeWindow = True

        # Run Program In List
        elif gc.event == keyboard.space:
            _Select = str(gc.GetValues["software"]).strip("[]''")
            print(_Select)
            Thread(target=RunThis, args=[_Select]).start()
            gc.closeWindow = True

    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)





