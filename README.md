<p> this lgpl3+ 4.61.0.206 Unreleased version <br>
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
this is lgpl3+ 4.61.0.206 Unreleased version and this is hobby project not for money and i don't wanto bs license window to see
</p>


<p>

Finish Examples <br>
----------------------------------- <br>
Simple Timer -> Finish <br>
Simple Calculator -> Fimish <br>
Simple Text Editor -> Fimish <br>

Simple Program Runner Like Rofi -> Fimish <br>
Simple Video and Music Download from Youtube -> Fimish <br>
Simple Video to Sound # convert -> Fimish <br>
Simple Music Player -> Fimish <br>
Simple Wine Manager -> not Fimish??? <br>

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

<p>
GCanvas detaile
    if you press key program become fast this is not good for simple game there is no lock fps
    there is no easy multi key support like this if key.w and key.return: print()
    read keyboard evet is have to much delay
    i create simple render pipeline like system it just works you can reade _11:SimpleGame Example

    Music -> pygame mixer
    2D Render -> Canvas
</p>


```
from GnuChanGUI import *

class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS

        self.text = ""

        self.Layout = [
            [   self.GC.GMultiline(value="out", xStretch=True, yStretch=True, font="Sans, 20")   ],
            [   self.GC.GInput(value="in", xStretch=True, font="Sans, 20")   ]
        ]

        self.GC.GWindow(mainWindow=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        self.GC.update(GUpdate=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        _pressCheck = self.KYB.SingleKeyPressCheck(event=self.GC.event, key=self.KYB.Return)
        if _pressCheck: 
            self.text += self.GC.GetValues["in"] + "\n"
            self.GC.window["out"].update(self.text)
            self.GC.window["in"].update("")

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
```
