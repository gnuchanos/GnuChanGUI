"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, os, Thread, GMessage
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors


# Extra Lib


#Thread(target=DownloadVideo, args=[]).start()
class SimpleTextEditor:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors
        self.TextFont = 11


        self.menu = [
            ["File", ["Open File", "Save File", "Save As File", "Close File"]],
            ["Settings", ["Show Settings", "Hide Settings"]],
            ["Help!", ["ShortCut"]],
            ["Tab",   ["Create Tab", "Remove Tab"]]
        ]


        self.settingsWin = [
            [
                self.GC.GText(SetText="Text Size: ", EmptySpace=(0, 0), BColor=self.C.purple7),
                self.GC.GSlider(SetValue="fontSize", MaxRange=(5, 100), SDirection="h", xStretch=True, DefaultValue=12, BColor=self.C.purple6), 
            ],
            [
                self.GC.GText(SetText="Text Color 'Enter Color name': ", BColor=self.C.purple7),
                self.GC.GInput(SetValue="tcolor", xStretch=True, Size=(30, None), BColor=self.C.purple6),
            ],
            [
                self.GC.GText(SetText="Background Color 'Enter Color name': ", BColor=self.C.purple7),
                self.GC.GInput(SetValue="BColor", xStretch=True, Size=(30, None), BColor=self.C.purple6),
            ],
            [ 
                self.GC.GPush(self.C.purple7),
                self.GC.GButton(Text="Save Settings"),
                self.GC.GPush(self.C.purple7)
            ]
        ]

        self.settingsWin = [
            [
                self.GC.GText(SetText="Text Size: ", EmptySpace=(0, 0), BColor=self.C.purple7),
                self.GC.GSlider(SetValue="fontSize", MaxRange=(5, 100), SDirection="h", xStretch=True, DefaultValue=12, BColor=self.C.purple6), 
            ],
            [
                self.GC.GText(SetText="Text Color 'Enter Color name': ", BColor=self.C.purple7),
                self.GC.GInput(SetValue="tcolor", xStretch=True, Size=(30, None), BColor=self.C.purple6),
            ],
            [
                self.GC.GText(SetText="Background Color 'Enter Color name': ", BColor=self.C.purple7),
                self.GC.GInput(SetValue="bcolor", xStretch=True, Size=(30, None), BColor=self.C.purple6),
            ],
            [ 
                self.GC.GPush(self.C.purple7),
                self.GC.GButton(Text="Save Settings"),
                self.GC.GPush(self.C.purple7)
            ]
        ]

        self.win0 = [
                [ self.GC.GMultiline(SetValue="text0", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8, Border=2) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text0_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]
        self.win1 = [
                [ self.GC.GMultiline(SetValue="text1", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8, Border=2) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text1_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]
        self.win2 = [
                [ self.GC.GMultiline(SetValue="text2", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text2_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]
        self.win3 = [
                [ self.GC.GMultiline(SetValue="text3", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text3_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]
        self.win4 = [
                [ self.GC.GMultiline(SetValue="text4", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text4_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]
        self.win5 = [
                [ self.GC.GMultiline(SetValue="text5", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text5_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]
        self.win6 = [
                [ self.GC.GMultiline(SetValue="text6", xStretch=True, yStretch=True, TFont=f"Sans, {str(self.TextFont)}", 
                                NoScroolBar=False, BColor=self.C.purple8) 
                ],
                [ self.GC.GText(SetText="File Path Here", SetValue="text6_path", TFont=f"Sans, {str(self.TextFont)}", xStretch=True)]
            ]

        self.Layout = [ 
            [self.GC.GMenuForTheme(self.menu, TFont="Sans, 15", TColor=None, BColor=None)],
            [self.GC.GTabGroup(TabGroupLayout=[
                [self.GC.GTab(Text="TAB-0", TabLayout=self.win0, SetValue="tab0")],
                [self.GC.GTab(Text="TAB-1", TabLayout=self.win1, SetValue="tab1")],
                [self.GC.GTab(Text="TAB-2", TabLayout=self.win2, SetValue="tab2")],
                [self.GC.GTab(Text="TAB-3", TabLayout=self.win3, SetValue="tab3")],
                [self.GC.GTab(Text="TAB-4", TabLayout=self.win4, SetValue="tab4")],
                [self.GC.GTab(Text="TAB-5", TabLayout=self.win5, SetValue="tab5")],
                [self.GC.GTab(Text="TAB-6", TabLayout=self.win6, SetValue="tab6")],
            ], SetValue="tabG", Border=0)],
            [ self.GC.GColumn(winColumnLayout_List=self.settingsWin, xStretch=True, SetValue="settings", BColor=GColors().purple7) ],
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)


        # Call Function Here


        self.GC.GetWindow["settings"].update(visible=False)
        self.GC.GetWindow["settings"].hide_row()

        for i in ("text0", "text1", "text2", "text3", "text4", "text5", "text6"):
            self.GC.GMultilineTabSpace(WindowValue=i, TFont=f"Sans, {str(self.TextFont)}")
            self.GC.AddNewBorderWithColor(WindowValue=i, Color=self.CGC.FColors5, BorderSize=5)

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects
        
        ActiveTab = self.GC.GetValues["tabG"]
        _defaultTextValue = f"text{ActiveTab[len(ActiveTab)-1:]}"
        if self.GC.GetEvent == "Open File":
            try:
                _FilePath = self.GC.GetFilePath(defaultPATH=os.path.expanduser("~"))
                self.GC.GetWindow[f"text{ActiveTab[-1]}_path"].update(_FilePath)
                with open(_FilePath, 'r', encoding="utf-8") as Value:
                    _ThisText = Value.read()
                    self.GC.GetWindow[f"text{ActiveTab[-1]}"].update(_ThisText)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Save File":
            try:
                _GetText = self.GC.GetValues[f"text{ActiveTab[-1]}"]
                _ThisPath = self.GC.GetGTextValue(f"text{ActiveTab[-1]}_path")
                with open(_ThisPath, 'w', encoding="utf-8") as _Value:
                    _Value.write(_GetText)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Save As File":
            try:
                _GetText = self.GC.GetValues[f"text{ActiveTab[-1]}"]
                _ThisPath = self.GC.GetFileForSave(defaultPATH=os.path.expanduser("~"))
                with open(_ThisPath, 'w', encoding="utf-8") as _GetValue:
                    _GetValue.write(_GetText)
                    self.GC.GetWindow[f"text{ActiveTab[-1]}_path"].update(_ThisPath)
            except Exception as ERR:
                print(ERR)

        if self.GC.GetEvent == "Close File":
            self.GC.GetWindow[_defaultTextValue].update("")
            _defPath = f"text{ActiveTab[len(ActiveTab)-1:]}_path".strip("")
            self.GC.GetWindow[_defPath].update("File Path Here")

        if self.GC.GetEvent == "Remove Tab":
            pass
        elif self.GC.GetEvent == "Create Tab":
            pass

        ######### Settings #########
        if self.GC.GetEvent == "Save Settings":
            self.GC.FontSize_Change(WindowValue=_defaultTextValue, FontSize=int(self.GC.GetValues["fontSize"]))
            if len(str(self.GC.GetValues["tcolor"]).strip(" ")) > 0:
                self.GC.TextColor_Change(WindowValue=_defaultTextValue, Color=str(self.GC.GetValues["tcolor"]).strip(" "))
            if len(str(self.GC.GetValues["bcolor"]).strip(" ")) > 0:
                self.GC.BackgroundColor_Change(WindowValue=_defaultTextValue, Color=str(self.GC.GetValues["bcolor"]).strip(" "))
            self.GC.GMessage(wmTitle="Danger!", Text=f"This is ERR")
            print(self.GC.GetValues["tcolor"])
            print(self.GC.GetValues["bcolor"])
            print(_defaultTextValue)

        # Press Button For This
        elif self.GC.GetEvent == "Show Settings":
            self.GC.GetWindow["settings"].update(visible=True)
            self.GC.GetWindow["settings"].unhide_row()
        elif self.GC.GetEvent == "Hide Settings":
            self.GC.GetWindow["settings"].update(visible=False)
            self.GC.GetWindow["settings"].hide_row()
        
        # Press Key For This
        elif self.GC.f1 in self.GC.CurrentKey:
            self.GC.GetWindow["settings"].update(visible=True)
            self.GC.GetWindow["settings"].unhide_row()
        elif self.GC.f2 in self.GC.CurrentKey:
            self.GC.GetWindow["settings"].update(visible=False)
            self.GC.GetWindow["settings"].hide_row()
        
        # Press Key For Help!
        elif self.GC.GetEvent == "ShortCut":
            help = """
    f1 = hide settings
    f2 = show settings
            """
            GMessage(WindowText="Help!", Text=help)
        ######### Settings ######### 

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleTextEditor()
