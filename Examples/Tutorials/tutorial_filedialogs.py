"""File dialogs tutorial - demonstrates GetFilePath, GetFileForSave, GetFolderPath usage.
"""

try:
    import GnuChanGUI as gc
except Exception:
    raise

class FileDialogsTutorial(gc.GnuChanGUI):
    def __init__(self):
        super().__init__(Title='File Dialogs', Size=(480,220), finalize=True)

        self.Layout = [
            [self.GText(SetText='File Dialogs demo', xStretch=True)],
            [self.GButton(Text='Open File', SetValue='open')],
            [self.GButton(Text='Save File', SetValue='save')],
            [self.GButton(Text='Pick Folder', SetValue='folder')],
            [self.GText(SetText='Result:', SetValue='res')]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout)
        self.SetUpdate(self.Update)

    def Update(self):
        if not self.GetValues:
            return
        if self.GetEvent == 'open':
            p = self.GetFilePath(message='Select a file to open')
            self.GetWindow['res'].update(str(p))
        if self.GetEvent == 'save':
            p = self.GetFileForSave(message='Save as')
            self.GetWindow['res'].update(str(p))
        if self.GetEvent == 'folder':
            p = self.GetFolderPath(message='Select a folder')
            self.GetWindow['res'].update(str(p))

if __name__ == '__main__':
    FileDialogsTutorial()
