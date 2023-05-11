import GnuChanGUI as gc
import os, subprocess

def get_filtered_programs():
    program_list = os.listdir('/usr/bin')
    programList = [{"name": "blender", "info": "3D"},
                    {"name": "godot", "info": "Game Engine"},
                    {"name": "qutebrowser", "info": "Browser"},
                    {"name": "firefox", "info": "Browser"},
                    {"name": "kdenlive", "info": "Video Editor"},
                    {"name": "zathura", "info": "Pdf Reader"},
                    {"name": "gimp", "info": "2d Editor"},
                    {"name": "arandr", "info": "xrandr GUI"},
                    {"name": "steam", "info": "More Games"},
                    {"name": "lutris", "info": "Game Software"},
                    {"name": "protontricks", "info": "Proton Settings"},
                    {"name": "lxappearance", "info": "System Theme"}]

    filtered_list = [program["name"] + " : " + program["info"] for program in programList if program["name"] in program_list]
    return filtered_list

def main():
    default = gc.GnuChanGUI(Title="GnuChan Program Runner", Size=(650,600), resizable=True)
    default.Theme()

    logWindow = [
        [default.GText(title="you must select program bro!", font="Sans, 20", position="center", xStretch=True)],
        [default.GButton(title="Close Warning", font="Sans, 20", xStretch=True)]
    ]

    layout = [[default.GText("|  SELECT PROGRAM |", font="Sans, 20", position="center", xStretch=True)],
              [default.GListBox(list=get_filtered_programs(), value='-LIST-', font="Sans, 20", position="center", xStretch=True, yStretch=True, noScroolBar=True)],
              [default.hsep()],
              [default.GText("Input:> ", font="Sans, 20"),
               default.GInput(font="Sans, 20", value="runSoft", size=(30,1), xStretch=True)],
              [default.GButton("RUN Input", value="runInput", font="sans, 20", xStretch=True),
               default.GButton('RUN', value="RUN", font="Sans, 20", xStretch=True)],
              [default.GColumn(winColumn=logWindow, value="logWarning", xStretch=True, visible=False)]]

    default.GWindow(mainWindow=layout)
    default.GListBoxFixer(value="-LIST-", border=0)

    while True:
        event, GetValues = default.window.read()
        if event in 'Exit':
            break

        if event == "RUN":
            try:
                selected_program = GetValues['-LIST-'][0].split(':')[0]
                subprocess.Popen(selected_program, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                default.window.close()
                break
            except IndexError:
                default.window["logWarning"].update(visible=True)

        if event == "runInput":
            software = GetValues["runSoft"]
            if software == "":
                default.window["logWarning"].update(visible=True)
            else:
                subprocess.Popen(software, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(software)
                default.window.close()
                break
            
        if event == "Close Warning":
            default.window["logWarning"].update(visible=False)


    default.window.close()
if __name__ == "__main__":
    main()