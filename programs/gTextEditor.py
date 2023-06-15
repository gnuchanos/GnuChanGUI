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
        [default.GMultiline(font=default.font, value="textFile", focus=True, xStretch=True, yStretch=True, border=0)],
        [default.GText(value="filepath", font=defaultFont, xStretch=True, position="center")]]

    default.GWindow(mainWindow=layout)

    default.GMultilineSpaceFixer(value="textFile")
    

    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            break

        xfile = FileSave(value="textFile", filepath="filepath", getValue=GetValues, window=default.window)
        if event == "Open Text File":
            xfile.Open
        elif event == "Save Text File":
            xfile.SaveAs
        




    default.window.close()
if __name__ == "__main__":
    main()