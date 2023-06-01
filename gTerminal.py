from GnuChanGUI import *
import os


    

def main():
    default = GnuChanGUI(Title="GnuChan Program Runner", Size=(800,600), resizable=True)
    default.Theme()
    defaultFont = "Sans, 15"


    def execute_command(command):
        if command.startswith('cd '):
            directory = command[3:]
            try:
                os.chdir(directory)
                return f"Directory changed to: {os.getcwd()}"
            except FileNotFoundError:
                return f"Directory not found: {directory}"
        else:
            output = os.popen(command).read()
            return output


    term = [
        [default.GText("GnuChan Simple Terminal", font=defaultFont, xStretch=True, position="center")],
        [default.GLog(size=(80, 5), value="log", xStretch=True, yStretch=True)],
        [default.GInput(value='-COMMAND-', size=(60, 1), xStretch=True)]]

    gMenu = [
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
        ]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GColumn(winColumn=term, xStretch=True, yStretch=True)],
    ]

    default.GWindow(mainWindow=layout)

    def terminalAct():
        command = GetValues['-COMMAND-']
        output = execute_command(command)
        #print(f"$ {command}")
        print(output)
        default.window["-COMMAND-"].update("")

        if command == "clear":
            default.GWidgetUpdate(GWidgetValue="log", getValue="")


    while True:
        event, GetValues = default.window.read(timeout=24)
        if event == WIN_CLOSED or event == "Exit":
            break

        default.GKey(GetValues="-COMMAND-", key1="Return", event=event, Action=terminalAct)
            
                





    default.window.close()
if __name__ == "__main__":
    main()
