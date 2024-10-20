"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread
import subprocess
import keyboard
from pygame import mixer

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Music Player Powerad by Pygame!", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    musicPlay = GMixer()

    Buttons = [
        [
            gc.GPush(BColor=GnuChanOSColor().colors0),
            gc.GButton(Text="Add Folder"),
            gc.GButton(Text="<", WindowValue="Previous Music"),
            gc.GButton(Text="Play Music"),
            gc.GButton(Text="Stop Music"),
            gc.GButton(Text=">", WindowValue="Next Music"),
            gc.GPush(BColor=GnuChanOSColor().colors0)
        ],
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
            gc.GText(SetText=f"{dir}/", BColor=GColors().purple7, EmptySpace=(0, 0)), 
            gc.GInput(WindowValue="input", xStretch=True, BColor=GColors().purple7, EmptySpace=(0, 0))
        ],
        [   gc.GColumn(winColumnLayout_List=Buttons, xStretch=True, BColor=GColors().purple8)   ],
        [ 
            gc.GVSep(Color=GnuChanOSColor().colors3),
            gc.GListBox(WindowValue="mp3", Size=(75, None), LFont="Sans, 15", xStretch=True, yStretch=True, BColor=GnuChanOSColor().colors1, EmptySpace=(0, 0)),
            gc.GVSep(Color=GnuChanOSColor().colors3),
        ],
        [ 
            gc.GText(SetText="Music: ", BColor=GColors().purple7, EmptySpace=(0, 0)), 
            gc.GText(TextValue="musicName", xStretch=True, BColor=GColors().purple7, EmptySpace=(0, 0)) 
        ],
        [   gc.GSlider(MaxRange=(0, 10), DefaultValue=volume_slider, SDirection="h", WindowValue="slider", xStretch=True, BColor=GColors().purple8)   ]
    ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    gc.AddNewBorderWithColor(WindowValue="mp3", Color="red", BorderSize=0)
    gc.GetWindow["input"].update("Music")
    gkeys = GKeyboard(window=gc.GetWindow)

    def MusicPlay():
        global dir, path, volume, fileList, musicList, musicIndex, musicSelect, start, volume_slider, volume
        if gc.GetEvent == "Add Folder":
            try:
                musicPlay.SoundFileList = []
                path = f"{dir}/{gc.GetValues["input"]}"
                fileList = os.listdir(path=path)
                for i in fileList:
                    if i.endswith(".mp3"):
                        musicPlay.SoundFileList.append(f"{path}/{i}")
                musicPlay.SoundFileList.sort()
                gc.GetWindow["mp3"].update(musicPlay.SoundFileList)
            except Exception as ERR:
                print (f"{ERR}")
        
        if gc.GetEvent == "Play Music":
            if not start:
                musicPlay.PlaySound_SingleChannel(SoundPath=gc.GetValues["mp3"][0])
                gc.GetWindow["musicName"].update(gc.GetValues["mp3"][0])

        elif gc.GetEvent == "Stop Music":
            musicPlay.StopSound()

        elif gc.GetEvent == "Next Music" or gc.GetEvent == gkeys.d:
            if not start:
                _musicName = musicPlay.NextSound_SingleChannel()
                gc.GetWindow["musicName"].update(musicPlay.MusicName)

        elif gc.GetEvent == "Previous Music" or gc.GetEvent == gkeys.a:
            if not start:
                _musicName = musicPlay.PreviousSound_SingleChannel()
                gc.GetWindow["musicName"].update(musicPlay.MusicName)

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

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)


