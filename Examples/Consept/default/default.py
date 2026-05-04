"""
GnuChanGUI — temel pencere sablonu (butun Tutorial ornekleri bununla ayni yapiyi kullanir).

Parcali ogrenme: ../Tutorials/INDEX.txt
LGPL-3.0+ / hobby project
"""

try:
    from GnuChanGUI import GnuChanGUI, os, Thread, GTime
    from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GMessage
    from GnuChanGUI import GKeyboard_Winows
except ImportError as e:
    raise ImportError("GnuChanGUI yuklu degil (pip install / PYTHONPATH).") from e


class DefaultExample(GnuChanGUI):
    """Minimal: GText + GButton + GHSep, SetUpdate dongusu, BeforeExit."""

    def __init__(
        self,
        Title="Default Title",
        Size=(600, 300),
        resizable=False,
        finalize=True,
        winPosX=1920 / 2,
        winPosY=1080 / 2,
    ):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS
        self.C = GColors()
        self.CGC = GnuChanOSColor()
        self.Key_Windolf = GKeyboard_Winows()

        self.Layout = [
            [self.GText(SetText="text", TPosition="c", xStretch=True, yStretch=True, SetValue="text")],
            [
                self.GHSep(),
                self.GButton(Text="button", SetValue="click"),
                self.GHSep(),
            ],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout, Borderless=False, KeepOnTop=False)
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.CurrentKey == self.Enter:
            GMessage(WindowTitle="Klavye", WindowText="Enter (eski CurrentKey)")

        if self.CurrentKey == self.Key_Windolf.NumpadAdd:
            GMessage(WindowTitle="Klavye", WindowText="Numpad + (GKeyboard_Winows)")

        if self.GetEvent == "click":
            self.GetWindow["text"].update("button pressed")

    def BeforeExit(self):
        print("Exit")


if __name__ == "__main__":
    DefaultExample()
