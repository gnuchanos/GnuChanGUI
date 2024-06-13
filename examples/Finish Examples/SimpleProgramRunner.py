"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread



#Thread(target=DownloadVideo, args=[]).start()


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(350, 600), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    SoftwareListActive = []
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
        "discord", "telegram-desktop", "skype", "zoom",
        # Clouth APP
        "dropbox", "nextcloud", "megasync", "insync",
        # EMail APP
        "thunderbird", "geary", "evolution", "kmail",
        # Games
        "steam", "lutris", "minecraft-launcher", "mgba-qt", "PPSSPPSDL", "duckstation-qt", "pcsx2-qt", "melonDS", "snes9x", "nestopia"
        # Sanal Makineler ve Emülatörler
        "virtualbox", "vmware-player", "gnome-boxes", "qemu" ]

    middleThings = [
        [ 
            gc.GText(title="> ", bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)), 
            gc.GInput(value="input", size=(20, None), bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)) 
        ],
        [ gc.GText(title="", xStretch=True) ],
        [ gc.GListBox(value="software", position="center", xStretch=True, yStretch=True, noScroolBar=True) ],
        [ gc.GText(title="", xStretch=True) ],
    ]

    layout = [ 
        [ gc.GText(xStretch=True) ],
        [ gc.GText(xStretch=True), gc.GColumn(winColumn=middleThings, yStretch=True), gc.GText(xStretch=True) ] ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(value="software", border=0)

    def softwareListFunc():
        global SoftwareListActive, mySoftwareList
        softwareList = os.listdir("/usr/bin")
        for i in softwareList:
            if i in mySoftwareList:
                SoftwareListActive.append(i)
        gc.window["software"].update(SoftwareListActive)
    softwareListFunc()

    def update():
        global Start
        if gc.event == "Return:36":
            try:
                commandInput = str(gc.GetValues["input"])
                if commandInput != "" or len(commandInput) > 3:
                    subprocess.Popen(commandInput, shell=True)
                    gc.closeWindow = True
                else:
                    command = str(gc.GetValues["software"]).strip("[]")
                    subprocess.Popen(command, shell=True)
                    gc.closeWindow = True
            except Exception as Err:
                print(f"{Err} - UwU")


    gc.update(GUpdate=update)



