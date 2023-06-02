# GnuChanGUI
<p> Please note that this is a library based on the PySimpleGUI library with the aim of simplifying and making it more user-friendly. Keep in mind that I am also a beginner in Python and constantly improving myself. </p>
 
important note
```
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
```


```
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
```

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




example 1 simple Timer
 ```
from GnuChanGUI import *

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
]

gc.GWindow(mainWindow=layout)

second = 0
timerStart = False


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

example 2 basic input change text (press button or press enter)
```
from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GText(value="text", font=gc.font, xStretch=True, position="center")],
    [gc.GInput(value="textInput", font=gc.font, xStretch=True)],
    [gc.GButton("change text", font=gc.font, xStretch=True)],
]

gc.GWindow(mainWindow=layout)

def inputEnter():
    gc.window["text"].update(gc.GetValues["textInput"])

def GQ():
    if gc.event == "change text":
        gc.window["text"].update(gc.GetValues["textInput"])
    
    gc.GKey(Action=inputEnter, GetValues="textInput", key1="Return")


    
gc.update(GUpdate=GQ)
gc.window.close()
```


example 3 basic listbox
```
from GnuChanGUI import *

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]


testList = []

layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GListBox(list=testList, value="glist", font=gc.font, xStretch=True, yStretch=True, noScroolBar=True)],
    [gc.GButton("Add List", value="addList", font=gc.font, xStretch=True)],
]

gc.GWindow(mainWindow=layout)
gc.GListBoxFixer(border=0, value="glist")
def GQ():
    if gc.event == "addList":
        for i in range(1, 10):
            testList.append(i)
        gc.window["glist"].update(testList)
    
gc.update(GUpdate=GQ)
gc.window.close()
```


example 4 basic multiline random number 
```
from GnuChanGUI import *
import random

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]


testList = ""
layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GMultiline(value="glist", font=gc.font, xStretch=True, yStretch=True, noScroolBar=True)],
    [gc.GButton("Add List", value="addList", font=gc.font, xStretch=True)],
]

gc.GWindow(mainWindow=layout)

def GQ():
    global testList
    if gc.event == "addList":
        testList += str(random.randint(0, 50)) + "\n"
        gc.window["glist"].update(testList)
    
gc.update(GUpdate=GQ)
gc.window.close()

```



example 4 basic GCheack example
```
from GnuChanGUI import *
import random

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]


testList = ""
layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GText(value="hlGame", font=gc.font, xStretch=True, position="center")],
    [gc.GCheack(title="Dead island", value="game1", font=gc.font),
     gc.GCheack(title="Half Life 2", value="game2", font=gc.font),
     gc.GCheack(title="Summerset Saga", value="game3", font=gc.font)],
    [gc.GButton("show checkbox", value="checkbox", font=gc.font, xStretch=True)],
]

gc.GWindow(mainWindow=layout)

def GQ():
    global testList
    if gc.event == "checkbox":
        if gc.GetValues["game1"]:
            print("Dead Island - Good Game")
        if gc.GetValues["game2"]:
            print("Half Life 2 - is COOL GAME")
        if gc.GetValues["gam3"]:
            print("SummerSet Saga is game")
            


gc.update(GUpdate=GQ)
gc.window.close()
````





example 5 basic GRadio example
```
from GnuChanGUI import *
import random

gc = GnuChanGUI(Title="GnuChan Program Timer", Size=(1024, 600), resizable=False)
gc.Theme()

gMenu = [
    ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
    ["System", ["Exit"]]
]


testList = ""
layout = [
    [gc.GMenuForTheme(winMenu=gMenu, font=gc.font)],
    [gc.GText(value="hlGame", font=gc.font, xStretch=True)],
    [gc.GRadio(title="half life 1", groupID="halflife", value="hl1", font=gc.font),
     gc.GRadio(title="half life 2", groupID="halflife", value="hl2", font=gc.font),
     gc.GRadio(title="half life 3", groupID="halflife", value="hl3", font=gc.font)],
    [gc.GButton("Add List", value="addList", font=gc.font, xStretch=True)],
]

gc.GWindow(mainWindow=layout)

def GQ():
    global testList
    if gc.event in ["hl1", "hl2", "hl3"]:
        if gc.event == "hl1":
            gc.window["hlGame"].update("can you play half life 1 before ?")
        elif gc.event == "hl2":
            gc.window["hlGame"].update("half life 2 good game")
        elif gc.event == "hl3":
            gc.window["hlGame"].update("there is no half life 3 :(")


gc.update(GUpdate=GQ)
gc.window.close()
````
