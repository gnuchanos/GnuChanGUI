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

Simple Game -> 1 level demo finish but have keyboard delay :@

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



# simple virtual environment
python -m venv .gcVENV
source .gcVENV/bin/activate
pip install .

```


```
gc.GetEvent:  = everythings is event like button click, keyboard, input, multiline,
gc.GetValues[] = return value in 
gc.GetWindow[].update() = update everything in window
         


new keyboard event example
self.d == self.CurrentKey # this is hold 

# sorry but i don't like windows or mac this is only for gnu/linux if you you windows or mac use old
from GnuChanGUI import GKeyboard as GK

if self.GetEvent == GK().w:
    print("this is old keyboard event i can't remove in source kod right now")




self.num2 == self.CurrentKey

>gc is class name



# text
GText    -> SetText
GButton  -> Text
GListBox -> list
GInput   -> InText
GMultiline -> InText
GCheackBox -> CText
GRadio     -> RText


if "Button" == gc.GetEvent:
    gc.GetWindow["Button"].update(gc.GetValues["ButtonNameChanger"])

GetWindow["button"].update(button_color = ("#9d4edd","#5a189a")) --> Change button color
GetWindow["button"].update(gc.GetWindow["text"].get())   --> text name change button name
```



```

"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, GTime
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GMessage
from GnuChanGUI import GKeyboard_Winows as GK_Windolf

# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample(GnuChanGUI):
    def __init__(self, Title="Defaul Title", Size=(600, 300), resizable=False, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # old keyboard event
        self.Key_Windolf = GK_Windolf()


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text")],
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text2")],
            [self.GText(SetText="text", TPosition='c', xStretch=True, yStretch=True, SetValue="text3")],
            [
                self.GHSep(),
                self.GButton(Text="button", SetValue="click"),
                self.GHSep()
            ]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        # Call Function Here

        # update window/getvalue

        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GetEvent == "event" -> window event
        #self.GetWindow["text"].update("this text") -> update window objects

        # keyboard example
        if self.CurrentKey == self.Enter:
            GMessage(WindowTitle="old version keyboard event", WindowText="message YEY")

        # keyboard example WINDOLF
        if self.CurrentKey == self.Key_Windolf.NumpadAdd:
            GMessage(WindowTitle="old version keyboard event", WindowText="message YEY")


        print(self.CurrentKey, " : ", self.Key_Windolf.NumpadAdd)

      
        # button and change text example
        if "click" == self.GetEvent:
            self.GetWindow["text"].update("button pressed")


    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()


```
