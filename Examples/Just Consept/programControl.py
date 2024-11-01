import psutil

def checkIfProcessRunning(processName):
    for process in psutil.process_iter():
        try:
            if processName.lower() in process.name().lower():
                print(f"{processName} is running!")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("Program not running")
    return False
checkIfProcessRunning("qutebrowser")
