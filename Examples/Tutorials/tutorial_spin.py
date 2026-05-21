"""Spin / IncreaseSelection tutorial - demonstrates GIncreaseSelection (Spin).
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class SpinTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Spin Tutorial', Size=(360,180), finalize=True)

        self.Layout = [
            [self.GText(SetText='Spin demo', xStretch=True)],
            [self.GIncreaseSelection(ListValues=[1,2,3,4,5], StartValue=2, SetValue='spin')],
            [self.GButton(Text='Show', SetValue='show')],
            [self.GText(SetText='Value:', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'show':
            self.GetWindow['lbl'].update('Value: ' + str(self.GetValues.get('spin')))

if __name__ == '__main__':
    SpinTutorial()
