"""Widget helpers tutorial - demonstrates utility methods like GetGTextValue, GBorder, GSelectionBorderSize, GListboxReturnIndex, and GMultilineTabSpace.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class WidgetHelpersTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='Widget Helpers', Size=(620,420), finalize=True)

        self.Layout = [
            [self.GText(SetText='Widget helper demo', TFont='Sans,16', xStretch=True)],
            [self.GText(SetText='Named Text field', SetValue='label_text', xStretch=True, BColor='#eeeeee')],
            [self.GText(SetText='ListBox selection', xStretch=True)],
            [self.GListBox(list=['One','Two','Three','Four'], SetValue='list1', Size=(30,4), xStretch=True)],
            [self.GText(SetText='Combo selection', xStretch=True)],
            [self.GSelection(ListValues=['Red','Green','Blue'], DefaultValue='Red', SetValue='sel', xStretch=True)],
            [self.GText(SetText='Multiline with tab spacing:', xStretch=True)],
            [self.GMultiline(InText='A\tB\tC\n1\t2\t3\nX\tY\tZ', SetValue='mult', TFont='Sans,14', Size=(60,6), xStretch=True, yStretch=True)],
            [self.GButton(Text='Read GText', SetValue='read_text'), self.GButton(Text='Borderize Text', SetValue='border_text')],
            [self.GButton(Text='Style Combo', SetValue='style_combo'), self.GButton(Text='List Index', SetValue='list_index')],
            [self.GButton(Text='Apply Tab Spacing', SetValue='tab_space'), self.GButton(Text='Hide Multi', SetValue='hide_mult')],
            [self.GButton(Text='Show Multi', SetValue='show_mult')],
            [self.GText(SetText='Result:', SetValue='result', xStretch=True)]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return

        if self.GetEvent == 'read_text':
            value = self.GetGTextValue('label_text')
            self.GetWindow['result'].update('GText value: ' + str(value))

        if self.GetEvent == 'border_text':
            self.GBorder('label_text', 2, '#ff0000')
            self.GetWindow['result'].update('Added red border to GText')

        if self.GetEvent == 'style_combo':
            self.GSelectionBorderSize(2, 'sel', '#00aa00', '#ffffff')
            self.GetWindow['result'].update('Styled selection border')

        if self.GetEvent == 'list_index':
            idx = self.GListboxReturnIndex('list1')
            self.GetWindow['result'].update('List index: ' + str(idx))

        if self.GetEvent == 'tab_space':
            self.GMultilineTabSpace('Sans,14', 'mult')
            self.GetWindow['result'].update('Tab spacing applied')

        if self.GetEvent == 'hide_mult':
            self.GVisible('mult', False)
            self.GetWindow['result'].update('Multiline hidden')

        if self.GetEvent == 'show_mult':
            self.GVisible('mult', True)
            self.GetWindow['result'].update('Multiline shown')

if __name__ == '__main__':
    WidgetHelpersTutorial()
