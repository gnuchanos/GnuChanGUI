"""Radio buttons tutorial - demonstrates radio group selection."""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class RadioTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Radio Tutorial', Size=(420,220), finalize=True)

        self.Layout = [
            [self.GText(SetText='Radio demo', TFont='Sans,14', xStretch=True)],
            [[self.GRadio(RText='One', groupID='RAD', SetValue='r1'), self.GRadio(RText='Two', groupID='RAD', SetValue='r2'), self.GRadio(RText='Three', groupID='RAD', SetValue='r3')]],
            [self.GButton(Text='Which selected?', SetValue='which')],
            [self.GText(SetText='Selected:', SetValue='lbl_sel')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'which':
            sel = 'None'
            if self.GetValues.get('r1'):
                sel = 'One'
            elif self.GetValues.get('r2'):
                sel = 'Two'
            elif self.GetValues.get('r3'):
                sel = 'Three'
            self.GetWindow['lbl_sel'].update(f'Selected: {sel}')

if __name__ == '__main__':
    RadioTutorial()
