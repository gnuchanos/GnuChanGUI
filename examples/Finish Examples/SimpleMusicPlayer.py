"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread
import subprocess



#Thread(target=DownloadVideo, args=[]).start()
if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(1250, 900), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    menu = [
        ["Menu", ["Close"]]
    ]


    Buttons = [
        [gc.GMenuForTheme(winMenu=menu)],
        [gc.GButton(title="Add Folder", size=(12, None))],
        [gc.GButton(title="Play Music", size=(12, None))],
        [gc.GButton(title="Next Music", size=(12, None))],
        [gc.GButton(title="Stop Music", size=(12, None))],
        [gc.GButton(title="Previous Music", size=(12, None))],
        [gc.hsep],
        [gc.GText(title="Next or Previous\nonly works\n if you Play Music", position="center", xStretch=True, bcolor=GColors().purple6)],
        [gc.hsep],
        [gc.Push]
    ]

    dir = os.path.expanduser("~")
    path = ""
    volume = 19656
    volume_slider = 60
    fileList = []
    musicList = []
    musicIndex = 0
    musicSelect = ""
    start = False


    layout = [
        [
            gc.GText(title=f"{dir}/", bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)), 
            gc.GInput(value="input", xStretch=True, bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0))
        ],
        [ 
            gc.vsep,
            gc.GColumn(winColumn=Buttons, yStretch=True, bcolor=GColors().purple8, EmptySpace=(0, 0)),
            gc.vsep,
            gc.GListBox(value="mp3", size=(75, None), font="Sans, 15", xStretch=True, yStretch=True, noScroolBar=True, bcolor=GColors().purple5, EmptySpace=(0, 0)),
            gc.vsep,
        ],
        [ 
            gc.GText(title="Music: ", bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)), 
            gc.GText(value="musicName", xStretch=True, bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)) 
        ],
        [ gc.GSlider(range=(0, 100), defaultValue=volume_slider, direction="h", value="slider", xStretch=True) ]
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(border=0, value="mp3")
    gc.window["input"].update("Music")


    def MusicPlay():
        global dir, path, volume, fileList, musicList, musicIndex, musicSelect, start, volume_slider
        if gc.event == "Add Folder":
            try:
                musicList = []
                path = f"{dir}/{gc.GetValues["input"]}"
                fileList = os.listdir(path=path)
                for i in fileList:
                    if i.endswith(".mp3"):
                        musicList.append(i)
                gc.window["mp3"].update(musicList)
            except Exception as ERR:
                print (f"{ERR}")
        
        if gc.event == "Play Music":
            try: 
                if not start:
                    musicIndex = musicList.index(gc.GetValues["mp3"][0])
                    musicSelect = musicList[musicIndex]
                    music_command = f"mpg123 -f '{str(volume)}' '{path}/{musicSelect}'"
                    play_process = subprocess.Popen(music_command, shell=True)
                    gc.window["musicName"].update(musicSelect)
                    start = True
            except Exception as ERR:
                print(f"{ERR}")

        elif gc.event == "Next Music":
            if start:
                if musicIndex < len(musicList) - 1:
                    musicIndex += 1
                    musicSelect = musicList[musicIndex]
                    music_command = f"killall mpg123 && mpg123 -f '{str(volume)}' '{path}/{musicSelect}'"
                    play_process = subprocess.Popen(music_command, shell=True)
                    gc.window["musicName"].update(musicSelect)

        elif gc.event == "Previous Music":
            if start:
                if musicIndex > 0:
                    musicIndex -= 1
                    musicSelect = musicList[musicIndex]
                    music_command = f"killall mpg123 && mpg123 -f '{str(volume)}' '{path}/{musicSelect}'"
                    play_process = subprocess.Popen(music_command, shell=True)
                    gc.window["musicName"].update(musicSelect)

        elif gc.event == "Stop Music":
            if start:
                killall = subprocess.Popen(["killall", "mpg123"])
                gc.window["musicName"].update("")
                start = False

        if gc.event == "Close":
            subprocess.Popen(["killall", "mpg123"])
            gc.closeWindow = True

    def update():
        Thread(target=MusicPlay, args=[]).start()


        volume_slider = gc.GetValues["slider"]

        

    if gc.window.close == True:
        subprocess.Popen(["killall", "mpg123"])

    gc.update(GUpdate=update)
