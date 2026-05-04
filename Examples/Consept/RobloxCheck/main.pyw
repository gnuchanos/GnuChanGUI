import CheckCustomer
import json, os, time

"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

try:
    # Don't do like this from lib import * for gnchangui
    from GnuChanGUI import GnuChanGUI, os, Thread, GTime
    from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GMessage
    from GnuChanGUI import GKeyboard_Winows, GTime
    
except ImportError as e:
    raise ImportError("you need install GnuChanGUI") from e


# Extra Lib
# #Thread(target=DownloadVideo, args=[]).start()

# note this is test Place

class DefaultExample(GnuChanGUI):
    def __init__(self, Title="Simple Roblox Check System", Size=(1200, 900), resizable=False, finalize=True, winPosX=1920 / 2, winPosY=1080 / 2):
        super().__init__(Title, Size, resizable, finalize, winPosX, winPosY)

        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors

        # old keyboard event
        self.Key_Windolf = GKeyboard_Winows()
        self.TypeList = (
            "Follower", "Goup", "AssetLike", "BundleLike", "GameFav", "FrendReq", "ForumFollow", "ForumLikes"
        )

        self.DATA = CheckCustomer.SYSTEM()
        self.UPDATECUSTOMER_THREAD = True


        self.Top = [
            [self.GText(BColor=self.CGC.SColors1, TFont="Sans, 5")],
            [
                self.GText(SetText="ID: ", EmptySpace=(0, None)),
                self.GInput(SetValue="ID", xStretch=True, EmptySpace=(0, None))
            ],
            [self.GText(BColor=self.CGC.SColors1, TFont="Sans, 1")],
            [
                self.GText(SetText="Goal: ", EmptySpace=(0, None)),
                self.GInput(SetValue="Goal", xStretch=True, EmptySpace=(0, None))
            ],
            [self.GText(BColor=self.CGC.SColors1, TFont="Sans, 1")],
            [
                self.GText(SetText="Choose Type: ", EmptySpace=(0, None)),
                self.GSelection(ListValues=self.TypeList, DefaultValue="Follower", SetValue="Type", xStretch=True, EmptySpace=(0, None)),
            ],
            [self.GText(BColor=self.CGC.SColors1, TFont="Sans, 1")],
            [
                self.GPush(BColor=self.CGC.SColors1),
                self.GButton(Text="ADD", xStretch=True),
                self.GButton(Text="REMOVE", xStretch=True),
                self.GButton(Text="COPY LINK", xStretch=True),
                self.GPush(BColor=self.CGC.SColors1)
            ],
            [self.GText(BColor=self.CGC.SColors1, TFont="Sans, 5")]
        ]


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GColumn(winColumnLayout_List=self.Top, BColor=self.CGC.SColors1, xStretch=True)],
            [self.GListBox(SetValue="list", xStretch=True, yStretch=True, noScroolBar=True, LPosition="center")]
        ]





        # note don't call self.getwindow here
        self.GWindow(SetMainWindowLayout_List=self.Layout, Borderless=False, KeepOnTop=False)
        # Call Function Here not outside

        self.GBorder(WindowValue="list", Border=20, Color=self.CGC.SColors0)


        Thread(target=self.UpdateCustomer, args=[]).start()
        Thread(target=self.OPENFILE, args=[]).start()



        # Call Function Here
        self.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)
        # note don't call self.getwindow here

    def ADDHERE(self):
        # ID
        if not len(self.GetValues["ID"]) > 0 : return None
        if not self.GetValues["ID"].isdigit(): return None

        # GOAL
        if not len(self.GetValues["Goal"]) > 0 : return None
        if not self.GetValues["Goal"].isdigit(): return None

        # TYPE
        if not len(self.GetValues["Type"]) > 0 : return None

        # ADD USER
        print(f"{int(self.GetValues["ID"])} : {self.GetValues["Goal"]} : {self.GetValues["Type"]}")
        self.DATA.Add(Type=self.GetValues["Type"], ID=self.GetValues["ID"], Goal=self.GetValues["Goal"])
        self.GetWindow["list"].update(self.DATA.CustomersLIST)
        self.SAVEANDCHECK()

    def REMOVE(self):
        _SPLITHERE  = str(self.GetValues["list"]).strip("[']").split(" ")
        _ID         = _SPLITHERE[0][3::]
        REMOVEINDEX = self.GListboxReturnIndex(WindowValue="list")

        self.DATA.Remove(ID=_ID, REMOVEINDEX=REMOVEINDEX)
        self.SAVEANDCHECK()
        time.sleep(1)
        self.GetWindow["list"].update(self.DATA.CustomersLIST)

    def SAVEANDCHECK(self):
        PATH = os.getcwd()
        FILE = os.path.join(PATH, "Customer.gc")
        
        if os.path.exists(FILE):
            with open(FILE, "w") as file:
                json.dump(self.DATA.Customers, file, indent=4)

    def OPENFILE(self):
        PATH = os.getcwd()
        FILE = os.path.join(PATH, "Customer.gc")
        
        if os.path.exists(FILE):
            with open(FILE, 'r', encoding='utf-8') as file:
                self.DATA.Customers = json.load(file)

        self.DATA.AddInList()
        time.sleep(1)
        self.GetWindow["list"].update(self.DATA.CustomersLIST)

    def UpdateCustomer(self):
        while self.UPDATECUSTOMER_THREAD:
            self.DATA.Update()
            time.sleep(1)
            self.GetWindow["list"].update(self.DATA.CustomersLIST)
            time.sleep(60)

    def Update(self):
        #self.GetEvent == "event" -> window event
        #self.GetWindow["text"].update("this text") -> update window objects

        if "ADD" == self.GetEvent:
            Thread(target=self.ADDHERE, args=[]).start()
        
        if "REMOVE" == self.GetEvent:
            Thread(target=self.REMOVE, args=[]).start()

    def BeforeExit(self):
        self.UPDATECUSTOMER_THREAD = False
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()

    """
    gc.Customers.Add(Type="Follower", ID=7080613236, Goal=3123123)
    print('-'*30)
    gc.Customers.Add(Type="Goup", ID=800205755, Goal=3123123)
    print('-'*30)
    gc.Customers.Add(Type="AssetLike", ID=129622440083648, Goal=3123123)
    print('-'*30)
    gc.Customers.Add(Type="BundleLike", ID=236506229099970, Goal=3123123)
    print('-'*30)
    gc.Customers.Add(Type="GameFav", ID=9952351777, Goal=3123123)
    print('-'*30)
    gc.Customers.Add(Type="FrendReq", ID=4987966196, Goal=3123123)
    """







