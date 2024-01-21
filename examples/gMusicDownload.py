from GnuChanGUI import *
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import subprocess

# install ffmpeg

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(900, 600), resizable=False)
Themecolors().GnuChanOS

gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]

link = ""
path = ""
downloadPATH = ""
dirList = []
musicList = []

path2 = ""
downloadList = []

SingleDownload = [
    [gc.GText(title="Music Folder -> /home/user/Music/", font="Sans, 20", xStretch=True, position="center")],
    [gc.GInput(font="Sans, 20", xStretch=True, value="path"), gc.GButton(title="Select Folder", font="Sans, 20", value="tab1")],
    [gc.hsep],
    [gc.GInput(value="link", font="Sans, 20", xStretch=True),
     gc.GButton(title="Download", font="Sans, 20")],
    [gc.GListBox(value="pathList", font="Sans, 20", xStretch=True, yStretch=True)],
    [gc.GButton(title="Refresh Files", font="Sans, 20")] 
]

MultipleDownload = [
    [gc.GText(title="Music Folder -> /home/user/Music/", font="Sans, 20", xStretch=True, position="center")],
    [gc.GInput(font="Sans, 20", xStretch=True, value="path2"), gc.GButton(title="Select Folder", font="Sans, 20", value="tab2")],
    [gc.hsep],
    [gc.GInput(value="link2", font="Sans, 20", xStretch=True), gc.GButton(title="ADD", font="Sans, 20")],
    [gc.GListBox(value="dlist", font="Sans, 20", xStretch=True, yStretch=True)],
    [gc.GButton(title="Download ALL", font="Sans, 20"), gc.GButton(title="Remove", font="Sans, 20"), ]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GTabGroup(TabGroupLayout=[
        [gc.GTab(title="Single Download", TabLayout=SingleDownload)],
        [gc.GTab(title="Multiple Download", TabLayout=MultipleDownload)],
    ])]
    
    ]

gc.GWindow(mainWindow=layout)

gc.GListBoxBorderSize(value="pathList", border=0)
gc.GListBoxBorderSize(value="dlist", border=0)


def singleDownload():
    global link, path, downloadPATH, dirList, musicList

    # single download
    if gc.event == "tab1":
        try:
            path = popup_get_folder('Select a file to open', no_window=True) 
            downloadPATH = path + "/"
            gc.window["path"].update(downloadPATH)
            dirList = os.listdir(path)
            for i in dirList:
                if ".mp3" in i:
                    musicList.append(i)
            gc.window["pathList"].update(musicList)
        except TypeError:
            gc.GMessage(wmTitle="Warning", message="Choose Folder!")


    if gc.event == "Refresh Files":
        if path != "":
            musicList = []
            dirList = os.listdir(path)
            for i in dirList:
                if ".mp3" in i:
                    musicList.append(i)
            gc.window["pathList"].update(musicList)
        else:
            gc.GMessage(wmTitle="Warning!", message="path is empty no files here! -_- ")

    if gc.event == "Download":
        link = gc.GetValues["link"]
        if link != "" and path != "":
            try:
                gc.window["link"].update("")
                youtube = YouTube(link)
                audio = youtube.streams.filter(only_audio=Tree).first()

                Music = audio.download(path)
                mp3 = Music.strip(".mp4")
                subprocess.run(["ffmpeg", "-i", Music, f"{mp3}.mp3"]) # subprocess.run is list
                os.popen(f"rm {path}/*.mp4") # os.open string
                print(audio.download(path))
    
            except RegexMatchError:
                gc.GMessage(wmTitle="Warning!", message="no playlist support sorry ! -_- ")
        else:
            gc.GMessage(wmTitle="Warning!", message="Path or link is Empty ! -_- ")

def multiDownload():
    global path2, downloadList
    # multiple download
    if gc.event == "tab2":
        print("fack")
        try:
            path2 = popup_get_folder('Select a file to open', no_window=True) 
            downloadPATH = path2 + "/"
            gc.window["path2"].update(downloadPATH)

        except TypeError:
            gc.GMessage(wmTitle="Warning", message="Choose Folder!")

    if gc.event == "ADD":
        new = gc.GetValues["link2"]
        if new != "":
            if not str(new).startswith("https://www.youtube.com"):
                gc.GMessage("only youtube videos")
            else:
                downloadList.append(new)
                gc.window["dlist"].update(downloadList)
                gc.window["link2"].update("")
        else:
            gc.GMessage(wmTitle="Warning", message="Path is empty")
    
    if gc.event == "Remove":
        remove = str(gc.GetValues["dlist"]).lstrip("['").rstrip("']") # remove [' and ']
        print(remove)
        if remove in downloadList:
            downloadList.remove(remove)
            gc.window["dlist"].update(downloadList)
        else:
            gc.GMessage(wmTitle="Warning", message="Remove what?")

    if gc.event == "Download ALL":
        if path2 != "":
            for i in downloadList:
                youtube = YouTube(i)
                audio = youtube.streams.filter(only_audio=Tree).first()

                # convert mp4 to mp3 and remove mp4 file
                Music = audio.download(path2)
                mp3 = Music.strip(".mp4")
                subprocess.run(["ffmpeg", "-i", Music, f"{mp3}.mp3"]) # subprocess.run is list
                os.popen(f"rm {path2}/*.mp4") # os.open string

def update():
    # gnuchanos pages
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")

    singleDownload()
    multiDownload()

gc.update(GUpdate=update)

