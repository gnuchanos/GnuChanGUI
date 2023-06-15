from GnuChanGUI import *
from pytube import YouTube, Playlist
from pytube.exceptions import AgeRestrictedError

import os

def download_audio(url, output_path):
    try:
        audio = YouTube(url).streams.filter(only_audio=True).first()
        if audio:
            audio_file = audio.download(output_path=output_path)
            mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
            os.rename(audio_file, mp3_file)
            print("Audio download completed successfully.")
        else:
            print("No suitable audio stream found for download.")
    except Exception as e:
        print("An error occurred during the download process:", str(e))



def download_playlist(playlist_url, output_path):
    try:
        playlist = Playlist(playlist_url)
        if playlist:
            for video_url in playlist.video_urls:
                try:
                    video = YouTube(video_url)
                    if not video.age_restricted:
                        audio = video.streams.filter(only_audio=True).first()
                        if audio:
                            audio_file = audio.download(output_path=output_path)
                            mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
                            os.rename(audio_file, mp3_file)
                except AgeRestrictedError:
                    continue

            print("Playlist download completed successfully.")
        else:
            print("No playlist found at the given URL.")
    except Exception as e:
        print("An error occurred during the download process:", str(e))



def download_video(url, quality="high", format="mp4", output_path=None):
    yt = YouTube(url)

    if quality == "high":
        streams = yt.streams.filter(progressive=True, file_extension=format)
        if not streams:
            print("Belirtilen formatta bir video akışı bulunamadı.")
            return
        video = streams.get_highest_resolution()
    elif quality == "low":
        streams = yt.streams.filter(progressive=True, file_extension=format)
        if not streams:
            print("Belirtilen formatta bir video akışı bulunamadı.")
            return
        video = streams.get_lowest_resolution()
    else:
        print("Geçersiz kalite seçeneği. Varsayılan akış indiriliyor...")
        streams = yt.streams.filter(progressive=True, file_extension=format)
        if not streams:
            print("Belirtilen formatta bir video akışı bulunamadı.")
            return
        video = streams.first()

    video.download(output_path=output_path)


def main():
    default = GnuChanGUI(Title="GnuChan Program Music and Video Downloander", Size=(800, 600), resizable=True)
    default.Theme()
    defaultFont = "Sans, 15"

    download = ""
    filePath = ""
    filetype = ""
    ytQuality = ""

    musicWin = [
        [default.GText("music Download", font=defaultFont, xStretch=True, position="center")],

        [default.GRadio(title="Music", font=defaultFont, groupID="download", value="music"),
         default.GRadio(title="Video", font=defaultFont, groupID="download", value="video")],

        [default.GText("Youtube Link: ", font=defaultFont),
         default.GInput(value="ytLink", focus=True, font=defaultFont, xStretch=True)],

        [default.GText(title=filePath, value="filepath", font=defaultFont, xStretch=True),
         default.GButton(title="Select Download Folder", font=defaultFont)],

        [default.GText("", bColor="black", xStretch=True)],
        [default.GText(title="This part is just video if you need music just leave empty", font=defaultFont,
                       xStretch=True, position="center")],
        [default.Push,
         default.GText(title="Video resolution", font=defaultFont),
         default.GRadio(title="high", font=defaultFont, groupID="resolution", value="high"),
         default.GRadio(title="low", font=defaultFont, groupID="resolution", value="low"),

         default.GText(title="               ", font=defaultFont),

         default.GText(title="File Type #mp4 and mkv", font=defaultFont),
         default.GRadio(title="mp4", font=defaultFont, groupID="filetype", value="mp4"),
         default.Push],

        [default.GButton(title="Download Music", font=defaultFont, xStretch=True),
         default.GButton(title="Download PlayList", font=defaultFont, xStretch=True),
         default.GButton(title="Download Video", font=defaultFont, xStretch=True)]
    ]

    gMenu = [
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
    ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GColumn(winColumn=musicWin, xStretch=True)],
        [default.GLog(xStretch=True, yStretch=True, font=defaultFont)]
    ]

    default.GWindow(mainWindow=layout)

    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            break

        if event in ["music", "video"]:
            download = event
            print(download)

        if download == "video":
            if event in ["mp4"]:
                filetype = event
                print(filetype)
            if event in ["high", "low"]:
                ytQuality = event
                print(ytQuality)

        if event == "Select Download Folder":
            filePath = popup_get_folder('Select a file to save', no_window=True)
            default.window["filepath"].update(filePath)

        if download == "music" and filePath != "":
            if event == "Download Music":
                audio_url = GetValues["ytLink"]
                download_audio(url=audio_url, output_path=filePath)
            elif event == "Download PlayList":
                playList = GetValues["ytLink"]
                download_playlist(playlist_url=playList, output_path=filePath)
        elif download == "video" and filePath != "":
            if event == "Download Video":
                videourl = GetValues["ytLink"]
                download_video(url=videourl, quality=ytQuality, format=filetype, output_path=filePath)
        else:
            pass

    default.window.close()


if __name__ == "__main__":
    main()