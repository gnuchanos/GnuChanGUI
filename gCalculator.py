from GnuChanGUI import *


def main():
    default = GnuChanGUI(Title="GnuChan Program Runner", Size=(650,600), resizable=False)
    default.Theme()

    defaultFont = "Sans, 20"
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    mathSymbol = ["+","-","*","/"]
    mathEndSymbol = ["CLEAR", "=", "GO"]

    number1 = number2 = mathEnd = mathLog = equel = ""
    numberTypingLog = ""
    singleMathSybol = ""

    number1True = True
    mathEndNow = False
    

    topWin = [
        [default.GText(title=mathLog, font=defaultFont, value="math", xStretch=True, border=0, position="center", bColor="#10011f")],
        [default.GText(title=numberTypingLog, font=defaultFont, value="minfo", xStretch=True, border=0, position="center", bColor="#220242")],
    ]

    middleWin1 = [
        [default.GButton("1", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("2", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("3", xStretch=True, yStretch=True, font=defaultFont)],

        [default.GButton("4", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("5", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("6", xStretch=True, yStretch=True,  font=defaultFont)],

        [default.GButton("7", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("8", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("9", xStretch=True, yStretch=True,  font=defaultFont)],
        
        [default.GButton("R", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("0", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("D", xStretch=True, yStretch=True,  font=defaultFont)],

        [default.GButton("+", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("-", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("*", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("/", xStretch=True, yStretch=True,  font=defaultFont)],
        
        [default.GButton("=", xStretch=True, yStretch=True,  font=defaultFont)],
        [default.GButton("GO", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("CLEAR", xStretch=True, yStretch=True,  font=defaultFont)],
    ]

    gMenu = [["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
             ["System", ["Exit"]]]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GColumn(winColumn=topWin, xStretch=True)],
        [default.GColumn(winColumn=middleWin1, xStretch=True, yStretch=True)]
    ]

    default.GWindow(mainWindow=layout)


    while True:
        event, GetValues = default.window.read()
        if event == WIN_CLOSED:
            break
        if event == "Exit":
            break

        if event in numbers and mathEndNow == False:
            if number1True == True:
                number1 += event
                numberTypingLog = "Number1 is typing now"
                default.window["minfo"].update(numberTypingLog)
            else:
                number2 += event
                numberTypingLog = "Number1 is typing now"
                default.window["minfo"].update(numberTypingLog)

        if event in mathSymbol and mathEndNow == False:
            singleMathSybol = event
            number1True = False

        if event in mathEndSymbol and mathEndNow == False:
            equel = "="
            if number1True == False:
                if singleMathSybol == "+":
                    mathEnd = float(number1) + float(number2)
                    mathEndNow = True
                elif singleMathSybol == "-":
                    mathEnd = float(number1) - float(number2)
                    mathEndNow = True
                elif singleMathSybol == "*":
                    mathEnd = float(number1) * float(number2)
                    mathEndNow = True
                elif singleMathSybol == "/":
                    mathEnd = float(number1) / float(number2)
                    mathEndNow = True


        mathLog = f"{number1} {singleMathSybol} {number2} {equel} {mathEnd}"
        default.window["math"].update(mathLog)

    default.window.close()
if __name__ == "__main__":
    main()