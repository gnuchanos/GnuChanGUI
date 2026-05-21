"""TabGroup tutorial - demonstrates GTabGroup and GTab usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class TabTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Tab Tutorial', Size=(520,320), finalize=True)

        tab1 = [[self.GText(SetText='Content of Tab 1', xStretch=True)], [self.GButton(Text='Tab1 Btn', SetValue='t1btn')]]
        tab2 = [[self.GText(SetText='Content of Tab 2', xStretch=True)], [self.GButton(Text='Tab2 Btn', SetValue='t2btn')]]

        self.Layout = [
            [self.GText(SetText='TabGroup demo', TFont='Sans,14', xStretch=True)],
            [self.GTabGroup(TabGroupLayout=[
                [gc.GTab(Text='Tab 1', TabLayout=tab1, SetValue='tab1')],
                [gc.GTab(Text='Tab 2', TabLayout=tab2, SetValue='tab2')],
            ], SetValue='tabG')],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 't1btn':
            gc.GMessage(WindowTitle='Tab', WindowText='Tab1 button clicked')
        if self.GetEvent == 't2btn':
            gc.GMessage(WindowTitle='Tab', WindowText='Tab2 button clicked')

if __name__ == '__main__':
    TabTutorial()
