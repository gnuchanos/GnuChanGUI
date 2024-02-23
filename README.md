# GnuChanGUI

<p> this lgpl3+ 4.61.0.206 Unreleased version <br>
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
this is lgpl3+ 4.61.0.206 Unreleased version and this is hobby project not for money and i don't wanto bs license window to see
</p>

<p> Please note that this library with the aim of simplifying and making it more user-friendly. Keep in mind that I am also a beginner in Python and i still learning! </p>

important note
```
how you can install gnuchangui

first install 
pip install git+https://github.com/gnuchanos/gnuchangui

second install
1: download project .zip
2: extrack zip
3: cd gnuchangui
4: pip install .

font -> font
visible -> visible
readonly -> readonly and  disabled -> readonly
no_scrollbar -> noScroolBar
group_id -> groupID
default_value -> defaultValue

expand_x --> xStretch
expand_y --> yStretch
justification -> position > left,center,right
text_color -> tColor
background_color -> bColor
border_width -> border > border size
image_filename -> bImage
password_char -> PwChars > 123 > ***
```


```
event, GetValues = default.window.read(timeout=60)

event ---> everythings is event like button click, keyboard, input, multiline,
key ---> Getvalues ı give you 1 example you can understan why ı change key name for GetValues

>gc is class name

gc = GnuChanGUI(Title="", Size=(250, 600), resizable=False, finalize=True)
Themecolors().GnuChanOS

event -> gc.event
window[] -> gc.window[].update()
value[]  -> gc.getvalue[]
key=""   -> value=""

if gc.event == "Button":
    gc.window["Button"].update(gc.GetValues["ButtonNameChanger"])

window["button"].update(button_color = ("#9d4edd","#5a189a")) --> Change button color
window["button"].update(gc.window["text"].get())   --> text name change button name
```

example code

``` 

from GnuChanGUI import *

if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(250, 600), resizable=False, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ [gc.GText(value="text", xStretch=True, position="center")],
               [gc.GInput(value="user_input", xStretch=True)],
               [gc.GButton(title="change text", font="Sans, 20", xStretch=True)],
               [gc.GListBox(value="listbox", xStretch=True, yStretch=True, position="center")]
               ]

    gc.GWindow(mainWindow=layout)

    listboxList = []
    def update():
        global listboxList

        if gc.event == "change text":
            gc.window["text"].update(gc.GetValues["user_input"])
            gc.window["user_input"].update("")

            listboxList.append(gc.GetValues["user_input"])
            gc.window["listbox"].update(listboxList)


    gc.update(GUpdate=update)


```


little examples
```
GFrame example
    test1 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]
    test2 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]
    test3 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]
    test4 = [[default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
             [default.GText("test", xStretch=True, position="center")]]

    layout = [
        [default.GFrame(winLayout=test1, value="test1", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues()),
         default.GFrame(winLayout=test2, value="test2", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues())],
        [default.GFrame(winLayout=test3, value="test3", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues()),
         default.GFrame(winLayout=test4, value="test4", xStretch=True, yStretch=True, bColor=GColors(colors=1).blues())]]

    default.GWindow(mainWindow=layout)
   
   
   
   GColumn example 
    TopLayer = [[default.GText(title="Top Layer", position="center", font="Sans, 20", bColor=GColors(colors=1).blues(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]
    MiddleLeftLayer = [[default.GText(title="Middle Left", position="center", font="Sans, 20",bColor=GColors(colors=1).greens(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]
    MiddleRightLayer = [[default.GText(title="Middle Right", position="center", font="Sans, 20", bColor=GColors(colors=1).purples(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]
    BottomLayer = [[default.GText(title="Bottom Layer", position="center", font="Sans, 20", bColor=GColors(colors=5).blues(), xStretch=True, yStretch=True, EmptySpace=(0,0))]]

    layout = [
        [default.GColumn(TopLayer, xStretch=True, yStretch=True)],
        [default.GColumn(MiddleLeftLayer, xStretch=True, yStretch=True), 
         default.GColumn(MiddleRightLayer, xStretch=True, yStretch=True)],
        [default.GColumn(BottomLayer, xStretch=True, yStretch=True)] ]



tab and GTabGroup example
    tab1 = [[default.GText(title="tab1", font=defaultFont, bColor="black", xStretch=True)]]
    tab2 = [[default.GText(title="tab2", font=defaultFont, bColor="black", xStretch=True)]]
    layout = [
        [default.GTabGroup( TabGroupLayout=[[
            default.GTab(title="tab1", TabLayout=tab1),
            default.GTab(title="tab2", TabLayout=tab2),
            
            ]] )]
    ],
    
    
click event for button
    if gc.event == "button name or value": click event
        gc.window["text"].update(gc.GetValues["textInput"])
  

image change
if gc.event == "imgButton":
        gc.window["img"].update("logo2.png")


glistbox
if gc.event == "addList":
        for i in range(1, 10):
            testList.append(i)
        gc.window["glist"].update(testList)

ginput event 
if gc.event == "change text": # change text is button
        gc.window["text"].update(gc.GetValues["textInput"]) #text input value
   

checkbox example
if gc.event == "checkbox":
        if gc.GetValues["hl1"]:
            print("half life 1")
        if gc.GetValues["hl2"]:
            print("half life 2")
        if gc.GetValues["hl3"]:
            print("half life 3 ?????")
            
Radio example groupID=hlGames <-- this is important
    if gc.event in ["hl1", "hl2", "hl3"]:
        if gc.event == "hl1":
            gc.window["hlGame"].update("can you play half life 1 before ?")
        elif gc.event == "hl2":
            gc.window["hlGame"].update("half life 2 good game")
        elif gc.event == "hl3":
            gc.window["hlGame"].update("there is no half life 3 :(")
```





full script examples
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



example 5 basic GCheack example
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





example 6 basic GRadio example
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

example 7 simple image change example
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
    [gc.Push, gc.GImage(image="logo1.png", value="img"), gc.Push],
    [gc.GButton("change image", value="imgButton", font=gc.font, xStretch=True)],
]

gc.GWindow(mainWindow=layout)

def inputEnter():
    gc.window["img"].update("logo2.png")

def GQ():
    if gc.event == "imgButton":
        gc.window["img"].update("logo2.png")
    
gc.update(GUpdate=GQ)
gc.window.close()

```

selections examples
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
    
    [gc.GButton("value button", font=gc.font, xStretch=True)],

    [gc.GSelection(values=[1,2,3,4,5], value="GSelection", defaultValue=1, font=gc.font, xStretch=True)],
    
    [gc.GIncreaseSelection(startValue=1, rangeValue=[1,2,3,4,5], value="GIncreaseSelection", font=gc.font, xStretch=True)],
    
    [gc.GSlider(direction="v", font=gc.font, range=(1,100), defaultValue=1, value="GSlider1"),
     gc.GSlider(direction="h", font=gc.font, range=(1,100), defaultValue=1, value="GSlider2")],
    
    [gc.GProgressBar(direction="h", MaxValue=100, value="health"),
     gc.GProgressBar(direction="v", MaxValue=100, value="stamina")],
]

gc.GWindow(mainWindow=layout)
gc.GSelectionFixer(value="GSelection")

def GQ():
    if gc.event == "value button":
        if gc.GetValues["GSelection"]:
            print(gc.GetValues["GSelection"])
        if gc.GetValues["GIncreaseSelection"]:
            print(gc.GetValues["GIncreaseSelection"])


        if gc.GetValues["GSlider1"]:
            gc.window["health"].update(gc.GetValues["GSlider1"])
        if gc.GetValues["GSlider2"]:
            gc.window["stamina"].update(gc.GetValues["GSlider2"])
   

gc.update(GUpdate=GQ)
gc.window.close()

```

