import time

from CheckAccount import RobloxAccountCheck

try:
    from GnuChanGUI import (
        GnuChanGUI, os, Thread,
        GnuChanOSColor, GColors, Themecolors, GMessage,
        GKeyboard_Winows
    )
except ImportError as e:
    raise ImportError(e) from e


# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample(GnuChanGUI):
    def __init__( self, Title="Followers Control Center", Size=(1600, 900), resizable=True, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2 ):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS
        self.C = GColors()
        self.CGC = GnuChanOSColor()
        self.Key_Windolf = GKeyboard_Winows()

        self.CurrentPath = os.getcwd()
        print(self.CurrentPath)

        self.System = RobloxAccountCheck()
        self._UsersText = []
        self.UpdateNotClose = True


        _Top = [
            [
                self.GPush(BColor=self.CGC.SColors0),
                self.GButton(Text="Add User", SetValue="add"),
                self.GButton(Text="Remove User", SetValue="remove"),
                self.GButton(Text="Update Data", SetValue="refresh"),
                self.GButton(Text="Open Note", SetValue="load"),
                self.GButton(Text="Save Note", SetValue="save"),
                self.GPush(BColor=self.CGC.SColors0),
            ],
            [
                self.GText(SetText="User ID", BColor=self.CGC.SColors0),
                self.GInput(SetValue="inputID", xStretch=True, BColor=self.C.purple7),
            ],
            [
                self.GText(SetText="User Final Follower Limit", BColor=self.CGC.SColors0),
                self.GInput(SetValue="mf", xStretch=True, BColor=self.C.purple7),
            ],
        ]


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GText(SetValue="warning", xStretch=True, TPosition="center", BColor=self.C.purple5)],
            [self.GColumn(winColumnLayout_List=_Top, xStretch=True, BColor=self.CGC.SColors0)],
            [self.GListBox(SetValue="list", LPosition="center", xStretch=True, yStretch=True, BColor=self.C.purple8, noScroolBar=True)],
            [self.GMultiline(SetValue="note", xStretch=True, yStretch=True, TFont=("Sans, 40"))]
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        # Call Function Here not outside

        self.GBorder("list", Border=5, Color=self.C.purple3)
        self.GBorder("note", Border=5, Color=self.C.purple5)




        Thread(target=self._Load, args=[]).start()
        Thread(target=self._CheckIfFinish, args=[]).start()
        Thread(target=self._Update, args=[]).start()

        # Call Function Here not outside
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def _Load(self):
        try:
            self.System.LoadUsers()
            self._UsersText = self.System.AddInUsersTextListBox()
            self.GetWindow["list"].Update(self._UsersText)

        except Exception as ERR:
            print(ERR)

    def _CheckIfFinish(self):
        self.System._CheckIfFinish()

    def _Update(self):
        while self.UpdateNotClose:
            self.System.UpdateUsersData()
            self._Load()
            time.sleep(10)

    def _UpdateClickUpdate(self):
        self.System.UpdateUsersData()
        self._Load()

    def RemoveUser(self):
        try:
            _PlaceHolderUser = str(self.GetValues["list"]).split(" ")
            _READYID = _PlaceHolderUser[4].strip("]")
            self.System.RemoveUser(ID=_READYID)

            _lisboxIndex = self.GListboxReturnIndex(WindowValue="list")
            self._UsersText.pop(_lisboxIndex)

            Thread(target=self._UpdateClickUpdate, args=[]).start()
            Thread(target=self._Load, args=[]).start()

        except Exception as ERR:
            print(ERR)

    def _ADD(self):
        try:
            if len(self.GetValues["inputID"]) > 0 and len(str(self.GetValues["mf"])) > 0:
                _ID = self.GetValues["inputID"]
                _IDMAXFOLLOWER = int(self.GetValues["mf"])

                self.System.AddNew(_ID, _IDMAXFOLLOWER)
                self._Load()

        except Exception as ERR:
            print(ERR)

    def SaveNote(self):
        try:
            _PlaceHolderUser = str(self.GetValues["list"]).split(" ")
            _READYID = _PlaceHolderUser[4].strip("]")

            _Text = self.GetValues["note"]
            self.System.Users[_READYID]["Notes"] = _Text
            self.System.SaveUsers()

        except Exception as ERR:
            print(ERR)

    def LoadNote(self):
        try:
            _PlaceHolderUser = str(self.GetValues["list"]).split(" ")
            _READYID = _PlaceHolderUser[4].strip("]")
            self.GetWindow["note"].Update(self.System.Users[_READYID]["Notes"])

        except Exception as ERR:
            print(ERR)


    def Update(self):

        if self.GetEvent == "add":
            Thread(target=self._ADD, args=[]).start()

        elif self.GetEvent == "refresh":
            Thread(target=self._UpdateClickUpdate).start()

        elif self.GetEvent == "remove":
            Thread(target=self.RemoveUser).start()

        elif "save" == self.GetEvent:
            Thread(target=self.SaveNote).start()

        elif "load" == self.GetEvent:
            Thread(target=self.LoadNote).start()

    def BeforeExit(self):
        self.System.StopChecking = True
        self.UpdateNotClose = False

        print("Exit")


if __name__ == "__main__":
    gc = DefaultExample()
