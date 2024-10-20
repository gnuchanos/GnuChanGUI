"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
import termcolor
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
            gc.GText(SetText="Text Size: ", EmptySpace=(0, 0), BColor=GColors().purple7),
            gc.GSlider(WindowValue="fontSize", MaxRange=(5, 100), SDirection="h", xStretch=True, DefaultValue=12, BColor=GColors().purple6), 
        ],
        [
            gc.GText(SetText="Text Color 'Enter Color name': ", BColor=GColors().purple7),
            gc.GInput(WindowValue="tcolor", xStretch=True, Size=(30, None), BColor=GColors().purple6),
        ],
        [
            gc.GText(SetText="Background Color 'Enter Color name': ", BColor=GColors().purple7),
            gc.GInput(WindowValue="BColor", xStretch=True, Size=(30, None), BColor=GColors().purple6),
        ],
        [ 
            gc.GPush(GColors().purple7),
            gc.GButton(Text="Save Settings"),
            gc.GPush(GColors().purple7)
        ]
    ]



    win0 = [
            [ gc.GMultiline(WindowValue="text0", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text0_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]
    win1 = [
            [ gc.GMultiline(WindowValue="text1", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text1_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]
    win2 = [
            [ gc.GMultiline(WindowValue="text2", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text2_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]
    win3 = [
            [ gc.GMultiline(WindowValue="text3", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text3_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]
    win4 = [
            [ gc.GMultiline(WindowValue="text4", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text4_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]
    win5 = [
            [ gc.GMultiline(WindowValue="text5", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text5_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]
    win6 = [
            [ gc.GMultiline(WindowValue="text6", xStretch=True, yStretch=True, TFont=f"Sans, {str(_textFont)}", 
                            NoScroolBar=False, BColor=GColors().purple8, Border=2) 
            ],
            [ gc.GText(SetText="File Path Here", TextValue="text6_path", TFont=f"Sans, {str(_textFont)}", xStretch=True)]
        ]

    layout = [ 
        [gc.GMenuForTheme(menu, TFont="Sans, 15")],
        [gc.GTabGroup(TabGroupLayout=[
            [gc.GTab(Text="TAB-0", TabLayout=win0, WindowValue="tab0")],
            [gc.GTab(Text="TAB-1", TabLayout=win1, WindowValue="tab1")],
            [gc.GTab(Text="TAB-2", TabLayout=win2, WindowValue="tab2")],
            [gc.GTab(Text="TAB-3", TabLayout=win3, WindowValue="tab3")],
            [gc.GTab(Text="TAB-4", TabLayout=win4, WindowValue="tab4")],
            [gc.GTab(Text="TAB-5", TabLayout=win5, WindowValue="tab5")],
            [gc.GTab(Text="TAB-6", TabLayout=win6, WindowValue="tab6")],
        ], WindowValue="tabG", Border=1)],
        [ gc.GColumn(winColumnLayout_List=settingsWin, xStretch=True, SetWindowValue="settings", BColor=GColors().purple7) ],
    ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    
    gc.GetWindow["settings"].update(visible=False)
    gc.GetWindow["settings"].hide_row()

    for i in ("text0", "text1", "text2", "text3", "text4", "text5", "text6"):
        gc.GMultilineTabSpace(WindowValue=i, TFont=f"Sans, {str(_textFont)}")
        gc.AddNewBorderWithColor(WindowValue=i, Color=GnuChanOSColor().colors2, BorderSize=5)

    def update():
        global _defaultTextValue 
        
        ActiveTab = gc.GetValues["tabG"]
        _defaultTextValue = f"text{ActiveTab[len(ActiveTab)-1:]}"
        if gc.GetEvent == "Open File":
            try:
                _FilePath = gc.GetFilePath(defaultPATH=os.path.expanduser("~"))
                gc.GetWindow[f"text{ActiveTab[-1]}_path"].update(_FilePath)
                with open(_FilePath, 'r', encoding="utf-8") as Value:
                    _ThisText = Value.read()
                    gc.GetWindow[f"text{ActiveTab[-1]}"].update(_ThisText)
            except Exception as ERR:
                print(ERR)

        elif gc.GetEvent == "Save File":
            try:
                _GetText = gc.GetValues[f"text{ActiveTab[-1]}"]
                _ThisPath = gc.GetGTextValue(f"text{ActiveTab[-1]}_path")
                with open(_ThisPath, 'w', encoding="utf-8") as _Value:
                    _Value.write(_GetText)
            except Exception as ERR:
                print(ERR)

        elif gc.GetEvent == "Save As File":
            try:
                _GetText = gc.GetValues[f"text{ActiveTab[-1]}"]
                _ThisPath = gc.GetFileForSave(defaultPATH=os.path.expanduser("~"))
                with open(_ThisPath, 'w', encoding="utf-8") as _GetValue:
                    _GetValue.write(_GetText)
                    gc.GetWindow[f"text{ActiveTab[-1]}_path"].update(_ThisPath)
            except Exception as ERR:
                print(ERR)

        if gc.GetEvent == "Close File":
            gc.GetWindow[_defaultTextValue].update("")
            _defPath = f"text{ActiveTab[len(ActiveTab)-1:]}_path".strip("")
            gc.GetWindow[_defPath].update("File Path Here")

        if gc.GetEvent == "Remove Tab":
            pass
        elif gc.GetEvent == "Create Tab":
            pass

        ######### Settings #########
        if gc.GetEvent == "Save Settings":
            try:
                gc.FontSize_Change(windowValue=_defaultTextValue, fontSize=int(gc.GetValues["fontSize"]))
                if len(str(gc.GetValues["tcolor"]).strip(" ")) > 0:
                    gc.TextColor_Change(windowValue=_defaultTextValue, color=str(gc.GetValues["tcolor"]).strip(" "))
                if len(str(gc.GetValues["bcolor"]).strip(" ")) > 0:
                    gc.BackgroundColor_Change(windowValue=_defaultTextValue, color=str(gc.GetValues["bcolor"]).strip(" "))
            except Exception as ERR:
                gc.GMessage(wmTitle="Danger!", message=f"This is ERR{ERR}")

        # Press Button For This
        elif gc.GetEvent == "Show Settings":
            gc.GetWindow["settings"].update(visible=True)
            gc.GetWindow["settings"].unhide_row()
        elif gc.GetEvent == "Hide Settings":
            gc.GetWindow["settings"].update(visible=False)
            gc.GetWindow["settings"].hide_row()
        
        # Press Key For This
        elif gc.GetEvent == "F1:67":
            gc.GetWindow["settings"].update(visible=True)
            gc.GetWindow["settings"].unhide_row()
        elif gc.GetEvent == "F2:68":
            gc.GetWindow["settings"].update(visible=False)
            gc.GetWindow["settings"].hide_row()
        
        # Press Key For Help!
        elif gc.GetEvent == "ShortCut":
            help = """
    f1 = hide settings
    f2 = show settings
            """
            gc.GMessage(wmTitle="Help!", message=help)
        ######### Settings ######### 

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)


