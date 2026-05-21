"""ListBox tutorial - demonstrates listbox selection.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class ListboxTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='ListBox Tutorial', Size=(360,260), finalize=True)

        items = ['Apple','Banana','Cherry','Date','Elderberry']
        self.Layout = [
            [self.GText(SetText='ListBox demo', TFont='Sans,14', xStretch=True)],
            [self.GListBox(list=items, SetValue='lb', Size=(20,6), xStretch=True, yStretch=True)],
            [self.GButton(Text='Show Selected', SetValue='show')],
            [self.GText(SetText='Selected: ', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'show':
            sel = self.GetValues.get('lb')
            self.GetWindow['lbl'].update('Selected: ' + str(sel))

if __name__ == '__main__':
    ListboxTutorial()
