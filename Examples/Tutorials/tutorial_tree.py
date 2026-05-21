"""Tree tutorial - demonstrates GTree and GTreeData usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class TreeTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Tree Tutorial', Size=(520,360), finalize=True)

        self.tree_data = [
            ('Fruits', ['Apple','Banana','Cherry']),
            ('Vegetables', ['Asparagus','Broccoli','Carrot'])
        ]

        td = self.GTreeData()
        for idx,(k,v) in enumerate(self.tree_data):
            parent = td.insert('', f'root{idx}', k, [len(v)])
            for j, item in enumerate(v):
                td.insert(parent, f'child{idx}_{j}', item, [f'child {j+1}'])

        self.Layout = [
            [self.GText(SetText='Tree demo', TFont='Sans,14', xStretch=True)],
            [self.GTree(TreeDATA=td, headings=['Item', 'Info'], SetValue='tree', xStretch=True, yStretch=True)],
            [self.GButton(Text='Show Root Count', SetValue='count')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'count':
            gc.GMessage(WindowTitle='Tree', WindowText='Tree roots: ' + str(len(self.tree_data)))

if __name__ == '__main__':
    TreeTutorial()
