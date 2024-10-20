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
        [   gc.GText(SetText="This Is First Version gpu-screen-recorder GUI", xStretch=True, TPosition="center", TFont=gc.font)   ],
        [   gc.GText(SetText="Video or LiveStream Time", xStretch=True, TPosition="center", BColor=GColors().purple8, TFont=gc.font)   ],
        [   gc.GText(SetText="0:0:0", TextValue="time", xStretch=True, TPosition="center", TFont="Sans, 20")   ],

        [   gc.GText(SetText="Video FPS", xStretch=True, TPosition="center", BColor=GColors().purple8, TFont=gc.font)   ],
        [
            gc.GPush(BColor=GnuChanOSColor().colors1),
            gc.GRadio(WindowValue="14", groupID="fps", RText="14-FPS", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="24", groupID="fps", RText="24-FPS", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="30", groupID="fps", RText="30-FPS", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="60", groupID="fps", RText="60-FPS", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="120", groupID="fps", RText="120-FPS", BColor=GColors().purple7, TFont=gc.font),
            gc.GPush(BColor=GnuChanOSColor().colors1),
        ],

        [   gc.GText(SetText="Sound Quality", xStretch=True, TPosition="center", BColor=GColors().purple8, TFont=gc.font)   ],
        [
            gc.GPush(BColor=GnuChanOSColor().colors1),
            gc.GRadio(WindowValue="128", groupID="Kbps", RText="128 Kbps", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="192", groupID="Kbps", RText="192 Kbps", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="256", groupID="Kbps", RText="256 Kbps", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="320", groupID="Kbps", RText="320 Kbps", BColor=GColors().purple7, TFont=gc.font),
            gc.GPush(BColor=GnuChanOSColor().colors1),
        ],

        [   gc.GText(SetText="Video Quality", xStretch=True, TPosition="center", BColor=GColors().purple8, TFont=gc.font)   ],
        [
            gc.GPush(BColor=GnuChanOSColor().colors1),
            gc.GRadio(WindowValue="Medium", groupID="quality", RText="Medium", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="high", groupID="quality", RText="High", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="very_high", groupID="quality", RText="Very High", BColor=GColors().purple7, TFont=gc.font),
            gc.GRadio(WindowValue="ultra", groupID="quality", RText="Ultra", BColor=GColors().purple7, TFont=gc.font),
            gc.GPush(BColor=GnuChanOSColor().colors1),
        ],
        [   gc.GText(SetText="Monutor ID 'xrandr here': ", TFont=gc.font),
            gc.GInput(WindowValue="mID", xStretch=True, Size=(20, None), TFont=gc.font)
        ],
        [
            gc.GText(SetText="Micraphone Device ID: ", TFont="Sans, 15"), gc.GInput(WindowValue="mic", xStretch=True, Size=(20, None), TFont="Sans, 15"),
        ],
        [
            gc.GText(SetText="Desktop Sound Device ID: ", TFont="Sans, 15"), gc.GInput(WindowValue="desk", xStretch=True, Size=(20, None), TFont="Sans, 15"),
        ],
        [   gc.GText(SetText="Live Stream Settings", xStretch=True, TPosition="center", BColor=GColors().purple8, TFont=gc.font)   ],
        [   gc.GText(SetText="RTMP URL: ", TFont=gc.font),
            gc.GInput(WindowValue="rtmp", xStretch=True, Size=(20, None), TFont=gc.font)
        ],
        [   gc.GText(SetText="Stream key: ", TFont=gc.font),
            gc.GInput(WindowValue="skey", xStretch=True, HidePassword="*", Size=(20, None), TFont=gc.font)
        ],
        [   
            gc.GPush(BColor=GnuChanOSColor().colors1),
            gc.GButton(Text="Save And Start Live Stream", TFont=gc.font), gc.GButton(Text="Stop Live Stream", TFont=gc.font),
            gc.GPush(BColor=GnuChanOSColor().colors1),
        ],
        [   gc.GText(SetText="Video Record", xStretch=True, TPosition="center", BColor=GColors().purple8, TFont=gc.font)   ],
        [   gc.GText(SetText="File Path Here!", TextValue="path", xStretch=True, BColor=GColors().purple7, TFont=gc.font)],
        [   gc.GText(SetText="Video Name: ", TFont=gc.font), gc.GInput(WindowValue="vname", Size=(20, None), xStretch=True, TFont=gc.font)   ],
        [
            gc.GPush(BColor=GnuChanOSColor().colors1),
                gc.GButton(Text="Select Output Folder", TFont=gc.font),
                gc.GButton(Text="Save And Start Record", TFont=gc.font),
                gc.GButton(Text="Stop Record", TFont=gc.font),
            gc.GPush(BColor=GnuChanOSColor().colors1),
        ]

    ]

    layout = [ 
        [   
            gc.GVSep(Color=GColors().black),
            gc.GColumn(winColumnLayout_List=win, xStretch=True, yStretch=True),
            gc.GVSep(Color=GColors().black),
        ]
            ]

    gc.GWindow(SetMainWindowLayout_List=layout)

    _rtmp = _key = _monutorID = _fps = _quality = _sound = ""
    _path = _videoName = ""
    _Start = False
    _desktop = "$(pactl get-default-sink).monitor"
    _mic = "alsa_input.usb-Generic_USB2.0_PC_CAMERA_20100331010203-02.mono-fallback"
    _now = datetime.now()
    _LiveOrRecordStart = False

    gc.GetWindow["rtmp"].update("rtmp://a.rtmp.youtube.com/live2")
    gc.GetWindow["mID"].update("VGA1")
    gc.GetWindow["mic"].update(_mic)
    gc.GetWindow["desk"].update(_desktop)

    def LiveStream():
        global _rtmp, _key, _monutorID, _fps, _quality, _sound, _path, _videoName, _Start, _now, _mic, _desktop, _LiveOrRecordStart
        if gc.GetEvent in ["14", "24", "30", "60", "120"]:
            _fps = gc.GetEvent
        if gc.GetEvent in ["Medium", "high", "very_high", "ultra"]:
            _quality = str(gc.GetEvent).lower()
        if gc.GetEvent in ["128", "192", "256", "320"]:
            _sound = gc.GetEvent
        elif gc.GetEvent == "Save And Start Live Stream":
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
                        _liveStream = f"gpu-screen-recorder -w {_monutorID} -k h264 -ac aac -c flv -a {_mic}\\|{_desktop} -f {_fps} -q {_quality} -ab {_sound} -o {_rtmp}/{_key}"
                        os.popen(_liveStream)
                        os.popen("notify-send -t 3500 -u low \"Live Stream is Starting!\"")
                        _Start = True
                        _LiveOrRecordStart = True
            except Exception as ERR:
                print(ERR)

        elif gc.GetEvent == "Stop Live Stream":
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 3500 -u low \"Work Is Finish!\"")
            _Start = False
            _LiveOrRecordStart = False

    def RecordVideo():
        global _monutorID, _fps, _quality, _sound, _videoName, _Start, _path, _desktop, _mic
        _monutorID = gc.GetValues["mID"]
        _videoName = gc.GetValues["vname"]
        if gc.GetEvent in ["14", "24", "30", "60", "120"]:
            _fps = gc.GetEvent
        if gc.GetEvent in ["Medium", "high", "very_high", "ultra"]:
            _quality = str(gc.GetEvent).lower()
        if gc.GetEvent in ["128", "192", "256", "320"]:
            _sound = gc.GetEvent

        if gc.GetEvent == "Save And Start Record":
            if _path and _videoName and _monutorID and _fps and _quality and _sound != "":
                if not _Start:
                    # change this place for your device
                    _desktop = "$(pactl get-default-sink).monitor"
                    _mic = "alsa_input.usb-Generic_USB2.0_PC_CAMERA_20100331010203-02.mono-fallback"

                    _now = datetime.now()
                    _FileName = f"{_now.year}-{_now.month}-{_now.day}_{_now.hour}-{_now.minute}-{_now.second}"

                    _VideoRecord = f"gpu-screen-recorder -w {_monutorID} -k h264 -ac aac -c flv -a {_mic}\\|{_desktop} -f {_fps} -q {_quality} -ab {_sound} -o {_path}/{str(_videoName).replace(" ", "\\ ")}_{_FileName}.mkv"
                    os.popen(_VideoRecord)
                    os.popen("notify-send -t 3500 -u low \"Video Recording is Starting\"")
                    _Start = True
                    _LiveOrRecordStart = True

        elif gc.GetEvent == "Stop Record":
            os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 3500 -u low \"Work Is Finish!\"")
            _Start = False
            _LiveOrRecordStart = False

    _second = _minute = _hour = 0
    _sec = time.monotonic()

    def update():
        global _path
        if gc.GetEvent == "Select Output Folder":
            _path = popup_get_folder(no_window=True, title="Warning!", message="Select Output Folder For Recording Video")
            gc.GetWindow["path"].update(_path)
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
        gc.GetWindow["time"].update(f"{_hour}:{_minute}:{int(_second)}")

    def LastWorkBeforeExit():
        global _Start, _LiveOrRecordStart
        if _sound:
            if _LiveOrRecordStart:
                os.popen("killall -SIGINT gpu-screen-recorder && notify-send -t 3500 -u low \"Work Is Finish!\"")
                _Start = False

    gc.SetUpdate(Update=update, exitBEFORE=LastWorkBeforeExit)
