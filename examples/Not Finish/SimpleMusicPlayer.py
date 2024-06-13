"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread
from pygame import mixer



#Thread(target=DownloadVideo, args=[]).start()
if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(1250, 900), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    Buttons = [
        [gc.GButton(title="Add Folder", size=(12, None))],
        [gc.GButton(title="Play Music", size=(12, None))],
        [gc.GButton(title="Stop Music", size=(12, None))],
        [gc.Push]
    ]

    dir = os.path.expanduser("~")
    path = ""
    volume = 0.5
    play = False

    layout = [
        [
            gc.GText(title=f"{dir}/"), gc.GInput(value="input", xStretch=True, bcolor=GnuChanOSColor().colors0)
        ],
        [ 
            gc.GColumn(winColumn=Buttons, yStretch=True),
            gc.GListBox(value="mp3", size=(70, None), xStretch=True, yStretch=True, noScroolBar=True, bcolor=GnuChanOSColor().colors2)
        ]
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(border=0, value="mp3")
    gc.window["input"].update("Music/CyberpunkSamurai")


    class PlayMusic:
        def __init__(self, soundfile="") -> None:
            mixer.init()
            self.soundFile = soundfile

        @property
        def play(self):
            self.music = mixer.Sound(self.soundFile)
            self.music.set_volume(0.1)
            self.music.play()
        
        @property
        def stop(self):
            self.music.stop()

    music = PlayMusic(soundfile="")


    def update():
        global dir, path, volume, music, play
        if gc.event == "Add Folder":
            path = f"{dir}/{gc.GetValues["input"]}"
            fileList = os.listdir(path=path)
            gc.window["mp3"].update(fileList)
        
        if gc.event == "Play Music":
            if not play:
                music.soundFile = f"{path}/{gc.GetValues["mp3"][0]}" 
                Thread(target=music.play, args=[]).start()
                play = True
        elif gc.event == "Stop Music":
            if play:
                Thread(target=music.stop, args=[]).start()
                play = False

    gc.update(GUpdate=update)
