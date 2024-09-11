"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread
import subprocess
from pygame import mixer

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Music Player Powerad by Pygame!", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    musicPlay = GMixer()

    Buttons = [
        [gc.GButton(title="Add Folder", size=(12, None))],
        [gc.GButton(title="Play Music", size=(12, None))],
        [gc.GButton(title="Next Music", size=(12, None))],
        [gc.GButton(title="Stop Music", size=(12, None))],
        [gc.GButton(title="Previous Music", size=(12, None))],
        [gc.Push]
    ]

    dir = os.path.expanduser("~")
    path = ""
    volume = 0.5
    volume_slider = 5
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
            gc.GListBox(value="mp3", size=(75, None), font="Sans, 15", xStretch=True, yStretch=True, bcolor=GColors().purple5, EmptySpace=(0, 0)),
            gc.vsep,
        ],
        [ 
            gc.GText(title="Music: ", bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)), 
            gc.GText(value="musicName", xStretch=True, bcolor=GnuChanOSColor().colors0, EmptySpace=(0, 0)) 
        ],
        [ gc.GSlider(range=(0, 10), defaultValue=volume_slider, direction="h", value="slider", xStretch=True) ]
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(windowValue="mp3", border=0)
    gc.window["input"].update("Music")


    def MusicPlay():
        global dir, path, volume, fileList, musicList, musicIndex, musicSelect, start, volume_slider, volume
        if gc.event == "Add Folder":
            try:
                musicPlay.SoundFileList = []
                path = f"{dir}/{gc.GetValues["input"]}"
                fileList = os.listdir(path=path)
                for i in fileList:
                    if i.endswith(".mp3"):
                        musicPlay.SoundFileList.append(f"{path}/{i}")
                musicPlay.SoundFileList.sort()
                gc.window["mp3"].update(musicPlay.SoundFileList)
            except Exception as ERR:
                print (f"{ERR}")
        
        if gc.event == "Play Music":
            if not start:
                musicPlay.PlaySound_SingleChannel(SoundPath=gc.GetValues["mp3"][0])
                gc.window["musicName"].update(gc.GetValues["mp3"][0])

        elif gc.event == "Stop Music":
            musicPlay.StopSound()

        elif gc.event == "Next Music":
            if not start:
                _musicName = musicPlay.NextSound_SingleChannel()
                gc.window["musicName"].update(musicPlay.MusicName)

        elif gc.event == "Previous Music":
            if not start:
                _musicName = musicPlay.PreviousSound_SingleChannel()
                gc.window["musicName"].update(musicPlay.MusicName)

    def volume_func():
        global volume
        volume_slider = int(gc.GetValues["slider"])
        if volume_slider != 10:
            volume = float(f"0.{volume_slider}")
        else:
            volume = 1
        mixer.music.set_volume(volume)

    def update():
        Thread(target=MusicPlay, args=[]).start()
        Thread(target=volume_func, args=[]).start()

    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)


