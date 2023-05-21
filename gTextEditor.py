from GnuChanGUI import *

def main():
    default = GnuChanGUI(Title="GnuChan Program Runner", Size=(800,600), resizable=True)
    default.Theme()
    defaultFont = "Sans, 15"



    gMenu = [
        ["Log File", ["Open Text File", "Save Text File"]],
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
        ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GMultiline(font=defaultFont, value="textFile", focus=True, xStretch=True, yStretch=True, border=0)],
        [default.GText(value="filepath", font=defaultFont, xStretch=True, position="center")]]

    default.GWindow(mainWindow=layout)


    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            break
        if event == "Open Text File":
            default.Open(value="textFile", filepath="filepath")
        elif event == "Save Text File":
            default.SaveAs(getValue=GetValues, value="textFile", filepath="filepath")

    default.window.close()


    default.window.close()
if __name__ == "__main__":
    main()