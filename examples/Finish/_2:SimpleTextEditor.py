"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
from threading import Thread



#Thread(target=DownloadVideo, args=[]).start()

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Text Editor!", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 12"
    Themecolors().GnuChanOS


    menu = [
        ["File", ["Open File", "Save File", "Save As File", "Close File"]],
        ["Settings", ["Show Settings", "Hide Settings"]],
        ["Help!", ["ShortCut"]]
            ]

    settingsWin = [
        [
            gc.GText(title="Text Size: ", EmptySpace=(0, 0), bcolor=GColors().purple7),
            gc.GSlider(value="fontSize", range=(5, 100), direction="h", xStretch=True, defaultValue=12, bcolor=GColors().purple6), 
        ],
        [
            gc.GText(title="Text Color 'Enter Color name': ", bcolor=GColors().purple7),
            gc.GInput(value="tcolor", xStretch=True, size=(30, None), bcolor=GColors().purple6),
        ],
        [
            gc.GText(title="Background Color 'Enter Color name': ", bcolor=GColors().purple7),
            gc.GInput(value="bcolor", xStretch=True, size=(30, None), bcolor=GColors().purple6),
        ],
        [ 
            gc.Push,
            gc.GButton(title="Save Settings"),
            gc.Push
        ]
    ]

    _textFont = 11

    win0 = [
        [ gc.GMultiline(value="text0", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text0_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]
    win1 = [
        [ gc.GMultiline(value="text1", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text1_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]
    win2 = [
        [ gc.GMultiline(value="text2", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text2_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]
    win3 = [
        [ gc.GMultiline(value="text3", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text3_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]
    win4 = [
        [ gc.GMultiline(value="text4", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text4_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]
    win5 = [
        [ gc.GMultiline(value="text5", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text5_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]
    win6 = [
        [ gc.GMultiline(value="text6", xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", noScroolBar=False, bcolor=GColors().purple8, border=2) ],
        [ gc.GText(title="File Path Here", value="text6_path", font=f"Sans, {str(_textFont)}", xStretch=True)]
    ]


    layout = [ 
        [gc.GMenuForTheme(menu, font="Sans, 15")],
        [gc.GTabGroup(TabGroupLayout=[
            [gc.GTab(title="window 0", TabLayout=win0, value="tab0")],
            [gc.GTab(title="window 1", TabLayout=win1, value="tab1")],
            [gc.GTab(title="window 2", TabLayout=win2, value="tab2")],
            [gc.GTab(title="window 3", TabLayout=win3, value="tab3")],
            [gc.GTab(title="window 4", TabLayout=win4, value="tab4")],
            [gc.GTab(title="window 5", TabLayout=win5, value="tab5")],
            [gc.GTab(title="window 6", TabLayout=win6, value="tab6")],
        ], value="tabG")],
        [ gc.GColumn(winColumn=settingsWin, xStretch=True, value="settings", bcolor=GColors().purple7) ],
    ]

    gc.GWindow(mainWindow=layout)

    gc.window["settings"].update(visible=False)
    gc.window["settings"].hide_row()

    _defaultTextValue = "text0"
    textList = ["text0", "text1", "text2", "text3", "text4", "text5", "text6"]
    for i in textList:
        gc.GMultilineTabSpace(gMultilineValue=i, gMultilineFont=f"Sans, {str(_textFont)}")
        gc.AddNewBorderWithColor(Value=i, Color=GnuChanOSColor().colors2, BorderSize=5)


    _tab0 = _tab1 = _tab2 = _tab3 = _tab4 = _tab5 = _tab6 = ""
    def update():
        global _defaultTextValue, _tab0, _tab1, _tab2, _tab3, _tab4, _tab5, _tab6

        ActiveTab = gc.GetValues["tabG"]
        _defaultTextValue = f"text{ActiveTab[len(ActiveTab)-1:]}"
        if gc.event == "Open File":
            try:
                if ActiveTab == "tab0":
                    _tab0 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text0_path"].update(_tab0)
                    with open(_tab0, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text0"].update(_GetText)
                elif ActiveTab == "tab1":
                    _tab1 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text1_path"].update(_tab1)
                    with open(_tab1, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text1"].update(_GetText)
                elif ActiveTab == "tab2":
                    _tab2 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text2_path"].update(_tab2)
                    with open(_tab2, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text2"].update(_GetText)
                elif ActiveTab == "tab3":
                    _tab3 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text3_path"].update(_tab3)
                    with open(_tab3, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text3"].update(_GetText)
                elif ActiveTab == "tab4":
                    _tab4 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text4_path"].update(_tab4)
                    with open(_tab4, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text4"].update(_GetText)
                elif ActiveTab == "tab5":
                    _tab5 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text5_path"].update(_tab5)
                    with open(_tab5, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text5"].update(_GetText)
                elif ActiveTab == "tab6":
                    _tab6 = popup_get_file('Select a file to open', no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    gc.window["text6_path"].update(_tab6)
                    with open(_tab6, 'r', encoding="utf-8") as _GetValue:
                        _GetText = _GetValue.read()
                        gc.window["text6"].update(_GetText)
            except Exception as ERR:
                print(ERR)


        elif gc.event == "Save File":
            try:
                if ActiveTab == "tab0":
                    _GetText = gc.GetValues["text0"]
                    with open(_tab0, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
                if ActiveTab == "tab1":
                    _GetText = gc.GetValues["text1"]
                    with open(_tab1, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
                if ActiveTab == "tab2":
                    _GetText = gc.GetValues["text2"]
                    with open(_tab2, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
                if ActiveTab == "tab3":
                    _GetText = gc.GetValues["text3"]
                    with open(_tab3, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
                if ActiveTab == "tab4":
                    _GetText = gc.GetValues["text4"]
                    with open(_tab4, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
                if ActiveTab == "tab5":
                    _GetText = gc.GetValues["text5"]
                    with open(_tab5, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
                if ActiveTab == "tab6":
                    _GetText = gc.GetValues["text6"]
                    with open(_tab6, 'w', encoding="utf-8") as _GetValue:
                            _GetValue.write(_GetText)
            except Exception as ERR:
                print(ERR)


        elif gc.event == "Save As File":
            try:
                if ActiveTab == "tab0":
                    _GetText = gc.GetValues["text0"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab0, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab0)
                if ActiveTab == "tab1":
                    _GetText = gc.GetValues["text1"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab1, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab1)
                if ActiveTab == "tab2":
                    _GetText = gc.GetValues["text2"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab2, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab2)
                if ActiveTab == "tab3":
                    _GetText = gc.GetValues["text3"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab3, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab3)
                if ActiveTab == "tab4":
                    _GetText = gc.GetValues["text4"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab4, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab4)
                if ActiveTab == "tab5":
                    _GetText = gc.GetValues["text5"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab5, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab5)
                if ActiveTab == "tab6":
                    _GetText = gc.GetValues["text6"]
                    _tab0 = popup_get_file('Select a file to open', save_as=True, no_window=True, default_path=os.path.expanduser("~"), keep_on_top=True, no_titlebar=True)
                    with open(_tab6, 'w', encoding="utf-8") as _GetValue:
                        _GetValue.write(_GetText)
                        gc.window["text0_path"].update(_tab6)
            except Exception as ERR:
                print(ERR)


        if gc.event == "Close File":
            gc.window[_defaultTextValue].update("")
            _defPath = f"text{ActiveTab[len(ActiveTab)-1:]}_path".strip("")
            gc.window[_defPath].update("File Path Here")

        ######### Settings #########
        if gc.event == "Save Settings":
            try:
                gc.FontSize_Change(windowValue=_defaultTextValue, fontSize=int(gc.GetValues["fontSize"]))
                if len(str(gc.GetValues["tcolor"]).strip(" ")) > 0:
                    gc.TextColor_Change(windowValue=_defaultTextValue, color=str(gc.GetValues["tcolor"]).strip(" "))
                if len(str(gc.GetValues["bcolor"]).strip(" ")) > 0:
                    gc.BackgroundColor_Change(windowValue=_defaultTextValue, color=str(gc.GetValues["bcolor"]).strip(" "))
            except Exception as ERR:
                gc.GMessage(wmTitle="Danger!", message=f"This is ERR{ERR}")
        elif gc.event == "Show Settings":
            gc.window["settings"].update(visible=True)
            gc.window["settings"].unhide_row()
        elif gc.event == "Hide Settings":
            gc.window["settings"].update(visible=False)
            gc.window["settings"].hide_row()
        elif gc.event == "F1:67":
            gc.window["settings"].update(visible=True)
            gc.window["settings"].unhide_row()
        elif gc.event == "F2:68":
            gc.window["settings"].update(visible=False)
            gc.window["settings"].hide_row()
        elif gc.event == "ShortCut":
            help = """
    f1 = hide settings
    f2 = show settings
            """
            gc.GMessage(wmTitle="Help!", message=help)
        ######### Settings ######### 



    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)


