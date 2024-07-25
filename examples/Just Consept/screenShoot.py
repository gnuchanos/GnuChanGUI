import os
import datetime, time

# get the current date and time
now = str(datetime.datetime.now()).split(" ")
inDay = now[0]
inTime = now[1][0:8].replace(":", "_")
inDay_inTime = f"{inDay}-{inTime}"

Dir = os.path.expanduser("~")
filePath = f"{Dir}/screenshot_{inDay_inTime}.png"

_def = "ffmpeg -y -f x11grab -s 1024x768 -i :0.0 -vframes 1"
os.popen(f"{_def} {filePath}")


