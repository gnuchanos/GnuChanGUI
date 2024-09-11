"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""
from GnuChanGUI import *
from threading import Thread

#Thread(target=DownloadVideo, args=[]).start()
"""
this only works with ffmpeg
"""

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple mp4 to mp3 conventer", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [ gc.GText(title="Input File: "), gc.GText(value="InputFile",  xStretch=True,  position="center") ],
        [ gc.GText(title="Output File: "), gc.GText(value="OutputFile", xStretch=True, position="center") ],
        [
            gc.GText(xStretch=True),
            gc.GButton(title="Select Input Folder"),
            gc.GButton(title="Select Output Folder"),
            gc.GButton(title="Start Convert"),
            gc.GText(xStretch=True),
        ],
        [ gc.GText(title="Mp4 Files", position="center", xStretch=True, bcolor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(value="mp4List", xStretch=True, yStretch=True, font="Sans, 12") ],
        [ gc.GText(title="Mp3 Files", position="center", xStretch=True, bcolor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(value="output", xStretch=True, yStretch=True, font="Sans, 12") ],
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(windowValue="mp4List", border=0)

    GInput = GOutput = ""
    InputMp4Folder = []
    StartConvert = False

    def update():
        global GInput, GOutput, StartConvert, InputMp4Folder

        if gc.event == "Select Input Folder":
            try:
                GInput = popup_get_folder('Select a folder to open', no_window=True)
                gc.window["InputFile"].update(GInput)
                path = os.path.expanduser(GInput)
                for file in os.listdir(path):
                    if file.endswith(".mp4"):
                        InputMp4Folder.append(file)
                gc.window["mp4List"].update(InputMp4Folder)
            except Exception as ERR:
                print(ERR)

        if gc.event == "Select Output Folder":
            try:
                GOutput = popup_get_folder('Select a folder to open', no_window=True)
                gc.window["OutputFile"].update(GOutput)
            except Exception as ERR:
                print(ERR)

        if gc.event == "Start Convert":
            StartConvert = True

        if StartConvert:
            path = os.path.expanduser(GInput)
            path2 = os.path.expanduser(GOutput)
            for i in InputMp4Folder:
                input_file = os.path.join(path, i)
                output_file = os.path.join(path2, f"{i[:-4]}.mp3")
                music_command = f"ffmpeg -i '{input_file}' -b:a 192K -vn '{output_file}'"
                subprocess.run(music_command, shell=True)

            _outputfolder = os.listdir(path2)
            _mp3List = []
            for i in _outputfolder:
                if str(i).endswith(".mp3"):
                    _mp3List.append(i)
            gc.window[""].update(_mp3List)

            StartConvert = False
                    
    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)

