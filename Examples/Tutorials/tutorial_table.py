"""Table tutorial - demonstrates GTable usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class TableTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Table Tutorial', Size=(520,300), finalize=True)

        rows = [["ID","Name","Value"], [1, 'Alpha', 10], [2, 'Beta', 20], [3, 'Gamma', 30]]
        self.Layout = [
            [self.GText(SetText='Table demo', TFont='Sans,14', xStretch=True)],
            [self.GTable(TableLists=rows, SetValue='tbl', VisibleRows=5, xStretch=True)],
            [self.GButton(Text='Print Selected', SetValue='print')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'print':
            v = self.GetValues.get('tbl')
            gc.GMessage(WindowTitle='Table Selection', WindowText=str(v))

if __name__ == '__main__':
    TableTutorial()
