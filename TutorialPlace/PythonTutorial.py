def main():
    personels = []
    lineNumber = 0
    infoPersonalString = ""
    
    while True:
        command = input(":> ")
        if command == "add user":
            userName = input("Name: ").strip()
            userjob = input("Job: ").strip()
            age = input("Age: ")
            personels.append([userName, age, userjob])

        elif command == "info":
            print(str(personels), "\n")

        elif command == "save":
            lineNumber = 0
            infoPersonalString = ""
            
            for a in personels:
                lineNumber += 1
                infoPersonalString += str(lineNumber) + ": " + "Name: " + str(a[0]) + " Age: " + str(a[1]) + " Job: " + str(a[2]) + "\n"
            
            with open("test.txt", "w") as file:
                file.write(infoPersonalString)
                print(infoPersonalString)
                file.close()
if __name__ == "__main__":
    main()
