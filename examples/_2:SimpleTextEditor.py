"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
#Thread(target=DownloadVideo, args=[]).start()

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Text Editor!", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 12"
    Themecolors().GnuChanOS
    _textFont = 11


    menu = [
        ["File", ["Open File", "Save File", "Save As File", "Close File"]],
        ["Settings", ["Show Settings", "Hide Settings"]],
        ["Help!", ["ShortCut"]],
        ["Tab",   ["Create Tab", "Remove Tab"]]
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

    def TextWindow(gMultilineValue, TextValue):
        return [
            [ gc.GMultiline(value=gMultilineValue, xStretch=True, yStretch=True, font=f"Sans, {str(_textFont)}", 
                            noScroolBar=False, bcolor=GColors().purple8, border=2) 
            ],
            [ gc.GText(title="File Path Here", value=TextValue, font=f"Sans, {str(_textFont)}", xStretch=True)]
        ]

    win0 = TextWindow(gMultilineValue=f"text0", TextValue=f"text0_path")
    win1 = TextWindow(gMultilineValue=f"text1", TextValue=f"text1_path")
    win2 = TextWindow(gMultilineValue=f"text2", TextValue=f"text2_path")
    win3 = TextWindow(gMultilineValue=f"text3", TextValue=f"text3_path")
    win4 = TextWindow(gMultilineValue=f"text4", TextValue=f"text4_path")
    win5 = TextWindow(gMultilineValue=f"text5", TextValue=f"text5_path")
    win6 = TextWindow(gMultilineValue=f"text6", TextValue=f"text6_path")

    defaultWin = [win1, win2, win3, win4, win5, win6]
    _WinIndex = 0

    layout = [ 
        [gc.GMenuForTheme(menu, font="Sans, 15")],
        [gc.GTabGroup(TabGroupLayout=[
            [gc.GTab(title="TAB-0", TabLayout=win0, value="tab0")],
        ], value="tabG")],
        [ gc.GColumn(winColumn=settingsWin, xStretch=True, value="settings", bcolor=GColors().purple7) ],
    ]

    gc.GWindow(mainWindow=layout)
    
    _index = 0
    _TabIndex = 1
    for i in defaultWin:
        gc.window["tabG"].add_tab(gc.GTab(title=f"TAB-{_TabIndex}", TabLayout=defaultWin[_index], value=f"tab{_index}"))
        _index += 1
        _TabIndex += 1

    gc.window["settings"].update(visible=False)
    gc.window["settings"].hide_row()

    for i in ("text0", "text1", "text2", "text3", "text4", "text5", "text6"):
        gc.GMultilineTabSpace(gMultilineValue=i, gMultilineFont=f"Sans, {str(_textFont)}")
        gc.AddNewBorderWithColor(Value=i, Color=GnuChanOSColor().colors2, BorderSize=5)

    def update():
        global _defaultTextValue 
        
        ActiveTab = gc.GetValues["tabG"]
        _defaultTextValue = f"text{ActiveTab[len(ActiveTab)-1:]}"
        if gc.event == "Open File":
            try:
                _FilePath = gc.GetFilePath(defaultPATH=os.path.expanduser("~"))
                gc.window[f"text{ActiveTab[-1]}_path"].update(_FilePath)
                with open(_FilePath, 'r', encoding="utf-8") as Value:
                    _ThisText = Value.read()
                    gc.window[f"text{ActiveTab[-1]}"].update(_ThisText)
            except Exception as ERR:
                print(ERR)

        elif gc.event == "Save File":
            try:
                _GetText = gc.GetValues[f"text{ActiveTab[-1]}"]
                _ThisPath = gc.GetGTextValue(f"text{ActiveTab[-1]}_path")
                with open(_ThisPath, 'w', encoding="utf-8") as _Value:
                    _Value.write(_GetText)
            except Exception as ERR:
                print(ERR)

        elif gc.event == "Save As File":
            try:
                _GetText = gc.GetValues[f"text{ActiveTab[-1]}"]
                _ThisPath = gc.GetFileForSave(defaultPATH=os.path.expanduser("~"))
                with open(_ThisPath, 'w', encoding="utf-8") as _GetValue:
                    _GetValue.write(_GetText)
                    gc.window[f"text{ActiveTab[-1]}_path"].update(_ThisPath)
            except Exception as ERR:
                print(ERR)

        if gc.event == "Close File":
            gc.window[_defaultTextValue].update("")
            _defPath = f"text{ActiveTab[len(ActiveTab)-1:]}_path".strip("")
            gc.window[_defPath].update("File Path Here")

        if gc.event == "Remove Tab":
            pass
        elif gc.event == "Create Tab":
            pass

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

        # Press Button For This
        elif gc.event == "Show Settings":
            gc.window["settings"].update(visible=True)
            gc.window["settings"].unhide_row()
        elif gc.event == "Hide Settings":
            gc.window["settings"].update(visible=False)
            gc.window["settings"].hide_row()
        
        # Press Key For This
        elif gc.event == "F1:67":
            gc.window["settings"].update(visible=True)
            gc.window["settings"].unhide_row()
        elif gc.event == "F2:68":
            gc.window["settings"].update(visible=False)
            gc.window["settings"].hide_row()
        
        # Press Key For Help!
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


