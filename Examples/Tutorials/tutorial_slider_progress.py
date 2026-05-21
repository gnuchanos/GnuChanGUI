"""Slider and ProgressBar tutorial - demonstrates interaction between slider and progress."""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class SliderProgressTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Slider & Progress', Size=(520,220), finalize=True)

        self.Layout = [
            [self.GText(SetText='Slider -> Progress demo', TFont='Sans,14', xStretch=True)],
            [self.GSlider(MaxRange=(0,100), DefaultValue=30, SetValue='s1', xStretch=True)],
            [self.GProgressBar(MaxRange=100, SetValue='p1', PDirection='h', xStretch=True)],
            [self.GButton(Text='Sync', SetValue='sync')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'sync':
            v = int(self.GetValues.get('s1', 0))
            self.GetWindow['p1'].update(v)

if __name__ == '__main__':
    SliderProgressTutorial()
