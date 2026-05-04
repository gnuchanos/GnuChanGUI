"""Part 01 — default.py ile ayni desen: pencere, metin, dugme, GHSep."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors, GMessage
    from GnuChanGUI import GKeyboard_Winows
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part01(GnuChanGUI):
    def __init__(self, Title="Part 01 — Text + Button", Size=(560, 260), resizable=False, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()
        self.Key_Windolf = GKeyboard_Winows()

        self.Layout = [
            [self.GText(SetText="Part 01: GText + GButton + GHSep", TPosition="c", xStretch=True, SetValue="info")],
            [self.GHSep(), self.GButton(Text="tikla", SetValue="click"), self.GHSep()],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, Borderless=False, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.GetEvent == "click":
            self.GetWindow["info"].update("Dugmeye basildi.")
        if self.CurrentKey == self.Enter:
            GMessage(WindowTitle="Part 01", WindowText="Enter")

    def BeforeExit(self):
        print("Part 01 cikis")


if __name__ == "__main__":
    Part01()
