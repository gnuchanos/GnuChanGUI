"""Push / Separator tutorial - demonstrates GPush, GHSep, GVSep.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class PushSepTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Push/Separator Tutorial', Size=(420,240), finalize=True)

        self.Layout = [
            [self.GText(SetText='Push and Separators', xStretch=True)],
            [self.GHSep()],
            [self.GText(SetText='Above Horizontal Separator', xStretch=True)],
            [self.GPush()],
            [self.GText(SetText='Below Push', xStretch=True)],
            [self.GVSep()],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        return

if __name__ == '__main__':
    PushSepTutorial()
