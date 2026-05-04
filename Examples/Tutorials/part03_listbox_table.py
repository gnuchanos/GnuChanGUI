"""Part 03 — GListBox ve GTable."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part03(GnuChanGUI):
    def __init__(self, Title="Part 03 — Listbox + Table", Size=(640, 480), resizable=True, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()

        fruits = ["elma", "armut", "uzum", "kiraz"]
        rows = [
            ["Urun", "Adet", "Durum"],
            ["Elma", "12", "Stokta"],
            ["Armut", "5", "Stokta"],
            ["Uzum", "0", "Tukendi"],
        ]

        self.Layout = [
            [self.GText(SetText="Listbox (secim)", xStretch=True)],
            [self.GListBox(list=fruits, SetValue="lb", Size=(24, 6), xStretch=True, yStretch=True)],
            [self.GText(SetText="Tablo", xStretch=True)],
            [self.GTable(TableLists=rows, SetValue="tbl", VisibleRows=6, xStretch=True)],
            [self.GButton(Text="Secilenleri goster", SetValue="read")],
            [self.GMultiline(InText="", SetValue="log", xStretch=True, yStretch=True, ReadOnly=True, Size=(None, 8), TFont="Sans, 11")],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.GetEvent != "read" or not self.GetValues:
            return
        lb = self.GetValues.get("lb")
        tbl = self.GetValues.get("tbl")
        self.GetWindow["log"].update("Listbox secimi: {}\n\nTable secimi / deger: {}\n".format(lb, tbl))

    def BeforeExit(self):
        print("Part 03 cikis")


if __name__ == "__main__":
    Part03()
