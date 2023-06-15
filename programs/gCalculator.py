from GnuChanGUI import *


def main():
    default = GnuChanGUI(Title="GnuChan Program Calculator", Size=(650,600), resizable=True)
    default.Theme()

    defaultFont = "Sans, 20"
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    mathSymbolList = ["+","-","*","/"]
    mathEndSymbol = ["CLEAR", "GO"]
    
    mathSymbol = ""
    number1 = number2 = mathEnd = mathLog = equel = ""

    number1True = True
    mathEndNow = False

    inputMath = ""
    inputMathEnd = 0
    

    middleWin1 = [
        [default.GText(title=mathLog, font=defaultFont, value="math", xStretch=True, size=(35, None), border=0, position="center", bColor="#10011f")],
        [default.GButton("1", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("2", xStretch=True, yStretch=True, font=defaultFont),
         default.GButton("3", xStretch=True, yStretch=True, font=defaultFont)],

        [default.GButton("4", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("5", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("6", xStretch=True, yStretch=True,  font=defaultFont)],

        [default.GButton("7", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("8", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("9", xStretch=True, yStretch=True,  font=defaultFont)],
        
        [default.GButton("<R", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("0", xStretch=True, yStretch=True,  font=defaultFont)],

        [default.GButton("+", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("-", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("*", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("/", xStretch=True, yStretch=True,  font=defaultFont)],
        
        [default.GButton("=", value="finish", xStretch=True, yStretch=True,  font=defaultFont)],
        [default.GButton("GO", xStretch=True, yStretch=True,  font=defaultFont),
         default.GButton("CLEAR", xStretch=True, yStretch=True,  font=defaultFont)],
    ]

    middleWin2 = [
        [default.GText(inputMath, font=defaultFont, value="mathEndInput", xStretch=True, position="center", bColor="#10011f")],
        
        [default.GText("Number1", font=defaultFont, position="center"),
         default.GInput(font=defaultFont, value="Inputnumber1", xStretch=True, size=(1,20))],

        [default.GText("Number2", font=defaultFont, position="center"),
         default.GInput(font=defaultFont, value="Inputnumber2", xStretch=True, size=(1,20))],
        
        [default.GText("| + | - | * | / |", font=defaultFont, position="center"),
         default.GInput(font=defaultFont, value="InputMath", xStretch=True, size=(1,20))],
        
        [default.GButton("Input CLEAR", xStretch=True, font=defaultFont),
         default.GButton("=", value="finishInput", xStretch=True, font=defaultFont),
          default.GButton("Input GO", xStretch=True, font=defaultFont)],
        
        [default.GText(title="", xStretch=True)],
        [default.GText(title="You Can Note and why not")],
        [default.GMultiline(value="noteLog", font=defaultFont, xStretch=True, yStretch=True)],
        [default.GText(value="fileName", font=defaultFont, xStretch=True)]
    ]

    gMenu = [
        ["Log File", ["Open Log File", "Save Log File"]],
        ["Info", ["GnuChanOS", "Youtube Channel", "Github Page"]],
        ["System", ["Exit"]]
]

    layout = [
        [default.GMenuForTheme(winMenu=gMenu, font="Sans, 16")],
        [default.GColumn(winColumn=middleWin1, xStretch=True, yStretch=True),
         default.GColumn(winColumn=middleWin2, xStretch=True, yStretch=True)]
    ]

    default.GWindow(mainWindow=layout)


    while True:
        event, GetValues = default.window.read()
        if event == WIN_CLOSED:
            break
        if event == "Exit":
            break


        if mathEndNow == False:
            if event in numbers:
                if number1True == True:
                    number1 += event
                else:
                    number2 += event

            if number1True == True:
                if event == "<R":
                    number1 = number1[:-1]
            else:
                if event == "<R":
                    number2 = number2[:-1]

                
            if event in mathSymbolList:
                mathSymbol = event
                number1True = False
            if event == "finish":
                mathEndNow = True
        if mathEndNow == True:
            if mathSymbol == "+":
                mathEnd = float(number1) + float(number2)
                number1True = True
            elif mathSymbol == "-":
                mathEnd = float(number1) - float(number2)
                number1True = True
            elif mathSymbol == "*":
                mathEnd = float(number1) * float(number2)
                number1True = True
            elif mathSymbol == "/":
                mathEnd = float(number1) / float(number2)
                number1True = True
            
        if event in mathEndSymbol:
            if event == "CLEAR":
                number1 = number2 = mathEnd = mathLog = equel = mathSymbol = ""
                number1True = True
                mathEndNow = False
            elif event == "GO":
                number1 = str(round(mathEnd, 5))
                number2 = mathEnd = mathLog = equel = mathSymbol = ""
                number1True = True
                mathEndNow = False

        mathLog = f"{number1} {mathSymbol} {number2} {equel} {mathEnd}"
        default.window["math"].update(mathLog)


        if event == "finishInput":
            if GetValues["Inputnumber1"] != "" and GetValues["Inputnumber2"] != "":
                inputNumber1 = float(GetValues["Inputnumber1"])
                inputNumber2 = float(GetValues["Inputnumber2"])

                inputMathSybol = ""
                if GetValues["InputMath"] in mathSymbolList:
                    inputMathSybol =  GetValues["InputMath"]
                    if  GetValues["InputMath"] == "+":
                        inputMathEnd = inputNumber1 + inputNumber2
                    if  GetValues["InputMath"] == "*":
                        inputMathEnd = inputNumber1 * inputNumber2
                    if  GetValues["InputMath"] == "/":
                        inputMathEnd = inputNumber1 / inputNumber2
                    if  GetValues["InputMath"] == "-":
                        inputMathEnd = inputNumber1 - inputNumber2

                inputMath = f"{inputNumber1} {inputMathSybol} {inputNumber2} = {inputMathEnd}"
                default.window["mathEndInput"].update(inputMath)

        xfile = FileSave(value="noteLog", filepath="fileName", getValue=GetValues, window=default.window)
        if event == "Open Log File":
            xfile.Open
        elif event == "Save Log File":
            xfile.SaveAs

    default.window.close()
if __name__ == "__main__":
    main()