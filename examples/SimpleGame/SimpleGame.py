"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
#Thread(target=DownloadVideo, args=[]).start()

class DefaultExample:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(900, 655), resizable=False, finalize=True)
        Themecolors().GnuChanOS

        self.text = ""

        self.Layout = [
            [self.GC.GCanvas(value="canvas", xStretch=True, yStretch=True)]            
        ]

        self.GC.GWindow(mainWindow=self.Layout)
        # KEYBOARD, CANVAS, GColors() 
        self.colors = GColors()
        self.KYB = GKeyboard(window=self.GC.window)
        self.KYB.AddMouseEvent(MouseTrigerValue="canvas")

        self.can = GCanvas(Window=self.GC.window, CanvasValue="canvas")

        self.CurrentLevel = 1
        self.CurrentScene = self.can.Scene_LOGO
        self.LogoTime = 2
        self.StartMusic = False

        # first start logo
        self.OpenImage = self.can.OpenImage(
                ImagePath="/home/archkubi/Github/gnuchangui/examples/Finish/SimpleGame/background.png", 
                Scale=GVector2(self.can.GetCanvasScale_X(), self.can.GetCanvasScale_Y())
        )
        self.bg = self.can.AddImageObject(
                ObjectName="background", Image=self.OpenImage, 
                Transform=GVector2(0, 0), 
                Scale=GVector2(self.can.GetCanvasScale_X(), self.can.GetCanvasScale_Y())
        )

        # menu GUI
        self.StartButton = self.can.AddRectangleObject(
            ObjectName="Start", Transform=GVector2(50, self.can.GetCanvasScale_Y()/2-50), 
            Scale=GVector2(200, 50), 
            FillColor=GColors().purple1, 
            OutLineColor=GColors().purple5,
            Active=False
        )

        self.StartButtonText = self.can.AddTextObject(
            ObjectName="Start Game Text",
            Text="Start Game", Font="Sans", Scale=25,
            Transform=GVector2(
                int(self.can.GetObjectPosition(Object=self.StartButton, xOrY='x')+self.can.GetObjectScale(Object=self.StartButton, xOrY='x')/2),
                int(self.can.GetObjectPosition(Object=self.StartButton, xOrY='y')+self.can.GetObjectScale(Object=self.StartButton, xOrY='y')/2)
            ),
            Active=False, Color=GColors().white
        )

        # First Level Object

        self.FirstLevelWarlls = (
            # top Left
            self.can.AddRectangleObject(
                ObjectName="wall_1", Active=False,
                Transform=GVector2(0, 0), Scale=GVector2(100, 50),
                FillColor=self.colors.purple8, OutLineColor=self.colors.purple5,
            ),
            # top Right
            self.can.AddRectangleObject(
                    ObjectName="wall_2", Active=False,
                    Transform=GVector2(200, 0), Scale=GVector2(self.can.GetCanvasScale_X()-200, 50),
                    FillColor=self.colors.purple8, OutLineColor=self.colors.purple5,
            ),
            # middle left
            self.can.AddRectangleObject(
                    ObjectName="wall_3", Active=False,
                    Transform=GVector2(0, 50), Scale=GVector2(50, self.can.GetCanvasScale_Y()-100),
                    FillColor=self.colors.purple8, OutLineColor=self.colors.purple5,
            ),
            # middle right
            self.can.AddRectangleObject(
                    ObjectName="wall_4", Active=False,
                    Transform=GVector2(self.can.GetCanvasScale_X()-50, 50), Scale=GVector2(50, self.can.GetCanvasScale_Y()-100),
                    FillColor=self.colors.purple8, OutLineColor=self.colors.purple5,
            ),
            # bottom
            self.can.AddRectangleObject(
                    ObjectName="wall_5", Active=False,
                    Transform=GVector2(0, self.can.GetCanvasScale_Y()-50), Scale=GVector2(self.can.GetCanvasScale_X(), 50),
                    FillColor=self.colors.purple8, OutLineColor=self.colors.purple5,
            ),
        )
        self.Door_0 = self.can.AddRectangleObject(
                ObjectName="door", Active=False,
                Transform=GVector2(100, 0), Scale=GVector2(100, 50),
                FillColor=self.colors.navy1, OutLineColor=self.colors.purple5 )
        self.Door_0_TrigerArea_obj = self.can.AddRectangleObject(
                ObjectName="door triger object", Active=False,
                Transform=GVector2(self.can.GetCanvasScale_X()-300, 50), Scale=GVector2(50, 50),
                FillColor=self.colors.pink1, OutLineColor=self.colors.purple5 )
        self.Door_0_TrigerObject = self.can.AddRectangleObject(
                ObjectName="door triger area", Active=False,
                Transform=GVector2(self.can.GetCanvasScale_X()-300, 350), Scale=GVector2(50, 50),
                FillColor=self.colors.pink8, OutLineColor=self.colors.purple5 )
        self.Door_0_Open = False
        self.Door_0_TrigetArea = False

        # First Level Object


        # Second Level Object
        self.GameOver = self.can.AddTextObject(
            ObjectName="textG",
            Text="Game Over", Font="Sans", Scale=100,
            Transform=GVector2(self.can.GetCanvasScale_X()/2, self.can.GetCanvasScale_Y()/2),
            Color=self.colors.purple1, Active=False
        )
        # Second Level Object

        _path = os.path.dirname(os.path.abspath(__file__))

        # Music List
        self.soundPlay = False
        self.GrabSound0 = f"{_path}/grab0.wav"
        self.GrabSound1 = f"{_path}/grab1.wav"
        self.GrabSound2 = f"{_path}/grab2.wav"
        self.doorOpenSound = f"{_path}/doorOpen.wav"
        self.Music = f"{_path}/music0.wav"
        self.Mixer = GMixer()
        self.musicStart = False
        # Music List


        # this is las object for render pipeline reasone
        self.Player = self.can.AddRectangleObject(
            ObjectName="Player", Active=False,
            Transform=GVector2(self.can.GetCanvasScale_X()/2-50, self.can.GetCanvasScale_Y()/2-50), Scale=GVector2(50, 50),
            FillColor=self.colors.purple1, OutLineColor=self.colors.purple7
        )
        self.PlayerGrab = False
        self.can.Draw()

        self.GC.update(GUpdate=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        if self.CurrentScene == self.can.Scene_LOGO:
            if self.LogoTime > 0:
                self.LogoTime -= 1
                print(self.LogoTime)
            else:
                self.LogoTime = 3
                self.CurrentScene = self.can.Scene_MENU #self.can.Scene_MENU
                self.CurrentLevel = 1
            self.can.Draw()


        elif self.CurrentScene == self.can.Scene_MENU:
            self.can.ReadMousePosition()
            self.can.ChangeObjectVisible(Object=self.bg, Visible=False)
            self.can.ChangeObjectVisible(Object=self.StartButton, Visible=True)
            self.can.ChangeObjectVisible(Object=self.StartButtonText, Visible=True)

            _StartButtonArea = self.can.CheckMouseInRectangle(
                mouse_x=self.can.MousePosition.x, mouse_y=self.can.MousePosition.y,
                rect_x=self.can.GetObjectPosition(Object=self.StartButton, xOrY='x'), rect_y=self.can.GetObjectPosition(Object=self.StartButton, xOrY='y'),
                rect_width=self.can.GetObjectScale(Object=self.StartButton, xOrY='x'), rect_height=self.can.GetObjectScale(Object=self.StartButton, xOrY='y')
            )

            if _StartButtonArea:
                if self.GC.event == self.KYB.LeftMouseKey:
                    self.CurrentScene = self.can.Scene_GAMEPLAY
                self.can.ChangeObjectColor(Object=self.StartButton, Color=GColors().purple1)
            else:
                self.can.ChangeObjectColor(Object=self.StartButton, Color=GColors().purple5)
            self.can.Draw()


        elif self.CurrentScene == self.can.Scene_GAMEPLAY:
            if self.CurrentLevel == 1:
                # unload Things -> Visible False
                # hide all old object
                self.can.ChangeObjectVisible(Object=self.bg, Visible=False)
                self.can.ChangeObjectVisible(Object=self.StartButton, Visible=False)
                self.can.ChangeObjectVisible(Object=self.StartButtonText, Visible=False)
                # show new objects
                self.can.ChangeObjectVisible(Object=self.Player, Visible=True)
                if not self.Door_0_Open:
                    self.can.ChangeObjectVisible(Object=self.Door_0, Visible=True)
                self.can.ChangeObjectVisible(Object=self.Door_0_TrigerArea_obj, Visible=True)
                self.can.ChangeObjectVisible(Object=self.Door_0_TrigerObject, Visible=True)
                for i in self.FirstLevelWarlls:
                    self.can.ChangeObjectVisible(Object=i, Visible=True)
                if not self.Door_0_Open:
                    _Door0Hit = self.can.SingleObject_RectangleCollisionCheck(Player=self.Player, SingleObject=self.Door_0)
                    if _Door0Hit:
                        self.can.stop = True
                        self.can.TeleportObject(Object=self.Player, Position=self.can.RecordY+5, XorY='y')
                    else:
                        self.can.stop = False

                # reset level
                if self.GC.event == self.KYB.r:
                    self.PlayerGrab = False
                    self.can.TeleportObject(Object=self.Player, Position=self.can.GetCanvasScale_X()/2-50, XorY='x')
                    self.can.TeleportObject(Object=self.Player, Position=self.can.GetCanvasScale_Y()/2-50, XorY='y')
                    self.can.TeleportObject(Object=self.Door_0_TrigerObject, Position=self.can.GetCanvasScale_X()-300, XorY='x')
                    self.can.TeleportObject(Object=self.Door_0_TrigerObject, Position=350, XorY='y')
                    self.can.ChangeObjectVisible(Object=self.Door_0, Visible=True)

                if not self.Door_0_Open:
                    _hitDoorArea = self.can.SingleObject_RectangleCollisionCheck(Player=self.Door_0_TrigerObject, SingleObject=self.Door_0_TrigerArea_obj)
                    _hitTriger = self.can.SingleObject_RectangleCollisionCheck(Player=self.Player, SingleObject=self.Door_0_TrigerObject)

                    if _hitTriger:
                        if self.GC.event == self.KYB.e and not self.PlayerGrab:
                            self.Mixer.PlaySound_MultiChannelNoLoop(SoundPath=self.GrabSound0, ChannelID=1)
                            self.PlayerGrab = True
                        elif self.GC.event == self.KYB.e and self.PlayerGrab:
                            self.Mixer.PlaySound_MultiChannelNoLoop(SoundPath=self.GrabSound1, ChannelID=1)
                            self.PlayerGrab = False

                    if not self.Door_0_Open:
                        if self.PlayerGrab:
                            self.can.TeleportObject(Object=self.Door_0_TrigerObject, Position=self.can.GetObjectPosition(Object=self.Player, xOrY='x'), XorY='x')
                            self.can.TeleportObject(Object=self.Door_0_TrigerObject, Position=self.can.GetObjectPosition(Object=self.Player, xOrY='y'), XorY='y')
                            if _hitDoorArea:
                                if not self.soundPlay:
                                    self.Mixer.PlaySound_MultiChannelNoLoop(SoundPath=self.GrabSound2, ChannelID=1)
                                    self.Mixer.PlaySound_MultiChannelNoLoop(SoundPath=self.doorOpenSound, ChannelID=2)
                                    self.soundPlay = True
                                self.PlayerGrab = False; 
                                self.Door_0_Open = True
                                self.can.TeleportObject(Object=self.Door_0_TrigerObject, Position=self.can.GetObjectPosition(Object=self.Door_0_TrigerArea_obj, xOrY='x'), XorY='x')
                                self.can.TeleportObject(Object=self.Door_0_TrigerObject, Position=self.can.GetObjectPosition(Object=self.Door_0_TrigerArea_obj, xOrY='y'), XorY='y')
                                self.can.ChangeObjectVisible(Object=self.Door_0, Visible=False)

                # leave the map
                if self.can.RecordY < 0:
                    self.CurrentLevel = 2

                self.Mixer.PlaySound_MultiChannelLoop(SoundPath=self.Music, Loop=True, ChannelID=0)

                self.can.SimplePlayer2D(Player=self.Player, Event=self.GC.event, Keyboard=self.KYB, SolidObjectList=self.FirstLevelWarlls)
                self.can.Draw()

            elif self.CurrentLevel == 2:
                # unload Things -> Visible False
                self.can.ChangeObjectVisible(Object=self.Door_0, Visible=False)
                self.can.ChangeObjectVisible(Object=self.Door_0_TrigerArea_obj, Visible=False)
                self.can.ChangeObjectVisible(Object=self.Door_0_TrigerObject, Visible=False)
                for i in self.FirstLevelWarlls:
                    self.can.ChangeObjectVisible(Object=i, Visible=False)
                # show new objects
                self.can.ChangeObjectVisible(Object=self.Player, Visible=True)


                self.can.SimplePlayer2D(Player=self.Player, Event=self.GC.event, Keyboard=self.KYB, SolidObjectList=())
                self.can.Draw()

        elif self.CurrentScene == self.can.Scene_End:
            pass

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = DefaultExample()
