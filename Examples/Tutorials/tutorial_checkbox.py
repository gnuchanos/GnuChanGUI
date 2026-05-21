"""Checkbox tutorial - demonstrates toggling and reading checkbox state."""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class CheckboxTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Checkbox Tutorial', Size=(420,220), finalize=True)

        self.Layout = [
            [self.GText(SetText='Checkbox demo', TFont='Sans,14', xStretch=True)],
            [[self.GCheackBox(CText='Option A', SetValue='chkA'), self.GCheackBox(CText='Option B', SetValue='chkB')]],
            [self.GButton(Text='Show states', SetValue='show')],
            [self.GText(SetText='States:', SetValue='lbl_states')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'show':
            a = self.GetValues.get('chkA', False)
            b = self.GetValues.get('chkB', False)
            self.GetWindow['lbl_states'].update(f'States: A={a}, B={b}')

if __name__ == '__main__':
    CheckboxTutorial()
