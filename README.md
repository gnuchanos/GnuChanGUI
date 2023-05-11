# GnuChanGUI
<p> Please note that this is a library based on the PySimpleGUI library with the aim of simplifying and making it more user-friendly. Keep in mind that I am also a beginner in Python and constantly improving myself. </p>



example code

``` 

from GnuChanGUI import *

def main():
    default = GnuChanGUI(Title="GnuChan Simple Visual Novel Beta", Size=(510,600))
    default.Theme()

    layout = [
        [default.GText("test", value="text", font="Sans, 20", xStretch=True, position="center")],
        [default.GButton("button", font="Sans, 20", xStretch=True)]
    ]

    default.GWindow(mainWindow=layout)

    while True:
        event, GetValues = default.window.read()
        if event in (default.WINDOW_CLOSED, 'Exit'):
            break
        
        if event == "button":
            default.window["text"].update("uwu")


    default.window.close()
if __name__ == "__main__":
    main()

```

<p> You can also see the code samples on my GitHub page as an extra.</p>

```
install from source
git clone https://github.com/gnuchanos/GnuChanGUI
cd GnuChanGUI
python setup.py install
python setup.py build
```