"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from PIL import Image
import io



if __name__ == "__main__":
    gc = GnuChanGUI(Title="Simple Image Viever", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    buttons = [
        [
            gc.GPush(GnuChanOSColor().colors2),
            gc.GVSep(Color=GnuChanOSColor().colors3),
            gc.GButton(Text="<"),
            gc.GButton(Text="Open Image"),
            gc.GButton(Text="Open Image Folder"),
            gc.GButton(Text=">"),
            gc.GVSep(Color=GnuChanOSColor().colors3),
            gc.GPush(GnuChanOSColor().colors2),
        ],
    ]

    showImage = [[gc.GCanvas(WindowValue="image", xStretch=True, yStretch=True, BColor="black")]]

    layout = [
        [   gc.GColumn(winColumnLayout_List=buttons, xStretch=True, BColor=GnuChanOSColor().colors2)   ],
        [   gc.GText(TextValue="path", xStretch=True)   ],
        [   gc.GPush(GnuChanOSColor().colors1)   ],
        [   gc.GColumn(winColumnLayout_List=showImage, xStretch=True, yStretch=True, EmptySpace=(0, 0)) ],
               ]

    gc.GWindow(SetMainWindowLayout_List=layout)
    gd = GCanvas(CanvasValue="image", Window=gc.GetWindow)


    _img = ""
    _imgs = []
    _index = 0
    _selectImage = ""
    def update():
        global _img, _imgs, _index, _selectImage, gd


        if gc.GetEvent == "Open Image":
            try:
                _defIMG = gc.GetFilePath(defaultPATH=str(os.path.expanduser("~")), fileTypes=gc.ImagesType)
                if str(_defIMG).endswith(".png") or str(_defIMG).endswith(".jpg"):
                    gd.ClearCanvas()
                    _img = gd.OpenImage(ImagePath=_defIMG, Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                    gd.AddImageObject(ObjectName="image", Image=_img, Transform=GVector2(0, 0), Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                    gd.Draw()

                    gc.GetWindow["path"].update(_defIMG)
            except Exception as ERR:
                print(ERR)

        elif gc.GetEvent == "Open Image Folder":
            try:
                _defFOLDER = gc.GetFolderPath(defaultPATH=str(os.path.expanduser("~")))
                _defFiles = os.listdir(os.path.expanduser(_defFOLDER))
                for i in _defFiles:
                    if str(i).endswith(".png") or str(i).endswith(".jpg"):
                        _imgs.append(f"{_defFOLDER}/{i}")
                _imgs.sort()
                gd.ClearCanvas()
                _img = gd.OpenImage(ImagePath=_imgs[0], Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                gd.AddImageObject(ObjectName="image", Image=_img, Transform=GVector2(0, 0), Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                gd.Draw()
                gc.GetWindow["path"].update(_imgs[0])
            except Exception as ERR:
                pass

        elif gc.GetEvent == "<":
            try:
                if _index > 0:
                    _index -= 1
                    _selectImage = _imgs[_index]
                    gd.ClearCanvas()
                    _img = gd.OpenImage(ImagePath=_selectImage, Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                    gd.AddImageObject(ObjectName="Image", Image=_img, Transform=GVector2(0, 0), Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                    gd.Draw()

                    gc.GetWindow["path"].update(_selectImage)

            except Exception as ERR:
                print(ERR)

        elif gc.GetEvent == ">":
            try:
                if _index < len(_imgs) - 1:
                    _index += 1
                    _selectImage = _imgs[_index]
                    _img = gd.OpenImage(ImagePath=_selectImage, Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                    gd.ClearCanvas()
                    gd.AddImageObject(ObjectName="Image", Image=_img, Transform=GVector2(0, 0), Scale=GVector2(gd.GetCanvasScale_X(), gd.GetCanvasScale_Y()))
                    gd.Draw()
                    gc.GetWindow["path"].update(_selectImage)
            except Exception as ERR:
                print(ERR)

    def BeforeExit():
        pass

    gc.SetUpdate(Update=update, exitBEFORE=BeforeExit)

