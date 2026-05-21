"""Sizegrip tutorial - demonstrates GSizegrip usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class SizegripTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Sizegrip Tutorial', Size=(420,200), finalize=True, resizable=True)

        self.Layout = [
            [self.GText(SetText='Sizegrip demo', xStretch=True, yStretch=True)],
            [self.GPush(), self.GSizegrip()]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if self.GetEvent == '__TIMEOUT__':
            return

if __name__ == '__main__':
    SizegripTutorial()
