"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from sqlite3 import Time
from GnuChanGUI import *
from threading import Thread
from datetime import time

#Thread(target=DownloadVideo, args=[]).start()
"""
this only works with ffmpeg
"""

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple mp4 to mp3 conventer", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [ gc.GText(SetText=" Input File: ", BColor=GColors().purple8, EmptySpace=(0, 0)),  
         gc.GText(SetValue="InputFile",   xStretch=True,  TPosition="left", BColor=GColors().purple8, EmptySpace=(0, 0)) ],
        [ gc.GText(SetText=" Output File: ", BColor=GColors().purple8, EmptySpace=(0, 0)),
         gc.GText(SetValue="OutputFile",  xStretch=True,  TPosition="left", BColor=GColors().purple8, EmptySpace=(0, 0)) ],
        [
            gc.GText(xStretch=True),
            gc.GButton(Text="Select Input Folder"),
            gc.GButton(Text="Select Output Folder"),
            gc.GButton(Text="Start Convert"),
            gc.GText(xStretch=True),
        ],
        [ gc.GText(SetText="Mp4 Files", TPosition="center", xStretch=True, BColor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(SetValue="mp4List", xStretch=True, yStretch=True, LFont="Sans, 12") ],
        [ gc.GText(SetText="Mp3 Files", TPosition="center", xStretch=True, BColor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(SetValue="output", xStretch=True, yStretch=True, LFont="Sans, 12") ],
        [ gc.GText(SetText="There is no error log please open this program in terminal", xStretch=True, BColor=GnuChanOSColor().colors0, TPosition="center") ],
    ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    gc.GListBoxBorderSize(WindowValue="mp4List", Border=0)

    GInput = GOutput = ""
    InputMp4Folder = []
    StartConvert = False

    def Convert():
        global GInput, GOutput, StartConvert, InputMp4Folder

        path = os.path.expanduser(GInput)
        path2 = os.path.expanduser(GOutput)
        for i in InputMp4Folder:
            input_file = os.path.join(path, i)
            output_file = os.path.join(path2, f"{i[:-4]}.mp3")
            music_command = f"ffmpeg -i '{input_file}' -b:a 192K -vn -y '{output_file}'"
            os.system(music_command)

        _outputfolder = os.listdir(path2)
        _mp3List = []
        for i in _outputfolder:
            if str(i).endswith(".mp3"):
                _mp3List.append(i)
        gc.GetWindow["output"].update(_mp3List)
        os.popen("notify-send -t 7000 -u low \"Convert Finish..! Maybe Check Terminal\"")


    def update():
        global GInput, GOutput, StartConvert, InputMp4Folder

        if gc.GetEvent == "Select Input Folder":
            try:
                GInput = popup_get_folder('Select a folder to open', no_window=True)
                gc.GetWindow["InputFile"].update(GInput)
                path = os.path.expanduser(GInput)
                for file in os.listdir(path):
                    if file.endswith(".mp4"):
                        InputMp4Folder.append(file)
                gc.GetWindow["mp4List"].update(InputMp4Folder)
            except Exception as ERR:
                print(ERR)

        if gc.GetEvent == "Select Output Folder":
            try:
                GOutput = popup_get_folder('Select a folder to open', no_window=True)
                gc.GetWindow["OutputFile"].update(GOutput)
            except Exception as ERR:
                print(ERR)

        if gc.GetEvent == "Start Convert":
            StartConvert = True

        if StartConvert:
            Thread(target=Convert, args=[]).start()
            StartConvert = False

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)

