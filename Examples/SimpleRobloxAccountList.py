import requests
import json

try:
    from GnuChanGUI import (
        GnuChanGUI, os, Thread,
        GnuChanOSColor, GColors, Themecolors, GMessage,
        GKeyboard_Winows
    )
except ImportError as e:
    raise ImportError(e) from e


class DefaultExample(GnuChanGUI):
    def __init__( self, Title="Followers Control Center", Size=(1600, 900), resizable=True, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2 ):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS
        self.C = GColors()
        self.CGC = GnuChanOSColor()
        self.Key_Windolf = GKeyboard_Winows()

        self.CurrentPath = os.getcwd()
        print(self.CurrentPath)

        # === DATA ===
        self.Users = {}    # { uid : data }
        self.UserIDs = []  # listbox order

        # === GUI ===
        _Top = [
            [
                self.GPush(BColor=self.CGC.SColors0),
                self.GButton(Text="Add User", SetValue="add"),
                self.GButton(Text="Remove User", SetValue="remove"),
                self.GButton(Text="Update Data", SetValue="refresh"),
                self.GPush(BColor=self.CGC.SColors0),
            ],
            [
                self.GText(SetText="User ID", BColor=self.CGC.SColors0),
                self.GInput(SetValue="inputID", xStretch=True, BColor=self.C.purple7),
            ],
        ]

        self.Layout = [
            [self.GText(SetValue="warning", xStretch=True, TPosition="center", BColor=self.C.purple5)],
            [self.GColumn(winColumnLayout_List=_Top, xStretch=True, BColor=self.CGC.SColors0)],
            [self.GListBox(SetValue="list", LPosition="center", xStretch=True, yStretch=True, BColor=self.C.purple8, noScroolBar=True)],
        ]

        self.GWindow(SetMainWindowLayout_List=self.Layout, KeepOnTop=False)
        self.GBorder("list", Border=5, Color=self.C.purple3)

        self.LoadUsers()
        Thread(target=self.UpdateRequest).start()

        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    # ===============================
    # ROBLOX API
    # ===============================
    def SendRequest(self, user_id):
        user_id = str(user_id)

        r = requests.get(
            f"https://friends.roblox.com/v1/users/{user_id}/followers/count"
        ).json()

        if "errors" in r:
            return None

        u = requests.get(
            f"https://users.roblox.com/v1/users/{user_id}"
        ).json()

        return {
            "ID": u["id"],
            "Name": u["name"],
            "DisplayName": u["displayName"],
            "Follower": r["count"],
            "IsBanned": u["isBanned"],
        }

    # ===============================
    # LIST
    # ===============================
    def RefreshList(self):
        items = []
        for uid in self.UserIDs:
            u = self.Users[uid]
            items.append(
                f"| [UserID: {u['ID']}] | [Name: {u['Name']}] [Display Name: {u["DisplayName"]} | [Follower: {u['Follower']}] | [IBanned: {u['IsBanned']}] |"
            )
        self.GetWindow["list"].Update(items)

    # ===============================
    # SAVE / LOAD
    # ===============================
    def SaveUsers(self):
        path = os.path.join(self.CurrentPath, "users.gc")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.Users, f, indent=4)

    def LoadUsers(self):
        path = os.path.join(self.CurrentPath, "users.gc")

        if not os.path.exists(path):
            self.Users = {}
            self.UserIDs = []
            return

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    self.Users = {}
                    self.UserIDs = []
                    return

                self.Users = json.loads(content)
                self.UserIDs = list(self.Users.keys())
                self.RefreshList()

        except (json.JSONDecodeError, ValueError):
            self.Users = {}
            self.UserIDs = []

    # ===============================
    # ADD / UPDATE / REMOVE
    # ===============================
    def Add(self):
        uid = self.GetValues["inputID"].strip()
        if not uid:
            return

        data = self.SendRequest(uid)
        if not data:
            self.GetWindow["warning"].Update("User not found")
            return

        if uid not in self.UserIDs:
            self.UserIDs.append(uid)

        self.Users[uid] = data
        self.SaveUsers()
        self.RefreshList()

    def UpdateRequest(self):
        for uid in self.UserIDs:
            data = self.SendRequest(uid)
            if data:
                self.Users[uid] = data

        self.SaveUsers()
        self.RefreshList()

    def Remove(self):
        try:
            index = self.GListboxReturnIndex("list")
        except (KeyError, IndexError):
            GMessage("Warning", "Silmek için kullanıcı seç")
            return

        uid = self.UserIDs[index]
        self.Users.pop(uid, None)
        self.UserIDs.pop(index)

        self.SaveUsers()
        self.RefreshList()

    # ===============================
    # EVENTS
    # ===============================
    def Update(self):
        if self.GetEvent == "add":
            Thread(target=self.Add).start()

        elif self.GetEvent == "refresh":
            Thread(target=self.UpdateRequest).start()

        elif self.GetEvent == "remove":
            Thread(target=self.Remove).start()

    def BeforeExit(self):
        print("Exit")


if __name__ == "__main__":
    DefaultExample()
