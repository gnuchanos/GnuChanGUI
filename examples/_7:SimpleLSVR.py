"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""


from GnuChanGUI import *
from threading import Thread
from datetime import datetime


"""
if [ "$#" -ne 3 ]; then
    echo "usage: restream-stream.sh <window_id> <fps> <livestream_key>"
    exit 1
fi

active_sink="$(pactl get-default-sink).monitor"
gpu-screen-recorder -w "$1" -c flv -f "$2" -q high -a "$active_sink" -o "rtmp://live.restream.io/live/$3"
"""

if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(1024, 655), resizable=True, finalize=True)
    gc.font = "Sans, 12"
    Themecolors().GnuChanOS

    win = [
        [   gc.GText(title="This Is First Version gpu-screen-recorder GUI", xStretch=True, position="center", font=gc.font)   ],
        [   gc.GText(title="Video or LiveStream Time", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [   gc.GText(title="0:0:0", value="time", xStretch=True, position="center", font="Sans, 20")   ],
        [   gc.GText(title="Video or LiveStream Time", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [   gc.hsep,   ],
        [   gc.GText(title="Video FPS", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [
            gc.Push,
            gc.GRadio(value="14", groupID="fps", title="14-FPS", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="24", groupID="fps", title="24-FPS", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="30", groupID="fps", title="30-FPS", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="60", groupID="fps", title="60-FPS", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="120", groupID="fps", title="120-FPS", bcolor=GColors().purple7, font=gc.font),
            gc.Push,
        ],
        [   gc.GText(title="Sound Quality", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [
            gc.Push,
            gc.GRadio(value="128", groupID="Kbps", title="128 Kbps", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="192", groupID="Kbps", title="192 Kbps", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="256", groupID="Kbps", title="256 Kbps", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="320", groupID="Kbps", title="320 Kbps", bcolor=GColors().purple7, font=gc.font),
            gc.Push,
        ],
        [   gc.GText(title="Video Quality", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [
            gc.Push,
            gc.GRadio(value="Medium", groupID="quality", title="Medium", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="high", groupID="quality", title="High", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="very_high", groupID="quality", title="Very High", bcolor=GColors().purple7, font=gc.font),
            gc.GRadio(value="ultra", groupID="quality", title="Ultra", bcolor=GColors().purple7, font=gc.font),
            gc.Push,
        ],
        [   gc.GText(title="Monutor ID 'xrandr here': ", font=gc.font),
            gc.GInput(value="mID", xStretch=True, size=(20, None), font=gc.font)
        ],
        [
            gc.GText(title="Micraphone Device ID: ", font="Sans, 15"), gc.GInput(value="mic", xStretch=True, size=(20, None), font="Sans, 15"),
        ],
        [
            gc.GText(title="Desktop Sound Device ID: ", font="Sans, 15"), gc.GInput(value="desk", xStretch=True, size=(20, None), font="Sans, 15"),
        ],
        [   gc.GText(title="Live Stream Settings", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [   gc.GText(title="RTMP URL: ", font=gc.font),
            gc.GInput(value="rtmp", xStretch=True, size=(20, None), font=gc.font)
        ],
        [   gc.GText(title="Stream key: ", font=gc.font),
            gc.GInput(value="skey", xStretch=True, PwChars="*", size=(20, None), font=gc.font)
        ],
        [   
            gc.Push,
            gc.GButton(title="Save And Start Live Stream", font=gc.font), gc.GButton(title="Stop Live Stream", font=gc.font),
            gc.Push,
        ],
        [   gc.GText(title="Video Record", xStretch=True, position="center", bcolor=GColors().purple8, font=gc.font)   ],
        [   gc.GText(title="File Path Here!", value="path", xStretch=True, bcolor=GColors().purple7, font=gc.font)],
        [   gc.GText(title="Video Name: ", font=gc.font), gc.GInput(value="vname", size=(20, None), xStretch=True, font=gc.font)   ],
        [
            gc.Push,
                gc.GButton(title="Select Output Folder", font=gc.font),
                gc.GButton(title="Save And Start Record", font=gc.font),
                gc.GButton(title="Stop Record", font=gc.font),
            gc.Push,
        ]

    ]

    layout = [ 
        [   
            gc.vsep,
            gc.GColumn(winColumn=win, xStretch=True, yStretch=True),
            gc.vsep,
        ]
               ]

    gc.GWindow(mainWindow=layout)

    _rtmp = _key = _monutorID = _fps = _quality = _sound = ""
    _path = _videoName = ""
    _Start = False
    _desktop = "$(pactl get-default-sink).monitor"
    _mic = "alsa_input.usb-Generic_USB2.0_PC_CAMERA_20100331010203-02.mono-fallback"
    _now = datetime.now()

    gc.window["rtmp"].update("rtmp://live.restream.io/live")
    gc.window["mID"].update("VGA1")
    gc.window["mic"].update(_mic)
    gc.window["desk"].update(_desktop)

    def LiveStream():
        global _rtmp, _key, _monutorID, _fps, _quality, _sound, _path, _videoName, _Start, _now, _mic, _desktop
        if gc.event in ["14", "24", "30", "60", "120"]:
            _fps = gc.event
        if gc.event in ["Medium", "high", "very_high", "ultra"]:
            _quality = str(gc.event).lower()
        if gc.event in ["128", "192", "256", "320"]:
            _sound = gc.event
        elif gc.event == "Save And Start Live Stream":
            _rtmp = gc.GetValues["rtmp"]
            _key = gc.GetValues["skey"]
            _monutorID = gc.GetValues["mID"]
            _desktop = gc.GetValues["desk"]
            _mic = gc.GetValues["mic"]

            _desktop = "$(pactl get-default-sink).monitor"
            _mic = "alsa_input.usb-Generic_USB2.0_PC_CAMERA_20100331010203-02.mono-fallback"

            try:
                if _rtmp and _key and _fps and _quality and _sound != "":
                    if not _Start:
                        _liveStream = f"gpu-screen-recorder -w {_monutorID} -k h264 -ac aac -c flv -a {_mic}\\|{_desktop} -f {_fps} -q {_quality} -ab {_sound}000 -o {_rtmp}/{_key}"
                        os.popen(_liveStream)
                        os.popen("notify-send -t 3500 -u low \"Live Stream is Starting!\"")
                        _Start = True
            except Exception as ERR:
                print(ERR)

        elif gc.event == "Stop Live Stream":
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 3500 -u low \"Work Is Finish!\"")
            _Start = False

    def RecordVideo():
        global _monutorID, _fps, _quality, _sound, _videoName, _Start, _path, _desktop, _mic
        _monutorID = gc.GetValues["mID"]
        _videoName = gc.GetValues["vname"]
        if gc.event in ["14", "24", "30", "60", "120"]:
            _fps = gc.event
        if gc.event in ["Medium", "high", "very_high", "ultra"]:
            _quality = str(gc.event).lower()
        if gc.event in ["128", "192", "256", "320"]:
            _sound = gc.event

        if gc.event == "Save And Start Record":
            if _path and _videoName and _monutorID and _fps and _quality and _sound != "":
                if not _Start:
                    # change this place for your device
                    _desktop = "$(pactl get-default-sink).monitor"
                    _mic = "alsa_input.usb-Generic_USB2.0_PC_CAMERA_20100331010203-02.mono-fallback"

                    _now = datetime.now()
                    _FileName = f"{_now.year}-{_now.month}-{_now.day}_{_now.hour}-{_now.minute}-{_now.second}"

                    _VideoRecord = f"gpu-screen-recorder -w {_monutorID} -k h264 -ac aac -c flv -a {_mic}\\|{_desktop} -f {_fps} -q {_quality} -ab {_sound}000 -o {_path}/{str(_videoName).replace(" ", "\\ ")}_{_FileName}.mkv"
                    os.popen(_VideoRecord)
                    os.popen("notify-send -t 3500 -u low \"Video Recording is Starting\"")
                    _Start = True

        elif gc.event == "Stop Record":
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 3500 -u low \"Work Is Finish!\"")
            _Start = False

    _second = _minute = _hour = 0
    _sec = time.monotonic()

    def update():
        global _path
        if gc.event == "Select Output Folder":
            _path = popup_get_folder(no_window=True, title="Warning!", message="Select Output Folder For Recording Video")
            gc.window["path"].update(_path)
            print(_path)

        Thread(target=LiveStream, args=[]).start()
        Thread(target=RecordVideo, args=[]).start()

        global _second, _minute, _hour, _Start, _sec
        if _Start:
            if _second < 60:
                _second += gc.dt
            else:
                if _minute != 60:
                    _minute += 1
                else:
                    _hour += 1
                    _minute = 0
                _second = 0
        else:
            _second = _minute = _hour = 0
        gc.window["time"].update(f"{_hour}:{_minute}:{int(_second)}")

    def LastWorkBeforeExit():
        global _Start
        if _sound:
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 3500 -u low \"Work Is Finish!\"")
            _Start = False

    gc.update(GUpdate=update, exitBEFORE=LastWorkBeforeExit)
