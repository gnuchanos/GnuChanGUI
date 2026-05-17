"""
Simple text editor — Ctrl+S / Ctrl+Shift+S / Ctrl+O Tk bind ile (pynput CurrentKey kombinasyonu desteklemez).
LGPL-3.0+ / hobby project
"""

import os

from GnuChanGUI import GnuChanGUI, GMessage
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors
from GnuChanGUI import threading
from GnuChanGUI.gcLibrary import IsKey_Hold, IsKey_Pressed

class SimpleTextEditor(GnuChanGUI):
    def __init__(
        self,
        Title="Simple Text Editor",
        Size=(1600, 900),
        resizable=False,
        finalize=True,
        winPosX=1920 / 2,
        winPosY=1080 / 2,
    ):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS
        self.C = GColors()
        self.CGC = GnuChanOSColor()
        self.TextFont = 11

        self._shortcut_save = False
        self._shortcut_save_as = False
        self._shortcut_open = False
        self._pending_show_settings = False
        self._pending_hide_settings = False

        self.menu = [
            ["File", ["Open File", "Save File", "Save As File", "Close File"]],
            ["Settings", ["Show Settings", "Hide Settings"]],
            ["Help!", ["ShortCut"]],
            ["Tab", ["Create Tab", "Remove Tab"]],
        ]

        self.settingsWin = [
            [
                self.GText(SetText="Text Size: ", EmptySpace=(0, 0), BColor=self.C.purple7),
                self.GSlider(
                    SetValue="fontSize",
                    MaxRange=(5, 100),
                    SDirection="h",
                    xStretch=True,
                    DefaultValue=12,
                    BColor=self.C.purple6,
                ),
            ],
            [
                self.GText(SetText="Text Color 'Enter Color name': ", BColor=self.C.purple7),
                self.GInput(SetValue="tcolor", xStretch=True, Size=(30, None), BColor=self.C.purple6),
            ],
            [
                self.GText(SetText="Background Color 'Enter Color name': ", BColor=self.C.purple7),
                self.GInput(SetValue="bcolor", xStretch=True, Size=(30, None), BColor=self.C.purple6),
            ],
            [
                self.GPush(self.C.purple7),
                self.GButton(Text="Save Settings"),
                self.GPush(self.C.purple7),
            ],
        ]

        def _CreateTab(n):
            return [
                [
                    self.GMultiline(
                        SetValue=f"text{n}",
                        xStretch=True,
                        yStretch=True,
                        TFont=f"Sans, {str(self.TextFont)}",
                        NoScroolBar=False,
                        BColor=self.C.purple8,
                    )
                ],
                [
                    self.GText(
                        SetText="File Path Here",
                        SetValue=f"text{n}_path",
                        TFont=f"Sans, {str(self.TextFont)}",
                        xStretch=True,
                    )
                ],
            ]



        # Index ile (0-based):
        # self.GRemoveTab('tabG', 0)          # İlk tabı sil

        # Key ile:
        # self.GRemoveTab('tabG', 'tab5')     # 'tab5' key'li tabı sil

        # Başlık ile:
        # self.GRemoveTab('tabG', 'TAB-5')    # 'TAB-5' başlıklı tabı sil


        self.Layout = [
            [self.GMenuForTheme(self.menu, TFont="Sans, 15", TColor=None, BColor=None)],
            [
                self.GTabGroup(
                    TabGroupLayout=[
                        [self.GTab(Text="TAB-0", TabLayout=_CreateTab(0), SetValue="tab0")]
                    ],
                    SetValue="tabG",
                    Border=0,
                )
            ],
            [
                self.GColumn(
                    winColumnLayout_List=self.settingsWin,
                    xStretch=True,
                    SetValue="settings",
                    BColor=GColors().purple7,
                )
            ],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)

        

        self.GetWindow["settings"].update(visible=False)
        self.GetWindow["settings"].hide_row()

        # for i in ("text0", "text1", "text2", "text3", "text4", "text5", "text6"):
        #     self.GMultilineTabSpace(WindowValue=i, TFont=f"Sans, {str(self.TextFont)}")
        #     self.GBorder(WindowValue=i, Border=5, Color=self.CGC.FColors5)


        for i in range(1, 5):
            self.GAddTab("tabG", f"TAB-{i}", _CreateTab(i))



        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)



    def _action_open_file(self):
        ActiveTab = self.GetValues["tabG"]
        suf = ActiveTab[-1]
        try:
            _FilePath = self.GetFilePath(defaultPATH=os.path.expanduser("~"))
            self.GetWindow[f"text{suf}_path"].update(_FilePath)
            with open(_FilePath, "r", encoding="utf-8") as Value:
                self.GetWindow[f"text{suf}"].update(Value.read())
        except Exception as ERR:
            print(ERR)

    def _action_save_file(self):
        ActiveTab = self.GetValues["tabG"]
        suf = ActiveTab[-1]
        try:
            _GetText = self.GetValues[f"text{suf}"]
            _ThisPath = self.GetGTextValue(f"text{suf}_path")
            if not _ThisPath or _ThisPath == "File Path Here":
                GMessage(WindowTitle="Kaydet", WindowText="Once dosya yolu secin veya Save As kullanin.")
                return

            with open(_ThisPath, "w", encoding="utf-8") as _Value:
                _Value.write(_GetText)
        except Exception as ERR:
            print(ERR)

    def _action_save_as_file(self):
        ActiveTab = self.GetValues["tabG"]
        suf = ActiveTab[-1]
        try:
            _GetText = self.GetValues[f"text{suf}"]
            _ThisPath = self.GetFileForSave(defaultPATH=os.path.expanduser("~"))
            with open(_ThisPath, "w", encoding="utf-8") as _GetValue:
                _GetValue.write(_GetText)
                self.GetWindow[f"text{suf}_path"].update(_ThisPath)

        except Exception as ERR:
            print(ERR)

    def Update(self):

        if IsKey_Hold(self.W):
            print("W is being held down")
        
        if IsKey_Pressed(self.S):
            print("S was just pressed")
        else:
            print("S is not currently pressed")

        if self._shortcut_open:
            self._shortcut_open = False
            self._action_open_file()

        if self._shortcut_save:
            self._shortcut_save = False
            self._action_save_file()

        if self._shortcut_save_as:
            self._shortcut_save_as = False
            self._action_save_as_file()

        if self._pending_show_settings:
            self._pending_show_settings = False
            self.GetWindow["settings"].update(visible=True)
            self.GetWindow["settings"].unhide_row()

        if self._pending_hide_settings:
            self._pending_hide_settings = False
            self.GetWindow["settings"].update(visible=False)
            self.GetWindow["settings"].hide_row()

        ActiveTab = self.GetValues["tabG"]
        suf = ActiveTab[-1]
        _defaultTextValue = f"text{suf}"

        if self.GetEvent == "Open File":
            self._action_open_file()

        elif self.GetEvent == "Save File":
            self._action_save_file()

        elif self.GetEvent == "Save As File":
            self._action_save_as_file()

        if self.GetEvent == "Close File":
            self.GetWindow[_defaultTextValue].update("")
            self.GetWindow[f"text{suf}_path"].update("File Path Here")

        if self.GetEvent == "Remove Tab":
            pass
        elif self.GetEvent == "Create Tab":
            pass

        if self.GetEvent == "Save Settings":
            self.FontSize_Change(WindowValue=_defaultTextValue, FontSize=int(self.GetValues["fontSize"]))
            try:
                if len(str(self.GetValues["tcolor"]).strip(" ")) > 0:
                    self.TextColor_Change(
                        WindowValue=_defaultTextValue,
                        Color=str(self.GetValues["tcolor"]).strip(" "),
                    )
                if len(str(self.GetValues["bcolor"]).strip(" ")) > 0:
                    self.BackgroundColor_Change(
                        WindowValue=_defaultTextValue,
                        Color=str(self.GetValues["bcolor"]).strip(" "),
                    )
            except Exception as ERR:
                GMessage(WindowTitle="DANGER!!!", WindowText=str(ERR))

            print(self.GetValues["tcolor"])
            print(self.GetValues["bcolor"])
            print(_defaultTextValue)

        elif self.GetEvent == "Show Settings":
            self.GetWindow["settings"].update(visible=True)
            self.GetWindow["settings"].unhide_row()
        elif self.GetEvent == "Hide Settings":
            self.GetWindow["settings"].update(visible=False)
            self.GetWindow["settings"].hide_row()

        elif self.GetEvent == "ShortCut":
            help_txt = """
Ctrl+S       = Save File (aktif sekme)
Ctrl+Shift+S = Save As
Ctrl+O       = Open File
F1           = Show settings (Tk)
F2           = Hide settings (Tk)

Not: pynput ile CurrentKey tek tus icindir; kombinasyonlar Tk bind ile cozulur.
            """
            GMessage(WindowTitle="Kisayollar", WindowText=help_txt.strip())

    def BeforeExit(self):
        print("Exit")


if __name__ == "__main__":
    threading.Thread(target=SimpleTextEditor, args=[]).start()
