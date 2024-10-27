import time
from threading import Thread

class GTimer:
    def __init__(self) -> None:
        self.StartNow = False
        self.ReturnTimerSecond = 0.0
        self.StartTime = 0.0

    def ReturnTime(self):
        if not self.StartNow:
            self.StartTime = time.time()
            self.StartNow = True

        while True:
            self.Second = int(time.time() - self.StartTime)       
            self.Minute = int(self.Second / 60)
            self.Hour   = int(self.Minute / 60)
            print(self.Second)

    def Update(self):
        self.ReturnTime()
        Thread(target=self.ReturnTime).start()
    
gc = GTimer()
defaultTimer = 0
gc.Update()
defaultTimer = gc.ReturnTimerSecond



