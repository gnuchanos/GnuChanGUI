"""Part 02 — GInput, GMultiline, GetValues ile okuma."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part02(GnuChanGUI):
    def __init__(self, Title="Part 02 — Input + Multiline", Size=(520, 420), resizable=True, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()

        self.Layout = [
            [self.GText(SetText="Tek satir:", SetValue="lbl1")],
            [self.GInput(InText="Buraya yaz...", SetValue="single", xStretch=True)],
            [self.GText(SetText="Cok satir:", SetValue="lbl2")],
            [self.GMultiline(InText="Satir 1\nSatir 2", SetValue="multi", xStretch=True, yStretch=True, Size=(None, 12), TFont="Sans, 12")],
            [self.GButton(Text="Degerleri status satirina yaz", SetValue="go")],
            [self.GText(SetText="", SetValue="out", xStretch=True, TPosition="l")],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.GetEvent != "go" or not self.GetValues:
            return
        single = self.GetValues.get("single", "")
        multi = self.GetValues.get("multi", "")
        self.GetWindow["out"].update("Input: {}\n\nMultiline:\n{}".format(single, multi))

    def BeforeExit(self):
        print("Part 02 cikis")


if __name__ == "__main__":
    Part02()
