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

```


```
event, GetValues = default.window.read(timeout=60)

event ---> everythings is event like button click, keyboard, input, multiline,
key ---> Getvalues ı give you 1 example you can understan why ı change key name for GetValues

>gc is class name

gc = GnuChanGUI(Title="", Size=(250, 600), resizable=False, finalize=True)
Themecolors().GnuChanOS

event -> gc.GetEvent
window[] -> gc.GetWindow[].update()
value[]  -> gc.GetValues[]
key=""   -> SetValue=""

if gc.GetEvent == "Button":
    gc.window["Button"].update(gc.GetValues["ButtonNameChanger"])

window["button"].update(button_color = ("#9d4edd","#5a189a")) --> Change button color
window["button"].update(gc.window["text"].get())   --> text name change button name
```

```
# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import GKeyboard


# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()


class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        # main window layout you can use column and frame in here
        self.Layout = [
            
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)
        self.KYB = GKeyboard(window=self.GC)
        # Call Function Here




        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        pass

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    DefaultExample()
```
