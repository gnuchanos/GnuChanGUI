"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# Don't do like this from lib import * for gnchangui
from GnuChanGUI import GnuChanGUI
from GnuChanGUI import GnuChanOSColor, GColors, Themecolors


# Extra Lib
from numpy import number

#Thread(target=DownloadVideo, args=[]).start()
class SimpleCalculator:
    def __init__(self) -> None:
        self.GC = GnuChanGUI(Title=" UwU ", Size=(500, 655), resizable=False, finalize=True)
        Themecolors().GnuChanOS        # you can change theme color
        self.C = GColors()             # all color in here
        self.CGC = GnuChanOSColor()    # gnuchanos colors


        # main window layout you can use column and frame in here
        self.Layout = [
            [self.GC.GText(SetText="Let's Start Math", SetValue="math", xStretch=True, TPosition="center", BColor=self.CGC.FColors0)],
            [self.gb(text="1"), self.gb(text="2"), self.gb(text="3"), self.gb(text="+")],
            [self.gb(text="4"), self.gb(text="5"), self.gb(text="6"), self.gb(text="-")],
            [self.gb(text="7"), self.gb(text="8"), self.gb(text="9"), self.gb(text="*")],
            [self.gb(text="<"), self.gb(text="0"), self.gb(text="."), self.gb(text="/")],
            [
                self.GC.GButton(Text="CLEAN", xStretch=True), 
                self.GC.GButton(Text="GO", xStretch=True),
                self.GC.GButton(Text="CLEAR LOG", xStretch=True),
            ],
            [self.gb(text="=")],
            [self.GC.GListBox(SetValue="output", xStretch=True, yStretch=True, LPosition="center", noScroolBar=True, BColor=self.CGC.SColors0)]
        ]

        self.GC.GWindow(SetMainWindowLayout_List=self.Layout)


        # Call Function Here
        self.GC.GListBoxBorderSize(WindowValue="output", Border=0)

        # Variables
        self.Number0: str = ""
        self.Number1: str = ""
        self.MathFinish: bool = False
        self.Number1Typing: bool = True
        self.Numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.')
        self.MathSymbols: tuple = ('+', '-', '*', '/')
        self.CurrentMathSymbol: str = ""
        self.MathEnd: float = 0
        self.MathList = []


        # Call Function Here
        self.GC.SetUpdate(Update=self.Update, exitBEFORE=self.BeforeExit)
    
    def gb(self, text: str):
        return self.GC.GButton(Text=text, xStretch=True, Size=(2, None))

    def Update(self):
        #self.GC.GetEvent == "event" -> window event
        #self.GC.GetWindow["text"].update("this text") -> update window objects

        if not self.MathFinish:
            if self.GC.GetEvent in self.Numbers:
                # add number
                if self.Number1Typing:
                    self.Number0 += self.GC.GetEvent
                    self.GC.GetWindow["math"].update(self.Number0)
                else:
                    self.Number1 += self.GC.GetEvent
                    self.GC.GetWindow["math"].update(self.Number1)

            # remove number
            if self.GC.GetEvent == '<':
                if self.Number1Typing:
                    self.Number0 = self.Number0[:-1]
                    self.GC.GetWindow["math"].update(self.Number0)
                else:
                    self.Number1 = self.Number1[:-1]
                    self.GC.GetWindow["math"].update(self.Number1)
            
            # math
            if self.GC.GetEvent in self.MathSymbols:
                if self.Number1Typing:
                    self.Number1Typing = False
                    self.CurrentMathSymbol = self.GC.GetEvent

            if self.GC.GetEvent == "=":
                if not self.Number1Typing:
                    if self.CurrentMathSymbol == "+":
                        self.MathEnd = float(self.Number0) + float(self.Number1)
                        self.GC.GetWindow["math"].update(round(self.MathEnd, 5))
                        self.MathFinish = True
                        
                        self.MathList.append(self.MathEnd)
                        self.GC.GetWindow["output"].update(self.MathList)
                    elif self.CurrentMathSymbol == "-":
                        self.MathEnd = float(self.Number0) - float(self.Number1)
                        self.GC.GetWindow["math"].update(round(self.MathEnd, 5))
                        self.MathFinish = True

                        self.MathList.append(self.MathEnd)
                        self.GC.GetWindow["output"].update(self.MathList)
                    elif self.CurrentMathSymbol == "*":
                        self.MathEnd = float(self.Number0) * float(self.Number1)
                        self.GC.GetWindow["math"].update(round(self.MathEnd, 5))
                        self.MathFinish = True

                        self.MathList.append(self.MathEnd)
                        self.GC.GetWindow["output"].update(self.MathList)
                    elif self.CurrentMathSymbol == "/":
                        self.MathEnd = float(self.Number0) / float(self.Number1)
                        self.GC.GetWindow["math"].update(round(self.MathEnd, 5))
                        self.MathFinish = True

                        self.MathList.append(self.MathEnd)
                        self.GC.GetWindow["output"].update(self.MathList)

        if self.GC.GetEvent == "GO":
            self.Number1Typing = True
            self.Number0 = str(self.MathEnd)
            self.Number1 = self.CurrentMathSymbol = ""
            self.MathFinish = False
            self.GC.GetWindow["math"].update(self.Number0)

        elif self.GC.GetEvent == "CLEAN":
            self.Number1Typing = True
            self.Number0 = self.Number1 = self.CurrentMathSymbol = ""
            self.MathEnd = 0
            self.MathFinish = False
            self.GC.GetWindow["math"].update("Let's Start Math")
        
        elif self.GC.GetEvent == "CLEAR LOG":
            self.MathList.clear()
            self.GC.GetWindow["output"].update(self.MathList)




    def BeforeExit(self):
        print("Exit")

if __name__ == "__main__":
    gc = SimpleCalculator()
