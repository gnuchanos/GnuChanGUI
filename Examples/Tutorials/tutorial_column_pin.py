"""Column and visibility tutorial - demonstrates GColumn, GPin, GVisible, and GPush.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ColumnPinTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Column / Pin / Visibility', Size=(560,320), finalize=True)

        self.left = self.GColumn([[self.GText(SetText='Left panel', xStretch=True), self.GButton(Text='Hide Right', SetValue='hide_right')]], xStretch=True, yStretch=True)
        self.right = self.GColumn([[self.GText(SetText='Right panel', xStretch=True), self.GButton(Text='Show Right', SetValue='show_right')]], xStretch=True, yStretch=True)

        self.button_frame = self.GFrame(
            InsideWindowLayout=[
                [self.GButton(Text='Pin Left', SetValue='pin_left'), self.GButton(Text='Pin Right', SetValue='pin_right')],
                [self.GPush(), self.GHSep(), self.GVSep()]
            ],
            SetValue='options', xStretch=True, yStretch=False, Border=1
        )

        self.Layout = [
            [self.GText(SetText='Column + Pin + Visibility demo', TFont='Sans,14', xStretch=True)],
            [self.left, self.right],
            [self.button_frame],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'hide_right':
            self.GVisible('options', False)
        if self.GetEvent == 'show_right':
            self.GVisible('options', True)
        if self.GetEvent == 'pin_left':
            self.GPin(self.left)
            gc.GMessage(WindowTitle='Pinned', WindowText='Left column pinned.')
        if self.GetEvent == 'pin_right':
            self.GPin(self.right)
            gc.GMessage(WindowTitle='Pinned', WindowText='Right column pinned.')

if __name__ == '__main__':
    ColumnPinTutorial()
