"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

from GnuChanGUI import *
from threading import Thread
from gamelist import gamelist

if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Wine Manager", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    # First Create Wine Container
    CreateWinePrefix = [
        [   gc.hsep   ],
        [   gc.GText(title=f"'{os.path.expanduser("~")}/Games/winePrefix/' <-- Wine Prefix here", 
                     position="center", xStretch=True, bcolor=GColors().purple7)   
        ],
        [   
            gc.GText(title=f"{os.path.expanduser("~")}/Games/winePrefix/", EmptySpace=(0, 0), bcolor=GColors().purple6),
            gc.GInput(value="path_wine", xStretch=True, EmptySpace=(0, 0), bcolor=GColors().purple6)
        ],
        [
            gc.Push,
            gc.GRadio(value="32bit", groupID="wine", title="32Bit", bcolor=GColors().purple7),
            gc.GRadio(value="64bit", groupID="wine", title="64Bit", bcolor=GColors().purple7),
            gc.Push
        ],
        [   gc.Push, gc.GButton(title="Create Prefix"), gc.Push    ],
        [   
            gc.GListBox(value="gamelist_create", xStretch=True, yStretch=True, bcolor=GColors().purple8),
        ],
        [   gc.hsep   ],
    ]

    # Second Run Games 
    wineBody = [
        [   gc.hsep   ],
        [   gc.GText(title="Don't forget to choose your game's own Wine prefix!", xStretch=True, position="center", bcolor=GColors().purple7)     ],
        [   gc.GText(title="This Important Warning! 'File Name' is okay but ' file name ' NOPE!", 
                     bcolor=GColors().purple5, xStretch=True, position="center")   ],

        [   gc.GText(title="Choose Youre Wine", xStretch=True, position="center", bcolor=GColors().purple7)   ],

        [   
            gc.Push,
            gc.GButton(title="WineTRICKS"),
            gc.GButton(title="WineCFG"),
            gc.GButton(title="Run .EXE"),
            gc.GButton(title="Update Prefix"),
            gc.GButton(title="Remove Prefix"),
            gc.Push,
        ],
        [   
            gc.GListBox(value="gamelist_run", xStretch=True, yStretch=True, bcolor=GColors().purple8),
        ],
        [   gc.hsep   ],
    ]


    wine_Create = [
        [   gc.GColumn(winColumn=CreateWinePrefix, xStretch=True, yStretch=True, bcolor=GColors().purple7)   ],
        [   gc.GText(title="", xStretch=True)   ],
    ]

    wine_Run = [ 
        [   gc.GColumn(winColumn=wineBody, xStretch=True, yStretch=True, bcolor=GColors().purple7)   ]
    ]

    wine_debug = [
        [gc.GLog(xStretch=True, yStretch=True, bcolor=GnuChanOSColor().colors0)]
    ]

    wine_triks = [
        [gc.GMultiline(value="output", font="Sans, 12", xStretch=True, yStretch=True, readonly=True, bcolor=GnuChanOSColor().colors0)],
        [gc.GInput(value="input", font="Sans, 15", xStretch=True, bcolor=GColors().purple8)],
    ]

    layout = [ 
        [
            gc.GTabGroup(
                TabGroupLayout=[
                    [gc.GTab(title="Output", TabLayout=wine_debug, value="tab0")],
                    [gc.GTab(title="Help!", TabLayout=wine_triks, value="tab1")],

                    [gc.GTab(title="Create Wine", TabLayout=wine_Create, value="tab2")],
                    [gc.GTab(title="Run Wine", TabLayout=wine_Run, value="tab3")],
                      ], 
            value="tabG")
        ]
    ]

    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(windowValue="gamelist_create", border=1)
    gc.GListBoxBorderSize(windowValue="gamelist_run", border=1)

    gc.window["gamelist_create"].update(gamelist)
    gc.window["gamelist_run"].update(gamelist)

    class gcWine:
        def __init__(self) -> None:
            self.winePrefix_List = gamelist
            gc.window["gamelist_create"].update(self.winePrefix_List)
            gc.window["gamelist_run"].update(self.winePrefix_List)

            self.Path = f"{os.path.expanduser("~")}/Games/winePrefix/"
            self._currentPosition = None
            self._exe = None
            self.winePrefix = None
            self._WinePrefix = None
            self.game = None

        def CreatePrefix(self):
            try:
                if len(str(gc.GetValues["path_wine"]).strip(" ")) > 0:
                    createDir = f"mkdir -p {self.Path}{str(gc.GetValues["path_wine"]).strip(" ")}"
                    os.popen(createDir)
                    if self.winePrefix == 32:
                        _32bitPath = os.path.expanduser(f"{self.Path}{str(gc.GetValues["path_wine"]).strip(" ")}")
                        createPath = f"WINEPREFIX={_32bitPath} WINEARCH=win32 wine winecfg"
                        os.popen(createPath)
                        self._WinePrefix = _32bitPath
                        print(f"32_bit Wine Prefix Creating is Finish: {createPath}")
                    elif self.winePrefix == 64:
                        _64bitPath = os.path.expanduser(f"{self.Path}{str(gc.GetValues["path_wine"]).strip(" ")}")
                        createPath = f"WINEPREFIX={_64bitPath} WINEARCH=win64 wine winecfg"
                        os.popen(createPath)
                        self._WinePrefix = _64bitPath
                        print(f"64_bit Wine Prefix Creating is Finish: {createPath}")
                    else:
                        gc.GMessage(wmTitle="Warning!", message="Choose Wine Prefix 32Bit/64Bit")

                    if self.winePrefix != None:
                        if self._WinePrefix not in self.winePrefix_List:
                            self.winePrefix_List.append(self._WinePrefix)
                        _file_path = os.path.expanduser(f"{os.path.expanduser("~")}/.config/qtile/Programs/gamelist.py")
                        with open(_file_path, 'w') as file:
                            file.write(f"gamelist = {gamelist}")
                        gc.window["gamelist_create"].update(gamelist)
                        gc.window["gamelist_run"].update(gamelist)
                        print(f"Wine Prefix List: {self.winePrefix_List}")
                else:
                    print(str(gc.GetValues["path_wine"]).strip(" "))
            except Exception as ERR:
                print(ERR)


        def RemovePrefix(self):
            try:
                self.winePrefix_List.remove(gc.GetValues["gamelist_run"][0])
                gc.window["gamelist_run"].update(showPath.winePrefix_List)
                _removeThis = f"rm -r {str(gc.GetValues["gamelist_run"][0])}"
                os.popen(_removeThis)
                file_path = os.path.expanduser(f"{os.path.expanduser("~")}/.config/qtile/Programs/gamelist.py")
                with open(file_path, 'w') as file:
                    file.write(f"gamelist = {gamelist}")
                    gc.window["gamelist_run"].update(gamelist)
                    gc.window["gamelist_create"].update(gamelist)
                print(f"Remove Finish!: {_removeThis}")
            except Exception as ERR:
                print(ERR)

        def wineTRICKS(self):
            if len(str(gc.GetValues["gamelist_run"]).strip("[]'")) > 0:
                choose = str(gc.GetValues["gamelist_run"]).strip("[]'")
                _Winetriks = f"WINEPREFIX={choose} winetricks"
                os.popen(_Winetriks)
                print(f"WineTriks Opening: {_Winetriks}")
            else:
                print("first Choose Wine prefix")

        def wineCFG(self):
            if len(str(gc.GetValues["gamelist_run"]).strip("[]'")) > 0:
                choose = str(gc.GetValues["gamelist_run"]).strip("[]'")
                _Winecfg = f"WINEPREFIX={choose} winecfg"
                os.popen(_Winecfg)
                print(f"WineCFG Opening: {_Winecfg}")
            else:
                print("first Choose Wine prefix")

        def ChooseGame(self):
            try:
                if len(str(gc.GetValues["gamelist_run"]).strip("[]'")) > 0:
                    try:
                        self.game = gc.GetFilePath(defaultPATH=str(gc.GetValues["gamelist_run"]).strip("[]'") )
                    except Exception as ERR:
                        print(ERR)

                    # fake workers
                    _pass = str(self.game).split("/")
                    _exe = _pass[len(_pass)-1]
                    _pass.pop()

                    # last work old man!
                    self._exe = _exe.replace(" ", "\\ ")  # this take .exe name
                    _def = str(self.game).replace(_exe, " ")
                    self._currentPosition = os.chdir(f"{os.path.expanduser(_def.strip(" "))}") # auto os. location

                    # debug
                    print(f"{_def} | ")
                    print(f"this is test >>>>> {self._exe}")
                    print(f"you select Winfart game or program: \n{os.getcwd()}")
            except Exception as ERR:
                print(ERR)

        def PlayGame(self):
            try:
                _winePrefix = str(gc.GetValues["gamelist_run"]).strip("[]'")
                if str(self.game).endswith(".exe"):
                    #game_path = os.path.abspath(os.path.expanduser(str(self.game)))
                    # ( problem here i hope this is fix
                    _dir = os.path.dirname(os.path.abspath(__file__))
                    _Wine = f"WINEPREFIX={_winePrefix} primusrun gamemoderun mangohud --dlsym wine \"{str(self._exe)}\" > {_dir}/output.txt 2>&1"
                   
                    print(f"Game Or Program Start: {_Wine}")
                    os.popen(_Wine)
            except Exception as ERR:
                print(ERR)

        def UpdateWinePrefix(self):
            _UpdateWinePrefix_ = str(gc.GetValues["gamelist_run"]).strip("[]'")
            _wine = f"WINEPREFIX={_UpdateWinePrefix_} wineboot --update"
            print(f"WINEPREFIX={_UpdateWinePrefix_} wineboot --update")
            os.popen(_wine)

    showPath = gcWine()

    _output = "welcome to GnuChanOS Wine Manager!\nuse help command! \n"
    gc.window["output"].update(_output)
    def update():
        global showPath, _output

        if gc.event in ["32bit", "64bit"]:
            if gc.event == "32bit":
                showPath.winePrefix = 32
            elif gc.event == "64bit":
                showPath.winePrefix = 64

        #Thread(target=DownloadVideo, args=[]).start()
        if gc.event == "Create Prefix":
            Thread(target=showPath.CreatePrefix, args=[]).start()
        elif gc.event == "Run .EXE":
            showPath.ChooseGame()
            Thread(target=showPath.PlayGame, args=[]).start()
        elif gc.event == "Remove Prefix":
            Thread(target=showPath.RemovePrefix, args=[]).start()
        elif gc.event == "WineTRICKS":
            Thread(target=showPath.wineTRICKS, args=[]).start()
        elif gc.event == "WineCFG":
            Thread(target=showPath.wineCFG, args=[]).start()
        elif gc.event == "Update Prefix":
            Thread(target=showPath.UpdateWinePrefix, args=[]).start()

        # this is help!
        if gc.event == "Return:36":
            _command = gc.GetValues["input"]
            _output += _command + "\n"

            if _command == "help":
                _output += "this is help how i can help you!" + "\n"

            gc.window["output"].update(_output)
            gc.window["input"].update("")

    def BeforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=BeforeExit)
