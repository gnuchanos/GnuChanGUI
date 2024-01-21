from GnuChanGUI import *
import webbrowser

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(300, 150), resizable=False)
Themecolors().GnuChanOS

gMenu = [ ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]], ["System", ["Exit"]] ]


timerStart = False
second = 59
minute = 59
hour = 0

layout = [
    [ gc.GMenuForTheme(winMenu=gMenu, font=gc.font) ],
    [ gc.Push, gc.GText(font="Sans, 35", value="timer"), gc.Push ],
    [ gc.GButton(title="Start", font="Sans, 20"), 
      gc.GButton(title="Stop", font="Sans, 20"), 
      gc.GButton(title="Clear", font="Sans, 20") ] ]

gc.GWindow(mainWindow=layout)

def timer():
    # gTimer Programs
    global timerStart, second, minute, hour
    if gc.event == "Start":
        if not timerStart:
            timerStart = True
    elif gc.event == "Stop":
        if timerStart:
            timerStart = False
    elif gc.event == "Clear":
        second = minute = hour = 0
        gc.window["timer"].update(f"{hour}:{minute}:{str(int(second))}")

    if timerStart:
        if second <= 60:
            second += gc.dt
        else:
            second = 0
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1

        gc.window["timer"].update(f"{hour}:{minute}:{str(int(second))}")


def update():
    # gnuchanos pages
    if gc.event == "GnuChanOS":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "Youtube Channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "Github Page":
        webbrowser.open("https://github.com/gnuchanos")

    # gnuchanos pages
    if gc.event == "gnuchanos":
        webbrowser.open("https://gnuchanos.github.io") 
    elif gc.event == "youtube channel":
        webbrowser.open("https://www.youtube.com/channel/ucmjtfic152myx7mbxmghfea")    
    elif gc.event == "github page":
        webbrowser.open("https://github.com/gnuchanos")

    timer()

gc.update(GUpdate=update)
