# GnuChanGUI
<p> Please note that this is a library based on the PySimpleGUI library with the aim of simplifying and making it more user-friendly. Keep in mind that I am also a beginner in Python and constantly improving myself. </p>
 
important note
"""
python -m PySimpleGUI.PySimpleGUI upgrade
position | left - center - right

font -> font
visible -> visible
readonly -> readonly and  disabled -> readonly
no_scrollbar -> noScroolBar
group_id -> groupID
default_value -> defaultValue

expand_x --> xStretch
expand_y --> yStretch
justification -> position
text_color -> tColor
background_color -> bColor
border_width -> border
image_filename -> bImage
password_char -> PwChars
"""


"""
event, GetValues = default.window.read(timeout=60)

event ---> everythings is event like button click, keyboard, input, multiline,
key ---> Getvalues ı give you 1 example you can understan why ı change key name for GetValues

>gc is class name
> input value
[gc.GInput(value="ButtonNameChanger")],
> I give a value to the button because if the button name changes, the button's click event won't work
[gc.GButton("Test Button", value="Button")] 
> write button name --> value="ButtonNameChanger" -> gc.window["Button"].update(gc.GetValues["ButtonNameChanger"])

if gc.event == "Button":
    gc.window["Button"].update(gc.GetValues["ButtonNameChanger"])

window["button"].update(button_color = ("#9d4edd","#5a189a")) --> Change button color
window["button"].update(gc.window["text"].get())   --> text name change button name
"""

example code

``` 

from GnuChanGUI import GnuChanGUI
import time

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GText(value="text", font=gc.font, xStretch=True, position="center")],
    [gc.GButton("Start Timer", font=gc.font, xStretch=True),
     gc.GButton("Stop Timer", font=gc.font, xStretch=True)],
    [gc.GMultiline(value="test")]
]

gc.GWindow(mainWindow=layout)

second = 0
timerStart = False


gc.window["text"].bind('<Shift>', ' Shift')



def GQ():
    global second, timerStart

    if gc.event == "Start Timer":
        timerStart = True
    elif gc.event == "Stop Timer":
        timerStart = False

    if timerStart == True:
        second += 1 * gc.dt
        gc.window["text"].update(str(second))
    else:
        pass

    

gc.update(GUpdate=GQ)

gc.window.close()


```




small example for widgets

 ```
 not finish yet
 ```
