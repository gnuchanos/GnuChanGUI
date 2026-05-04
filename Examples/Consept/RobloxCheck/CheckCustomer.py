import requests

class SYSTEM:
    def __init__(self):
        self.Customers = {}
        self.CustomersLIST = []
        self.ERROR = ""

    def Add(self, Type: str, ID: int, Goal: int):
        _Customer = ""

        if "Follower"  == Type:
            data = requests.get( f"https://friends.roblox.com/v1/users/{ID}/followers/count" ).json()
            dataExtra = requests.get( f"https://users.roblox.com/v1/users/{ID}" ).json()

            if "errors" in dataExtra:
                self.ERROR = f"dataExtra: {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            if "errors" in data:
                self.ERROR = f"data {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            self.Customers[ID] = {
                "ID"      : ID,
                "Name"    : dataExtra["name"],
                "Current" : data["count"],
                "Max"     : Goal,
                "Finish"  : False,
                "Type"    : Type
            }
            print(f"ADD Follower: {self.Customers[ID]}")

            Customer = f"ID:{self.Customers[ID]["ID"]} Name:{self.Customers[ID]["Name"]} Type:{self.Customers[ID]["Type"]} Current:{self.Customers[ID]["Current"]} Max:{self.Customers[ID]["Max"]} Finish:{self.Customers[ID]["Finish"]}"
            if Customer not in self.CustomersLIST:
                self.CustomersLIST.append( Customer )


        elif "Goup" == Type:
            data = requests.get( f"https://groups.roblox.com/v1/groups/{ID}" ).json()

            if "errors" in data:
                self.ERROR = f"data {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None
            
            self.Customers[ID] = {
                "ID"      : ID,
                "Name"    : data["name"],
                "Current" : data["memberCount"],
                "Max"     : Goal,
                "Finish"  : False,
                "Type"    : Type
            }
            print(f"ADD Goup: {self.Customers[ID]}")

            Customer = f"ID:{self.Customers[ID]["ID"]} Name:{self.Customers[ID]["Name"]} Type:{self.Customers[ID]["Type"]} Current:{self.Customers[ID]["Current"]} Max:{self.Customers[ID]["Max"]} Finish:{self.Customers[ID]["Finish"]}"
            if Customer not in self.CustomersLIST:
                self.CustomersLIST.append( Customer )

        elif "AssetLike" == Type:
            data = requests.get( f"https://economy.roblox.com/v2/assets/{ID}/details" ).json()
            dataExtra = requests.get( f"https://catalog.roblox.com/v1/favorites/assets/{ID}/count" ).json()
            _dataExtra = {"count": dataExtra}

            if "errors" in _dataExtra:
                self.ERROR = f"dataExtra: {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            if "errors" in data:
                self.ERROR = f"data {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            self.Customers[ID] = {
                "ID"      : ID,
                "Name"    : data["Name"],
                "Current" : _dataExtra["count"],
                "Max"     : Goal,
                "Finish"  : False,
                "Type"    : Type
            }
            print(f"ADD AssetLike: {self.Customers[ID]}")

            Customer = f"ID:{self.Customers[ID]["ID"]} Name:{self.Customers[ID]["Name"]} Type:{self.Customers[ID]["Type"]} Current:{self.Customers[ID]["Current"]} Max:{self.Customers[ID]["Max"]} Finish:{self.Customers[ID]["Finish"]}"
            if Customer not in self.CustomersLIST:
                self.CustomersLIST.append( Customer )

        elif "BundleLike" == Type:
            data = requests.get( f"https://catalog.roblox.com/v1/bundles/{ID}/details" ).json()
            dataExtra = requests.get( f"https://catalog.roblox.com/v1/favorites/bundles/{ID}/count" ).json()
            _dataExtra = {"count": dataExtra}

            if "errors" in _dataExtra:
                self.ERROR = f"dataExtra: {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            if "errors" in data:
                self.ERROR = f"data {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None
            
            self.Customers[ID] = {
                "ID"      : ID,
                "Name"    : data["name"],
                "Current" : _dataExtra["count"],
                "Max"     : Goal,
                "Finish"  : False,
                "Type"    : Type
            }
            print(f"ADD BundleLike: {self.Customers[ID]}")

            Customer = f"ID:{self.Customers[ID]["ID"]} Name:{self.Customers[ID]["Name"]} Type:{self.Customers[ID]["Type"]} Current:{self.Customers[ID]["Current"]} Max:{self.Customers[ID]["Max"]} Finish:{self.Customers[ID]["Finish"]}"
            if Customer not in self.CustomersLIST:
                self.CustomersLIST.append( Customer )

        # in inspect and under game-card-link -> universeId
        elif "GameFav" == Type:
            data = requests.get( f"https://games.roblox.com/v1/games?universeIds={ID}" ).json()

            if "errors" in data:
                self.ERROR = f"data {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None
            
            self.Customers[ID] = {
                "ID"      : ID,
                "Name"    : data["data"][0]["name"],
                "Current" : data["data"][0]["favoritedCount"],
                "Max"     : Goal,
                "Finish"  : False,
                "Type"    : Type
            }
            print(f"ADD GameFav: {self.Customers[ID]}")

            Customer = f"ID:{self.Customers[ID]["ID"]} Name:{self.Customers[ID]["Name"]} Type:{self.Customers[ID]["Type"]} Current:{self.Customers[ID]["Current"]} Max:{self.Customers[ID]["Max"]} Finish:{self.Customers[ID]["Finish"]}"
            if Customer not in self.CustomersLIST:
                self.CustomersLIST.append( Customer )

        elif "FrendReq" == Type:
            data = requests.get( f"https://friends.roblox.com/v1/users/{ID}/friends/count" ).json()
            dataExtra = requests.get( f"https://users.roblox.com/v1/users/{ID}" ).json()

            if "errors" in dataExtra:
                self.ERROR = f"dataExtra: {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            if "errors" in data:
                self.ERROR = f"data {data["errors"][0]["message"]}"
                print(self.ERROR)
                return None

            self.Customers[ID] = {
                "ID"      : ID,
                "Name"    : dataExtra["name"],
                "Current" : data["count"],
                "Max"     : Goal,
                "Finish"  : False,
                "Type"    : Type
            }

            print(f"ADD FrendReq: {self.Customers[ID]}")

            Customer = f"ID:{self.Customers[ID]["ID"]} Name:{self.Customers[ID]["Name"]} Type:{self.Customers[ID]["Type"]} Current:{self.Customers[ID]["Current"]} Max:{self.Customers[ID]["Max"]} Finish:{self.Customers[ID]["Finish"]}"
            if Customer not in self.CustomersLIST:
                self.CustomersLIST.append( Customer )

        elif "ForumFollow" == Type:
            data = requests.get( f"https://devforum.roblox.com/u/{ID}.json" ).json()

            print(data)

        elif "ForumLikes" == Type:
            data = requests.get( f"https://devforum.roblox.com/posts/{ID}.json" ).json()

            print(data)

    def Remove(self, ID: int, REMOVEINDEX: int):
        del self.Customers[ID]
        self.CustomersLIST.pop(int(REMOVEINDEX))

    def AddInList(self):
        for i in self.Customers:
            if i not in self.CustomersLIST:
                CUSTOMER = f"ID:{self.Customers[i]["ID"]} Name:{self.Customers[i]["Name"]} Type:{self.Customers[i]["Type"]} Current:{self.Customers[i]["Current"]} Max:{self.Customers[i]["Max"]} Finish:{self.Customers[i]["Finish"]}"
                self.CustomersLIST.append(CUSTOMER)
                print(CUSTOMER)
        
        print(self.CustomersLIST)
    
    def Update(self) -> None:
        _TEMPDICT      = self.Customers
        self.Customers = {}
        self.CustomersLIST = []

        for i in _TEMPDICT:
            self.Add(Type=_TEMPDICT[i]["Type"], ID=_TEMPDICT[i]["ID"], Goal=_TEMPDICT[i]["Max"])
            print(f"--> {i}")