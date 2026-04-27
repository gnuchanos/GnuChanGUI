import requests




test = {}
test[2312312] = {
    "ID" : 3123123,
    "Name" : "",
    "Current" : 23123,
    "Max" : 312312,
    "Finish" : False
}


class Customer:
    def __init__(self):
        self.Customers = {}

    def Add(self, Type: str, ID: int):
        _Customer = ""

        if "Follower"  == Type:
            data = requests.get( f"https://friends.roblox.com/v1/users/{ID}/followers/count" ).json()

        elif "Goup" == Type:
            data = requests.get( f"https://groups.roblox.com/v1/groups/{ID}" ).json()

        elif "AssetLike" == Type:
            data = requests.get( "https://catalog.roblox.com/v1/catalog/items/details", params={"itemIds": ID} ).json()

        elif "BundleLike" == Type:
            data = requests.get( f"https://catalog.roblox.com/v1/bundles/{ID}/details" ).json()

        elif "GameFav" == Type:
            data = requests.get( f"https://games.roblox.com/v1/games?universeIds={ID}" ).json()

        elif "FrendReq" == Type:
            data = requests.get( f"https://friends.roblox.com/v1/users/{ID}/friends" ).json()

        elif "ForumFollow" == Type:
            data = requests.get( f"https://devforum.roblox.com/u/{ID}.json" ).json()

        elif "ForumLikes" == Type:
            data = requests.get( f"https://devforum.roblox.com/posts/{ID}.json" ).json()

        elif "GoupLike" == Type:
            data = requests.get( f"https://groups.roblox.com/v1/groups/{ID}" ).json()
        
        print(data)

    def Remove(self):
        pass
