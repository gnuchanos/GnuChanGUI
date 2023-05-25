# GnuChanGUI
<p> Please note that this is a library based on the PySimpleGUI library with the aim of simplifying and making it more user-friendly. Keep in mind that I am also a beginner in Python and constantly improving myself. </p>



example code

``` 

from GnuChanGUI import *


def main():
    default = GnuChanGUI(Title="GnuChan Program Runner", Size=(950,600), resizable=True)
    default.Theme()
    defaultFont = "Sans, 15"


    gMenu = [
        ["Log File", ["Open Text File", "Save Text File"]],
        ["System", ["Exit"]]
    ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font=defaultFont)],
        
    ]

    default.GWindow(mainWindow=layout)

    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            break
    default.window.close()

if __name__ == "__main__":
    main()

```
