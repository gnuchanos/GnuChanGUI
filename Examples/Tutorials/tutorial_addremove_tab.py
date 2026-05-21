"""Add/Remove Tab tutorial - demonstrates GAddTab and GRemoveTab usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class AddRemoveTabTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Add/Remove Tab', Size=(640,360), finalize=True)

        tab1 = [[self.GText(SetText='Content of Tab 1', xStretch=True)]]
        tab2 = [[self.GText(SetText='Content of Tab 2', xStretch=True)]]

        self.Layout = [
            [self.GTabGroup(TabGroupLayout=[
                [self.GTab(Text='Tab 1', TabLayout=tab1, SetValue='t1')],
                [self.GTab(Text='Tab 2', TabLayout=tab2, SetValue='t2')],
            ], SetValue='tg')],
            [self.GButton(Text='Add Tab', SetValue='add'), self.GButton(Text='Remove Tab', SetValue='remove')],
        ]

        self.counter = 3
        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if self.GetEvent == 'add':
            title = f'New {self.counter}'
            layout = [[self.GText(SetText=f'This is {title}', xStretch=True)]]
            self.GAddTab('tg', title, layout)
            self.counter += 1
        if self.GetEvent == 'remove':
            # try to remove last tab by index
            try:
                # Tab identifiers may be title or index
                self.GRemoveTab('tg', -1)
            except Exception as e:
                print('Remove tab error', e)

if __name__ == '__main__':
    AddRemoveTabTutorial()
