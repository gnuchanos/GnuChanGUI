"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
import vlc



if __name__ == "__main__":
    gc = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()

    vid = [[gc.GCanvas(value="canvas", xStretch=True, yStretch=True, size=(750, None), bcolor=GColors().purple7)]]

    left = [
        [gc.GListBox(value="videos", font="Sans, 12", yStretch=True, xStretch=True, bcolor=GColors().purple8, noScroolBar=True)],
        [gc.hsep(color=GnuChanOSColor().colors3)],
        [gc.GText(title="Volume Slider", xStretch=True, position="center")],
        [gc.GSlider(value="volume", xStretch=True, range=(0, 100), defaultValue=80, bcolor=GColors().purple7, size=(20, None))],
        [gc.hsep(color=GnuChanOSColor().colors3)],
    ]

    _timeSize = 100
    layout = [ 
        [
            gc.Push(bcolor=GnuChanOSColor().colors1),
            gc.GButton(title="<"),
            gc.GButton(title="Open Video"),
            gc.GButton(title="Open Video Folder"),
            gc.GButton(title="Pause", value="pPlay"),
            gc.GButton(title=">"),
            gc.Push(bcolor=GnuChanOSColor().colors1),
        ],
        [
            gc.GColumn(winColumn=vid, xStretch=True, yStretch=True, bcolor=GColors().purple8),
            gc.GColumn(winColumn=left, xStretch=True, yStretch=True, bcolor=GColors().purple6, value="filePath"),
        ],
    ]

    gc.GWindow(mainWindow=layout)
    db = GKeyboard(window=gc.window)


    gc.GListBoxBorderSize(windowValue="videos", border=0)

    cans = gc.window["canvas"].Widget
    player.set_xwindow(cans.winfo_id()) # vscode can't auto-completed this .winfo_id()

    _Pause = False
    _videoFinish = False
    _startVideo = False
    _readyPlay = False
    _folderPath = ""
    video = ""
    videos = []
    _index = 0
    hideTree = False
    def update():
        global _Pause, video, videos, player, _startVideo, _index, _videoFinish, _readyPlay, _folderPath, db, hideTree

        try:
            if gc.event == db.Return:
                try:
                    video = vlc_instance.media_new(f"{_folderPath}/{videos[videos.index(str(gc.GetValues["videos"]).strip("[]'"))]}")
                    player.set_media(video)
                    player.play()
                except Exception as ERR:
                    print(ERR, " Return Key Press ERR")

            if gc.event == "Open Video Folder":
                _readyPlay = True
                _videoFinish = False
                _folderPath = gc.GetFolderPath(defaultPATH=str(os.path.expanduser("~")))
                _defaultList = os.listdir(_folderPath)
                for i in _defaultList:
                    if str(i).endswith(".mp4") or str(i).endswith(".mkv"):
                        videos.append(i)
                gc.window["videos"].update(videos)

                video = vlc_instance.media_new(f"{_folderPath}/{videos[0]}")
                player.set_media(video)
                player.play()

            if gc.event == "Open Video":
                _videoFinish = False
                _startVideo = True
                _videoPath = gc.GetFilePath(defaultPATH=str(os.path.expanduser("~")), fileTypes=gc.VideoTypes)
                player.stop()
                video = vlc_instance.media_new(_videoPath)
                player.set_media(video)
                player.play()

            elif gc.event == "pPlay":
                if not _videoFinish:
                    if _startVideo:
                        if pause:
                            player.pause()
                            gc.window["pPlay"].update("Pause")
                            pause = False
                        else:
                            player.pause()
                            gc.window["pPlay"].update("Play")
                            pause = True

            player.audio_set_volume(int(gc.GetValues["volume"]))

            if gc.event == "<":
                try:
                    if _readyPlay:
                        if _index > 0:
                            _index -= 1
                            player.stop()
                            _videoName = videos.index(_index)
                            _videoPath = f"{_folderPath}/{videos[_videoName]}"
                            video = vlc_instance.media_new(_videoPath)
                            player.set_media(video)
                            player.play()
                except Exception as ERR:
                    print(ERR, " < button ERR")

            if gc.event == '>':
                if _readyPlay:
                    if _index < len(videos):
                        _index += 1
                        player.stop()
                        _videoPath = f"{_folderPath}/{videos[_index-1]}"
                        video = vlc_instance.media_new(_videoPath)
                        player.set_media(video)
                        player.play()

            if _startVideo:
                if not _videoFinish:
                    if player.is_playing() != 0:
                        pass
                    else:
                        _videoFinish = True
            
            if gc.event == db.h:
                if not hideTree:
                    gc.window["filePath"].update(visible=False)
                    hideTree = True
                else:
                    gc.window["filePath"].update(visible=True)
                    hideTree = False



        except Exception as ERR:
            print(ERR)

    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)

