"""Part 04 — GCheackBox, GRadio, GSelection, GIncreaseSelection."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part04(GnuChanGUI):
    def __init__(self, Title="Part 04 — Checkbox / Radio / Combo / Spin", Size=(560, 520), resizable=True, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()

        self.Layout = [
            [self.GText(SetText="Checkbox", xStretch=True)],
            [
                self.GCheackBox(CText="Secenek A", SetValue="cb_a", Checked=False),
                self.GCheackBox(CText="Secenek B", SetValue="cb_b", Checked=True),
            ],
            [self.GText(SetText="Radio (aynı groupID)", xStretch=True)],
            [
                self.GRadio(RText="Mod 1", groupID="mode", SetValue="r1", defaultSelect=True),
                self.GRadio(RText="Mod 2", groupID="mode", SetValue="r2"),
            ],
            [self.GText(SetText="Combo (GSelection)", xStretch=True)],
            [self.GSelection(ListValues=["bir", "iki", "uc"], DefaultValue="iki", SetValue="combo", xStretch=True)],
            [self.GText(SetText="Spin (GIncreaseSelection)", xStretch=True)],
            [self.GIncreaseSelection(ListValues=[str(i) for i in range(1, 11)], StartValue="5", SetValue="spin", xStretch=True)],
            [self.GButton(Text="Ozetle", SetValue="sum")],
            [self.GMultiline(InText="", SetValue="out", xStretch=True, yStretch=True, ReadOnly=True, TFont="Sans, 11")],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        v = self.GetValues
        if self.GetEvent in ("r1", "r2"):
            self.GetWindow["out"].update("Radio olayi: {}\n".format(self.GetEvent))
            return
        if self.GetEvent != "sum" or not v:
            return
        lines = [
            "cb_a: {}".format(v.get("cb_a")),
            "cb_b: {}".format(v.get("cb_b")),
            "combo: {}".format(v.get("combo")),
            "spin: {}".format(v.get("spin")),
        ]
        self.GetWindow["out"].update("\n".join(lines))

    def BeforeExit(self):
        print("Part 04 cikis")


if __name__ == "__main__":
    Part04()
