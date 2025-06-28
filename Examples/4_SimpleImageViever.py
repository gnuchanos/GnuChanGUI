"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI, GCanvas
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors, GVector2
from GnuChanGUI import os

# Extra Lib


#Thread(target=DownloadVideo, args=[]).start()
class SimpleImageViever:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(1024, 655), resizable=True, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors





        # main window layout you can use column and frame in here
        self.buttons = [
            [
                self.GC.GPush(self.CGC.FColors2),
                self.GC.GButton(Text="<"),
                self.GC.GButton(Text="Open Image"),
                self.GC.GButton(Text="Open Image Folder"),
                self.GC.GButton(Text=">"),
                self.GC.GPush(self.CGC.FColors2),
            ],
        ]

        self.showImage = [[self.GC.GCanvas(SetValue="image", xStretch=True, yStretch=True, BColor=self.C.purple8)]]

        self.Layout = [
            [   self.GC.GColumn(winColumnLayout_List=self.buttons, xStretch=True, BColor=self.CGC.FColors2, EmptySpace=(0, 0))   ],
            [   self.GC.GText(SetText="Open Video!", SetValue="path", xStretch=True, BColor=self.CGC.FColors0, EmptySpace=(0, 0))   ],
            [   self.GC.GColumn(winColumnLayout_List=self.showImage, xStretch=True, yStretch=True, EmptySpace=(0, 0)) ],
                ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)



        # Call Function Here

        self.GD = GCanvas(CanvasValue="image", Window=self.GC.GetWindow)
        self._img = ""
        self._imgs = []
        self._index = 0
        self._selectImage = ""

        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects

        if self.GC.GetEvent == "Open Image":
            try:
                _defIMG = self.GC.GetFilePath(defaultPATH=str(os.path.expanduser("~")), fileTypes=self.GC.ImagesType)
                if str(_defIMG).endswith(".png") or str(_defIMG).endswith(".jpg"):
                    self.GD.ClearCanvas()
                    self._img = self.GD.OpenImage(ImagePath=_defIMG, Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                    self.GD.AddImageObject(ObjectName="image", Image=self._img, Transform=GVector2(0, 0), Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                    self.GD.Draw()

                    self.GC.GetWindow["path"].update(_defIMG)
            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == "Open Image Folder":
            try:
                _defFOLDER = self.GC.GetFolderPath(defaultPATH=str(os.path.expanduser("~")))
                _defFiles = os.listdir(os.path.expanduser(_defFOLDER))
                for i in _defFiles:
                    if str(i).endswith(".png") or str(i).endswith(".jpg"):
                        self._imgs.append(f"{_defFOLDER}/{i}")
                self._imgs.sort()
                self.GD.ClearCanvas()
                self._img = self.GD.OpenImage(ImagePath=self._imgs[0], Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                self.GD.AddImageObject(ObjectName="image", Image=self._img, Transform=GVector2(0, 0), Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                self.GD.Draw()
                self.GC.GetWindow["path"].update(self._imgs[0])
            except Exception as ERR:
                pass

        elif self.GC.GetEvent == "<":
            try:
                if self._index > 0:
                    self._index -= 1
                    self._selectImage = self._imgs[self._index]
                    self.GD.ClearCanvas()
                    self._img = self.GD.OpenImage(ImagePath=self._selectImage, Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                    self.GD.AddImageObject(ObjectName="Image", Image=self._img, Transform=GVector2(0, 0), Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                    self.GD.Draw()

                    self.GC.GetWindow["path"].update(self._selectImage)

            except Exception as ERR:
                print(ERR)

        elif self.GC.GetEvent == ">":
            try:
                if self._index < len(self._imgs) - 1:
                    self._index += 1
                    self._selectImage = self._imgs[self._index]
                    self._img = self.GD.OpenImage(ImagePath=self._selectImage, Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                    self.GD.ClearCanvas()
                    self.GD.AddImageObject(ObjectName="Image", Image=self._img, Transform=GVector2(0, 0), Scale=GVector2(self.GD.GetCanvasScale_X(), self.GD.GetCanvasScale_Y()))
                    self.GD.Draw()
                    self.GC.GetWindow["path"].update(self._selectImage)
            except Exception as ERR:
                print(ERR)

    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleImageViever()
