"""Selection (Combobox) tutorial - single widget example."""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class SelectionTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Selection Tutorial', Size=(420,200), finalize=True)

        self.Layout = [
            [self.GText(SetText='Selection demo', TFont='Sans,14', xStretch=True)],
            [self.GSelection(ListValues=['Apple','Banana','Cherry'], DefaultValue='Banana', SetValue='sel')],
            [self.GButton(Text='Show', SetValue='show')],
            [self.GText(SetText='Choice:', SetValue='lbl_choice')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'show':
            self.GetWindow['lbl_choice'].update('Choice: ' + str(self.GetValues.get('sel')))

if __name__ == '__main__':
    SelectionTutorial()
