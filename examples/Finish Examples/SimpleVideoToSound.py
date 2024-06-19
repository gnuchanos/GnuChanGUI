"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread

#Thread(target=DownloadVideo, args=[]).start()


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(1012, 900), resizable=True, finalize=True)
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
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
        [ gc.GListBox(value="mp4List", xStretch=True, yStretch=True, noScroolBar=True) ],
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
        [ gc.GLog(value="output", xStretch=True, yStretch=True, font="Sans, 12") ],
        [ gc.GText(xStretch=True, bcolor=GnuChanOSColor().colors0) ],
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(value="mp4List", border=0)

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
                #InputMp4Folder = [f for f in os.listdir(path) if f.endswith(".mp4")]
                
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
                print(music_command)
                subprocess.run(music_command, shell=True)
            StartConvert = False
                    
                   




    gc.update(GUpdate=update)