"""Part 08 — GCanvas: BeginScene2D ile basit cizim (tam oyun icin pong ornegine bak)."""
try:
    from GnuChanGUI import GnuChanGUI, GnuChanOSColor, GColors, Themecolors
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil.") from e


class Part08(GnuChanGUI):
    def __init__(self, Title="Part 08 — GCanvas Scene2D", Size=(640, 420), resizable=True, finalize=True, winPosX=960, winPosY=540):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)
        Themecolors().GnuChanOS
        self.CGC = GnuChanOSColor()
        GColors()

        self.Layout = [
            [self.GText(SetText="GCanvas + BeginScene2D (her frame yeniden cizilir)", xStretch=True)],
            [self.GCanvas(SetValue="cv", Size=(600, 300), xStretch=True, yStretch=True, BColor="#111")],
        ]
        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit, TimeOUT=50)

    def Update(self):
        cv = self.GetWindow["cv"]
        w, h = 600, 300
        try:
            with cv.BeginScene2D():
                cv.DrawRectangle("bg", 0, 0, w, h, fill="#1a1a2e", outline="")
                cv.DrawRectangle("bar", 40, 120, w - 80, 24, fill="#16213e", outline="#4ecca3")
                cv.DrawText("t1", 40, 60, "Part 08 — DrawText / DrawRectangle", fill="#eeeeee", font=("Segoe UI", 14))
                cv.DrawText("t2", 40, 200, "Detay: Examples/33-gcanvas-pong-example/pong.py", fill="#aaaaaa", font=("Segoe UI", 11))
        except Exception as ex:
            print("Canvas cizim hatasi:", ex)

    def BeforeExit(self):
        print("Part 08 cikis")


if __name__ == "__main__":
    Part08()
