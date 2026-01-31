import requests
import json
import time
import os
from gtts import gTTS
from threading import Thread
from GnuChanGUI import GMixer



class RobloxAccountCheck:
    def __init__(self):
        self.UserIDS      : list = []
        self.Users        : dict = {}
        self.CurrentPath  : str  = os.getcwd()
        self.Sound               = GMixer(MaxChannelLimit=1)
        self.StopChecking        = False

        self.u = {}
        self.r = {}
        self.Debug: bool = True

    def AddNew(self, ID: str, FinalFollower):
        try:
            self.r = requests.get(f"https://friends.roblox.com/v1/users/{ID}/followers/count").json()
            #time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
        
        print(self.r)

        try:
            self.u = requests.get(f"https://users.roblox.com/v1/users/{ID}").json()
            #time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")

        if "errors" not in self.r:
            if str(ID) not in self.UserIDS:
                self.UserIDS.append(str(ID))

                self.Users[str(ID)] = {
                    "ID"            : self.u["id"],
                    "Name"          : self.u["name"],
                    "DisplayName"   : self.u["displayName"],
                    "Follower"      : self.r["count"],
                    "IsBanned"      : self.u["isBanned"],
                    "Notes"         : "",
                    "FinalFollower" : FinalFollower,
                    "IsComplete"    : False
                }

                self.SaveUsers()

    # for GnuChanGUI
    def AddInUsersTextListBox(self):
        _list = []
        for i in self.UserIDS:
            _list.append(f"[Final Follower: {self.Users[i]["FinalFollower"]}] [ID: {self.Users[i]["ID"]}] [Follower: {self.Users[i]["Follower"]}] [Name: {self.Users[i]["Name"]}] [Is Banned: {self.Users[i]["IsBanned"]}]")

        return _list

    # for console Debug
    def Print(self, ID: str):
        try:
            print(f"[Name: {self.Users[str(ID)]["Name"]}] [ID: {self.Users[str(ID)]["ID"]}] [Name: {self.Users[str(ID)]["Name"]}] [DisplayName: {self.Users[str(ID)]["DisplayName"]}] [Follower: {self.Users[str(ID)]["Follower"]}] [Is Banned: {self.Users[str(ID)]["IsBanned"]}]")
        except KeyError:
            print(f"{ID} this USER ID wrong")

    # for console Debug
    @property
    def PrintALL(self):
        for i in self.Users:
            print(f"[Name: {self.Users[i]["Name"]}] [ID: {self.Users[i]["ID"]}] [Name: {self.Users[i]["Name"]}] [DisplayName: {self.Users[i]["DisplayName"]}] [Follower: {self.Users[i]["Follower"]}] [Is Banned: {self.Users[i]["IsBanned"]}]")

    def RemoveUser(self, ID: str):
        if str(ID) in self.UserIDS:
            self.Users.pop(str(ID), None)
            self.UserIDS.remove(str(ID))
        
        self.SaveUsers()

    def SaveUsers(self):
        _File = os.path.join(self.CurrentPath, "users.gc")

        if os.path.exists(_File):
                os.remove(_File)
        
        #time.sleep(1)

        with open(_File, "w", encoding="utf-8") as f:
            json.dump(self.Users, f, indent=4)

    def LoadUsers(self):
        _File = os.path.join(self.CurrentPath, "users.gc")

        with open(_File, "r", encoding="utf-8") as f:
            self.Users = json.load(f)

        for i in self.Users.keys():
            if i not in self.UserIDS:
                self.UserIDS.append(i)

        self.UpdateUsersData()
        

    def UpdateUsersData(self):
        for i in self.UserIDS:
            try:
                self.r = requests.get(f"https://friends.roblox.com/v1/users/{i}/followers/count").json()
                #time.sleep(1)

            except requests.exceptions.RequestException as e:
                print(f"Connection error: {e}")
                return None

            if "errors" in self.r:
                return None

            try:
                self.u = requests.get(f"https://users.roblox.com/v1/users/{i}").json()
                #time.sleep(1)

            except requests.exceptions.RequestException as e:
                print(f"Connection error: {e}")
                return None
            
            self.Users[i]["ID"] = self.u["id"]
            self.Users[i]["Name"] = self.u["name"]
            self.Users[i]["DisplayName"] = self.u["displayName"]
            self.Users[i]["Follower"] = self.r["count"]
            self.Users[i]["IsBanned"] = self.u["isBanned"]

            self.SaveUsers()

    def _CheckIfFinish(self):
        time.sleep(1)

        while not self.StopChecking:
            for i in self.UserIDS:
                time.sleep(5)

                if self.StopChecking:
                    break
                
                if self.Users[str(i)]["Follower"] >= self.Users[str(i)]["FinalFollower"] and not self.Users[str(i)]["IsComplete"]:
                    _Text = f"{self.Users[str(i)]["Name"]}'s order is completed."
                    myobj = gTTS(text=_Text, lang="en", slow=False)
                    _File = os.path.join(self.CurrentPath, "welcome.mp3")
                    myobj.save(_File)

                    self.Users[str(i)]["IsComplete"] = True
                    print(f"| Finish -----| ID: {self.Users[str(i)]["ID"]} | Name: {self.Users[str(i)]["Name"]} | Current Follower {self.Users[str(i)]["Follower"]} | Final Goal: {self.Users[str(i)]["FinalFollower"]}")
                    time.sleep(1)

                    # Play

                else:
                    if self.Debug:
                        print(f"| SEO -----| ID: {self.Users[str(i)]["ID"]} | Name: {self.Users[str(i)]["Name"]} | Current Follower {self.Users[str(i)]["Follower"]} | Final Goal: {self.Users[str(i)]["FinalFollower"]}")


            


RAC = RobloxAccountCheck()

class GUI:
    def __init__(self):
        self.System = RobloxAccountCheck()
        

        self.System.LoadUsers()
    
    def Main(self):
        self.System.AddNew(ID=2597993363, FinalFollower=5300) 
        #self.System.AddNew(ID=9549362351, FinalFollower=5000)

    def Update(self):
        while True:
            self.System._CheckIfFinish(Debug=True)




            time.sleep(60)

if __name__ == "__main__":
    GC = GUI()
    GC.Main()
    GC.Update()