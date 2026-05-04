"""Part 07 — GMenu, GStatusBar, GButtonMenu (ust menu + durum cubugu + menu dugmesi)."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part07(GnuChanGUI):
    def __init__(self, Title="Part 07 — Menu + StatusBar", Size=(560, 320), resizable=True, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()

        menubar = [
            ["Dosya", ["Durum yaz::stat", "---", "Cik"]],
            ["Yardim", ["Hakkinda"]],
        ]
        bmenu_def = ["Islemler", ["Kopyala", "Temizle", "---", "Cikis"]]

        self.Layout = [
            [self.GMenu(WinMENU_List=menubar)],
            [self.GText(SetText="Menu: Dosya/Yardim; asagida ButtonMenu.", xStretch=True, SetValue="hint")],
            [self.GButtonMenu("Islemler", bmenu_def, SetValue="bmenu")],
            [self.GText(SetText="", SetValue="main", xStretch=True, yStretch=True, TPosition="c")],
            [self.GStatusBar(SetText="Hazir", SetValue="sb", xStretch=True)],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        ev = self.GetEvent
        if ev in ("Cik", "Cikis"):
            self.closeWindow = True
            return
        if ev == "Hakkinda":
            self.GetWindow["main"].update("Yardim: GnuChanGUI Tutorial Part 07")
            self.GetWindow["sb"].update("Menu: Hakkinda")
            return
        if ev == "stat":
            self.GetWindow["sb"].update("Durum: stat secildi")
            return
        if ev in ("Kopyala", "Temizle"):
            self.GetWindow["main"].update("ButtonMenu: {}".format(ev))
            self.GetWindow["sb"].update(ev)

    def BeforeExit(self):
        print("Part 07 cikis")


if __name__ == "__main__":
    Part07()
