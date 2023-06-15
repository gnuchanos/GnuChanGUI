from GnuChanGUI import *
import os


    

def main():
    gc = GnuChanGUI(Title="GnuChan Program Runner", Size=(800,600), resizable=True)
    gc.Theme()
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
        [gc.GText("GnuChan Simple Terminal", font=defaultFont, xStretch=True, position="center")],
        [gc.GLog(size=(80, 5), value="log", xStretch=True, yStretch=True)],
        [gc.GInput(value='-COMMAND-', size=(60, 1), xStretch=True)]]

    gMenu = [
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
        ]

    layout = [
        [gc.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [gc.GColumn(winColumn=term, xStretch=True, yStretch=True)],
    ]

    gc.GWindow(mainWindow=layout)

    def terminalAct():
        command = gc.GetValues['-COMMAND-']
        output = execute_command(command)
        #print(f"$ {command}")
        print(output)
        gc.window["-COMMAND-"].update("")

        if command == "clear":
            gc.GWidgetUpdate(GWidgetValue="log", getValue="")


    def GQ():
        gc.GKey(GetValues="-COMMAND-", key1="Return", Action=terminalAct)

            
                
                    




    gc.update(GUpdate=GQ)
    gc.window.close()
if __name__ == "__main__":
    main()
