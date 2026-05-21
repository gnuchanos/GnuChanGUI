"""OptionMenu tutorial - demonstrates GOptionMenu usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class OptionMenuTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='OptionMenu Tutorial', Size=(420,200), finalize=True)

        self.Layout = [
            [self.GText(SetText='OptionMenu demo', TFont='Sans,14', xStretch=True)],
            [self.GOptionMenu(['One','Two','Three'], DefaultValue='Two', SetValue='opt', xStretch=True)],
            [self.GButton(Text='Show', SetValue='show')],
            [self.GText(SetText='Selected:', SetValue='lbl')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'show':
            self.GetWindow['lbl'].update('Selected: ' + str(self.GetValues.get('opt')))

if __name__ == '__main__':
    OptionMenuTutorial()
