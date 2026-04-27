import CheckCustomer











gc = CheckCustomer.requests.get( f"https://friends.roblox.com/v1/users/{3404146431}/followers" ).json()

for i in gc["data"]:
    print(i)

