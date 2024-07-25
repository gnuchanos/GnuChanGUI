"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread
from shapely.geometry import box



#Thread(target=DownloadVideo, args=[]).start()



if __name__ == "__main__":
    gc = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    layout = [ 
        [gc.GText(value="debug", xStretch=True, position="center")],
        [
            gc.Push,
            gc.GButton(title="Play"),
            gc.Push,
        ],
        [Canvas(key="canvas", expand_x=True, expand_y=True, background_color=GColors().black)]
               ]

    gc.GWindow(mainWindow=layout)
    cc = GKeyboard(gc.window, event=gc.event)
    aa = GCanvas(CanvasValue="canvas", Window=gc.window)

    _Image = aa.OpenImage(ImagePath=f"{os.path.expanduser("~")}/dd.png", Scale=GVector2(aa.GetCanvasScale_X(), aa.GetCanvasScale_Y()))
    bg = aa.AddImageObject(Transform=GVector2(0, 0), Image=_Image)

    player = aa.AddRectangleObject( Transform=GVector2(aa.GetCanvasScale_X()/2-50, aa.GetCanvasScale_Y()/2-50), Scale=GVector2(50, 50), FillColor=GColors().blue1, OutLineColor=GColors().blue8 )
    player_Transform = aa.SelectObject(Object=player, Parameter0="transform")
    player_scale = aa.SelectObject(Object=player, Parameter0="scale")

    a0 = aa.AddRectangleObject(Transform=GVector2(100, 100), Scale=GVector2(50, 100), FillColor=GColors().purple1, OutLineColor=GColors().purple2),
    a1 = aa.AddRectangleObject(Transform=GVector2(200, 100), Scale=GVector2(50, 50), FillColor=GColors().purple1, OutLineColor=GColors().purple2),
    a2 = aa.AddRectangleObject(Transform=GVector2(300, 100), Scale=GVector2(50, 50), FillColor=GColors().purple1, OutLineColor=GColors().purple2),
    a3 = aa.AddRectangleObject(Transform=GVector2(400, 100), Scale=GVector2(50, 50), FillColor=GColors().purple1, OutLineColor=GColors().purple2),
    a4 = aa.AddRectangleObject(Transform=GVector2(500, 100), Scale=GVector2(50, 50), FillColor=GColors().purple1, OutLineColor=GColors().purple2),
    a5 = aa.AddRectangleObject(Transform=GVector2(600, 100), Scale=GVector2(50, 50), FillColor=GColors().purple1, OutLineColor=GColors().purple2),
    a6 = aa.AddRectangleObject(Transform=GVector2(700, 100), Scale=GVector2(50, 50), FillColor=GColors().purple1, OutLineColor=GColors().purple2),



    _notHitPose = GVector2(0, 0)
    _play = False
    _hit = False
    def update():
        global cc, aa
        global _hit, _play
        global _notHitPose, _Image

        if gc.event == "Play":
            _play = True

        if _play:
            if gc.event == cc.d:
                aa.MoveRectangleX_withUpdate(Object=player, Position="right", Speed=100)
            elif gc.event == cc.a:
                aa.MoveRectangleX_withUpdate(Object=player, Position="left", Speed=100)
            if gc.event == cc.w:
                aa.MoveRectangleY_withUpdate(Object=player, Position="up", Speed=100)
            elif gc.event == cc.s:
                aa.MoveRectangleY_withUpdate(Object=player, Position="down", Speed=100)


            collisionList = [a0, a1, a2, a3, a4, a5, a6]
            aa.RectangleCollisionCheck(Player=player, SolidObjectList=collisionList, notHitBeforePlayerTransform=_notHitPose)


            aa.Draw()

    def beforeExit():
        pass

    gc.update(GUpdate=update, exitBEFORE=beforeExit, timeout=1)