"""Part 05 — GSlider ile GProgressBar guncelleme."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part05(GnuChanGUI):
    def __init__(self, Title="Part 05 — Slider + Progress", Size=(520, 220), resizable=False, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()

        self.Layout = [
            [self.GText(SetText="Slideri surukle; progress bar her karede guncellenir.", xStretch=True)],
            [self.GSlider(MaxRange=(0, 100), DefaultValue=30, SetValue="sl", xStretch=True)],
            [self.GProgressBar(MaxRange=100, SetValue="pro", xStretch=True)],
            [self.GText(SetText="0", SetValue="num", TPosition="c", xStretch=True)],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if not self.GetValues:
            return
        try:
            n = int(float(self.GetValues.get("sl", 0)))
        except (TypeError, ValueError):
            n = 0
        self.GetWindow["pro"].update(current_count=n)
        self.GetWindow["num"].update(str(n))

    def BeforeExit(self):
        print("Part 05 cikis")


if __name__ == "__main__":
    Part05()
