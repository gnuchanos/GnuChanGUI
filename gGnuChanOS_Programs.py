from GnuChanGUI import *
import subprocess


def main():
    default = GnuChanGUI(Title="GnuChan Program Runner", Size=(610,600), resizable=False)
    default.Theme()

    defaultFont = "Sans, 20"

    gnuchanProgramList = [" gRunner : Simple Dmenu Like Program", 
                          " gCalculator : Simple Calculator A+B=C", 
                          " gTimer : Simple Timer Program"]
    
    gMenu = [["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
             ["System", ["Exit"]]]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GText(title="This is Simple Program Runner", font=defaultFont, position="center", xStretch=True)],
        [default.GListBox(list=list(gnuchanProgramList), font=defaultFont, xStretch=True, yStretch=True, value="prunner", position="center", noScroolBar=True)],
        [default.GButton("Run", xStretch=True, font=defaultFont)]
    ]

    default.GWindow(mainWindow=layout)
    default.GListBoxFixer(value="prunner", border=0)

    while True:
        event, GetValues = default.window.read()
        if event == WIN_CLOSED:
            break
        

        oldVar = str(GetValues["prunner"])[2:]
        newVar = oldVar.split(":")[0].strip()


        if event == "Run":
            subprocess.Popen(f"python {newVar}" + ".py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            break

    default.window.close()
if __name__ == "__main__":
    main()



"""
xdsl numarası

"""