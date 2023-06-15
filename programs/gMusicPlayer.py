from GnuChanGUI import *
import subprocess
import os





def main():
    global MUSIC_FOLDER
    global music_files
    global current_music_index
    global vlc_process

    default = GnuChanGUI(Title="GnuChan Program Music Player", Size=(800,600), resizable=True)
    default.Theme()
    defaultFont = "Sans, 15"
    MUSIC_FOLDER = ""
    music_files = []
    current_music_index = 0
    vlc_process = None

    gMenu = [
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
    ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GText("GnuChan Simple Music Player", font="Sans, 20", xStretch=True, position="center")],
        [default.GText("", font=defaultFont, xStretch=True)],
        [   
            default.GButton(title="Play Music", font=defaultFont, xStretch=True), 
            default.GButton(title="Stop Music", font=defaultFont, xStretch=True),
            default.GButton(title="Open Music Folder", font=defaultFont, xStretch=True)
        ],
        [   
            default.GListBox(list=[], xStretch=True, yStretch=True, value="-MUSIC LIST-", noScroolBar=True, font=defaultFont, position="center")
        ],
        [   
            default.GText("Play Music:", font=defaultFont, xStretch=True),
            default.GText("", value="musicName", font=defaultFont, xStretch=True)
        ],
        [   
            default.GButton(title="Play Next", value="-PLAY NEXT-", font=defaultFont, xStretch=True), 
            default.GButton(title="Play Prev", value="-PLAY PREV-", font=defaultFont, xStretch=True),
            default.GButton(title="Volume +", value="-VOLUME UP-", font=defaultFont, xStretch=True),
            default.GButton(title="Volume -", value="-VOLUME DOWN-", font=defaultFont, xStretch=True)
        ]
    ]

    default.GWindow(mainWindow=layout)
    default.GListBoxFixer(value="-MUSIC LIST-", border=0)


    def play_music(music_path):
        global vlc_process
        if vlc_process is not None:
            stop_music()
        vlc_args = ["cvlc", "--play-and-exit", music_path]
        vlc_process = subprocess.Popen(vlc_args)

    def stop_music():
        global vlc_process
        if vlc_process is not None:
            vlc_process.terminate()
        vlc_process = None

    def play_next_music():
        global current_music_index
        if len(music_files) > 0:
            current_music_index = (current_music_index + 1) % len(music_files)
            selected_music = music_files[current_music_index]
            music_path = os.path.join(MUSIC_FOLDER, selected_music)
            play_music(music_path)
            default.window["musicName"].update(music_path)

    def play_previous_music():
        global current_music_index
        if len(music_files) > 0:
            current_music_index = (current_music_index - 1) % len(music_files)
            selected_music = music_files[current_music_index]
            music_path = os.path.join(MUSIC_FOLDER, selected_music)
            play_music(music_path)
            default.window["musicName"].update(music_path)

    def decrease_volume():
        subprocess.run(['pactl', 'set-sink-volume', '@DEFAULT_SINK@', '-5%'])

    def increase_volume():
        subprocess.run(['pactl', 'set-sink-volume', '@DEFAULT_SINK@', '+5%'])

    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            stop_music()
            break


        if event == "Open Music Folder":
            
            MUSIC_FOLDER = popup_get_folder('Select a file to open', no_window=True)
            try:
                if MUSIC_FOLDER != "":
                    music_files = [file for file in os.listdir(MUSIC_FOLDER) if file.endswith(".mp3")]
                    default.window["-MUSIC LIST-"].update(values=music_files)
            except TypeError:
                print("Select Music Folder") 


        if MUSIC_FOLDER != "":
            if event == "Play Music":
                try:
                    selected_music = GetValues["-MUSIC LIST-"][0]
                    music_path = os.path.join(MUSIC_FOLDER, selected_music)
                    current_music_index = music_files.index(selected_music)
                    play_music(music_path)
                    default.window["musicName"].update(music_path)
                except IndexError:
                    print("You forgot to add a music folder")

            elif event == "Stop Music":
                stop_music()

            elif event == "-PLAY NEXT-":
                play_next_music()

            elif event == "-PLAY PREV-":
                play_previous_music()

            elif event == "-VOLUME UP-":
                increase_volume()

            elif event == "-VOLUME DOWN-":
                decrease_volume()
            if vlc_process is not None and vlc_process.poll() is not None:
                current_music_index = (current_music_index + 1) % len(music_files)
                selected_music = music_files[current_music_index]
                music_path = os.path.join(MUSIC_FOLDER, selected_music)
                play_music(music_path=music_path)

    default.window.close()

if __name__ == "__main__":
    main()
