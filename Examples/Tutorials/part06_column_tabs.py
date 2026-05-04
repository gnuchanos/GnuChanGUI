"""Part 06 — GColumn ve GTabGroup / GTab."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part06(GnuChanGUI):
    def __init__(self, Title="Part 06 — Column + Tabs", Size=(640, 440), resizable=True, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.C = GColors()
        self.CGC = GnuChanOSColor()

        col_left = self.GColumn(
            winColumnLayout_List=[
                [self.GText(SetText="Sol kolon", BColor=self.C.blue5, xStretch=True, TPosition="c")],
                [self.GButton(Text="Sol dugme", SetValue="btnL")],
            ],
            SetValue="colL",
            xStretch=True,
            yStretch=True,
            BColor=self.C.blue5,
        )
        col_right = self.GColumn(
            winColumnLayout_List=[
                [self.GText(SetText="Sag kolon", BColor=self.C.green5, xStretch=True, TPosition="c")],
                [self.GButton(Text="Sag dugme", SetValue="btnR")],
            ],
            SetValue="colR",
            xStretch=True,
            yStretch=True,
            BColor=self.C.green5,
        )

        tab_a = [[self.GText(SetText="Sekme A icerigi", SetValue="ta", xStretch=True, TPosition="c", BColor=self.C.yellow3)]]
        tab_b = [[self.GText(SetText="Sekme B icerigi", SetValue="tb", xStretch=True, TPosition="c", BColor=self.C.pink1)]]

        tabs = self.GTabGroup(
            TabGroupLayout=[
                [self.GTab(Text="Alpha", TabLayout=tab_a, SetValue="tabA")],
                [self.GTab(Text="Beta", TabLayout=tab_b, SetValue="tabB")],
            ],
            SetValue="tabs",
            size=(600, 200),
        )

        self.Layout = [
            [self.GText(SetText="Ust: iki GColumn yan yana", xStretch=True)],
            [col_left, col_right],
            [tabs],
            [self.GText(SetText="Olaylar burada", SetValue="status", xStretch=True)],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        ev = self.GetEvent
        if ev in ("btnL", "btnR"):
            self.GetWindow["status"].update("Tiklanan: {}".format(ev))
        if ev in ("tabA", "tabB"):
            self.GetWindow["status"].update("Sekme olayi: {}".format(ev))

    def BeforeExit(self):
        print("Part 06 cikis")


if __name__ == "__main__":
    Part06()
