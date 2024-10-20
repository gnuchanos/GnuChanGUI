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

    vid = [[gc.GCanvas(WindowValue="canvas", xStretch=True, yStretch=True, Size=(750, None), BColor=GColors().purple7)]]

    left = [
        [gc.GListBox(WindowValue="videos", LFont="Sans, 12", yStretch=True, xStretch=True, BColor=GColors().purple8, noScroolBar=True)],
        [gc.GHSep(Color=GnuChanOSColor().colors3)],
        [gc.GText(SetText="Volume Slider", xStretch=True, TPosition="center")],
        [gc.GSlider(WindowValue="volume", xStretch=True, MaxRange=(0, 100), DefaultValue=80, BColor=GColors().purple7, Size=(20, None))],
        [gc.GHSep(Color=GnuChanOSColor().colors3)],
    ]

    layout = [ 
        [
            gc.GPush(BColor=GnuChanOSColor().colors1),
            gc.GButton(Text="<"),
            gc.GButton(Text="Open Video"),
            gc.GButton(Text="Open Video Folder"),
            gc.GButton(Text="Pause", WindowValue="pPlay"),
            gc.GButton(Text=">"),
            gc.GPush(BColor=GnuChanOSColor().colors1),
        ],
        [
            gc.GColumn(winColumnLayout_List=vid,  xStretch=True, yStretch=True, BColor=GColors().purple8),
            gc.GColumn(winColumnLayout_List=left, xStretch=True, yStretch=True, BColor=GColors().purple6, SetWindowValue="filePath"),
        ],
    ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    db = GKeyboard(window=gc.GetWindow)


    gc.GListBoxBorderSize(WindowValue="videos", Border=0)

    cans = gc.GetWindow["canvas"].Widget
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
            if gc.GetEvent == db.Return:
                try:
                    video = vlc_instance.media_new(f"{_folderPath}/{videos[videos.index(str(gc.GetValues["videos"]).strip("[]'"))]}")
                    player.set_media(video)
                    player.play()
                except Exception as ERR:
                    print(ERR, " Return Key Press ERR")

            if gc.GetEvent == "Open Video Folder":
                _readyPlay = True
                _videoFinish = False
                _folderPath = gc.GetFolderPath(defaultPATH=str(os.path.expanduser("~")))
                _defaultList = os.listdir(_folderPath)
                for i in _defaultList:
                    if str(i).endswith(".mp4") or str(i).endswith(".mkv"):
                        videos.append(i)
                gc.GetWindow["videos"].update(videos)

                video = vlc_instance.media_new(f"{_folderPath}/{videos[0]}")
                player.set_media(video)
                player.play()

            if gc.GetEvent == "Open Video":
                _videoFinish = False
                _startVideo = True
                _videoPath = gc.GetFilePath(defaultPATH=str(os.path.expanduser("~")), fileTypes=gc.VideoTypes)
                player.stop()
                video = vlc_instance.media_new(_videoPath)
                player.set_media(video)
                player.play()

            elif gc.GetEvent == "pPlay":
                if not _videoFinish:
                    if _startVideo:
                        if pause:
                            player.pause()
                            gc.GetWindow["pPlay"].update("Pause")
                            pause = False
                        else:
                            player.pause()
                            gc.GetWindow["pPlay"].update("Play")
                            pause = True

            player.audio_set_volume(int(gc.GetValues["volume"]))

            if gc.GetEvent == "<":
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

            if gc.GetEvent == '>':
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
            
            if gc.GetEvent == db.h:
                if not hideTree:
                    gc.GetWindow["filePath"].update(visible=False)
                    hideTree = True
                else:
                    gc.GetWindow["filePath"].update(visible=True)
                    hideTree = False



        except Exception as ERR:
            print(ERR)

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)

