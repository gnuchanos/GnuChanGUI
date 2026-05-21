"""Pane tutorial - demonstrates GPane usage (split panels).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class PaneTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Pane Tutorial', Size=(640,360), finalize=True)

        left = self.GColumn([[self.GText(SetText='Left panel', xStretch=True)]], xStretch=True, yStretch=True)
        right = self.GColumn([[self.GText(SetText='Right panel', xStretch=True)]], xStretch=True, yStretch=True)

        self.Layout = [
            [self.GText(SetText='Pane demo', TFont='Sans,14', xStretch=True)],
            [self.GPane(PaneColumns=[left, right], Orientation='horizontal', SetValue='pane', xStretch=True, yStretch=True, Size=(None,20))]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if self.GetEvent == '__TIMEOUT__':
            return

if __name__ == '__main__':
    PaneTutorial()
