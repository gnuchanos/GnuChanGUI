games = {
    "hl":"Half Life3",
    "lf3":"Left 4 Dead 3",
    "prt3":"Portal 3",
    "tf3": "Team fortress 3"
}

path = "/home/archkubi/Github/gnuchangui/examples/tutorial.txt"

print(games)
games["hl"] = "test"
print(games)

with open(path, 'w', encoding="utf-8") as file:
    file.write(str(games))

with open(path, 'r') as test:
    games = test.read()
print(games)

import os

os.popen("python deff.py")
os.system("echo hello world")

