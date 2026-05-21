"""Font tutorial - demonstrates GFont usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class FontTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Font Tutorial', Size=(420,200), finalize=True)

        gf = gc.GFont()
        try:
            f = gf.BuildFont('Sans', 14)
        except Exception:
            f = 'Sans, 14'

        self.Layout = [
            [self.GText(SetText='Font demo', xStretch=True)],
            [self.GText(SetText=f'Sample text with font {f}', TFont=f, xStretch=True)],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        return

if __name__ == '__main__':
    FontTutorial()
