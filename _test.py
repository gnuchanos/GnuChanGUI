import PySimpleGUI as sg

def main():
    layout = [
        [sg.Multiline(size=(60, 20), key='-TEXT-', autoscroll=True)],
        [sg.Button('Open'), sg.Button('Save'), sg.Button('Save As'), sg.Button('Exit')]
    ]

    window = sg.Window('Text Editor', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Open':
            filename = sg.popup_get_file('Select a file to open', no_window=True)
            if filename:
                with open(filename, 'r') as file:
                    content = file.read()
                    window['-TEXT-'].update(content)
        elif event == 'Save':
            filename = sg.popup_get_file('Select a file to save', save_as=True, no_window=True)
            if filename:
                with open(filename, 'w') as file:
                    content = values['-TEXT-']
                    file.write(content)
        elif event == 'Save As':
            filename = sg.popup_get_file('Select a file to save', save_as=True, no_window=True)
            if filename:
                with open(filename, 'w') as file:
                    content = values['-TEXT-']
                    file.write(content)
        window.refresh()

    window.close()

if __name__ == '__main__':
    main()