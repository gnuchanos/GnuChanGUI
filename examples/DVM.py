
from threading import Thread
import os
from pydub import AudioSegment
from pytube import YouTube
from GnuChanGUI import *


if __name__ == "__main__":

    gc = GnuChanGUI(Title="", Size=(1012, 600), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    ytlinksave = ""
    folderpathsave = ""
    readyDownload = ""
    video_url = ""

    layout = [ 
        [gc.GText(title="Download Music And Video", position="center", xStretch=True, bcolor=GnuChanOSColor().colors0)],
        [
            gc.Push,
                gc.GRadio(title="Video", groupID="yt", value="video"),
                gc.GRadio(title="Music", groupID="yt", value="music"),
            gc.Push,
        ],
        [gc.GText(title="YT Link: ", bcolor=GnuChanOSColor().colors0), gc.GInput(value="yt", xStretch=True)],
        [gc.GText(title="Folder Path: ", bcolor=GnuChanOSColor().colors0), 
         gc.GText(value="showpath"),
         gc.GInput(value="path", xStretch=True)],

        [gc.hsep],
        [gc.Push, gc.GButton(title="Download"), gc.Push],
        [gc.GText(title="Add Yt Link", value="ytlink", xStretch=True, position="center")],
        [gc.GText(title=f"{os.path.expanduser(f"~")}/Add Pc Folder", value="pathshow", xStretch=True, position="center")],
        [gc.hsep],

        [gc.GLog(value="output", xStretch=True, yStretch=True)]
        

              ]

    gc.GWindow(mainWindow=layout)
    gc.window["showpath"].update(f"{os.path.expanduser(f"~")}/")


    def DownloadVideo():
        global video_url
        try:
            #yt link
            video_url = str(gc.GetValues["yt"]).strip(" "); 
            gc.window["ytlink"].update(f"YT Link: {video_url[24:]}")

            # folder path
            userPath = str(gc.GetValues["path"]).strip(" ")
            Dir = os.path.expanduser(f"~")
            output_path = f"{Dir}/{userPath}/"

            print(video_url, " | ", userPath)
            if video_url != "":
                # .mp4 download
                yt = YouTube(video_url)
                video_stream = yt.streams.get_highest_resolution()
                video_title = yt.title
                video_file = video_stream.download(output_path=output_path, filename=f"{video_title}.mp4")
                print(f"{video_title} Download Finish")
        except Exception as ERR:
            print(f"{ERR} - Better Error Message Then Windows - unknow error like our sciens guy working on it")



    def DownloadMusic():
        try:
            # yt link
            video_url = str(gc.GetValues["yt"]).strip(" "); 
            gc.window["ytlink"].update(f"YT Link: {video_url[24:]}")

            # folder path
            userPath = str(gc.GetValues["path"]).strip(" ")
            gc.window["pathshow"].update(f"Folder Path:{userPath}")
            Dir = os.path.expanduser(f"~")
            output_path = f"{Dir}/{userPath}/"

            if video_url != "":
                # download .mp4 and convert later
                yt = YouTube(video_url)
                video_title = yt.title.replace(" ", "_").replace("/", "_").replace("\\", "_")
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_file = audio_stream.download(output_path=output_path, filename=f"{video_title}.mp4")

                # convert .mp4 to mp3
                audio = AudioSegment.from_file(audio_file)
                mp3_file = os.path.splitext(audio_file)[0] + '.mp3'
                audio.export(mp3_file, format='mp3')
                print(f"{video_title} Download Finish")

                # Remove the old MP4 file once the MP3 conversion is finished.
                os.remove(audio_file)
        except Exception as ERR:
            print(f"{ERR} - BTW I USE ARCH LINUX")


    def update():
        global readyDownload

        if gc.event in ["video", "music"]:
            if gc.event == "video":
                readyDownload = "video"
            elif gc.event == "music":
                readyDownload = "music"

        if gc.event == "Download":
            if readyDownload == "video":
                Thread(target=DownloadVideo, args=[]).start()
            elif readyDownload == "music":
                Thread(target=DownloadMusic, args=[]).start()



    gc.update(GUpdate=update)
