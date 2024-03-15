from GnuChanGUI import *
from moviepy.video.io.VideoFileClip import VideoFileClip

"""
this lgpl3+ 4.61.0.206 Unreleased version
fun it's a serious goal of the project. if we're not having fun while making stuff, when something's not right!
"""

# 60 second parts
class SplitVideo:
    def __init__(self, input_file, output_dir, second, stop) -> None:
        self.input_file = input_file
        self.output_dir = output_dir
        self.second = second
        self.stop = stop

    def update(self):
        try:
            self.clip = VideoFileClip(self.input_file)
            self.total_time = self.clip.duration
            self.start_time = 0
            self.end_time = min(self.second, self.total_time)
            self.part_number = 1

            while self.start_time < self.total_time:
                output_path = f"{self.output_dir}/part_{self.part_number}.mp4"
                subclip = self.clip.subclip(self.start_time, self.end_time)
                subclip.write_videofile(output_path, codec="libx264")
                self.part_number += 1
                self.start_time = self.end_time
                self.end_time = min(self.start_time + self.second, self.total_time)
                if self.stop:
                    break
            self.clip.close()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if hasattr(self, 'clip'):
                self.clip.close()


if __name__ == "__main__":
    gc = GnuChanGUI(Title="", Size=(800, 600), resizable=True, finalize=True)
    gc.font = "Sans, 20"
    Themecolors().GnuChanOS

    pathInput = ""
    pathOutput = ""
    second = 60
    mp4List = ""
    videoProcessStop = False

    leftColumn = [
        [gc.hsep],
            [gc.GText(title="Input Path: ", font="Sans, 20"),  gc.GText(title=pathInput, value="video_input", xStretch=True, font="Sans, 20")],
            [gc.GText(title="Output Path: ", font="Sans, 20"), gc.GText(title=pathOutput, value="video_output", xStretch=True, font="Sans, 20")],
            [gc.GText(title="Video Parts Second", font="Sans, 20"), gc.GText(title=second, value="second", xStretch=True, font="Sans, 20")],
        [gc.hsep],
            [gc.vsep, gc.GButton("Save input Path", font="Sans, 20"),  gc.GInput(value="path_input", xStretch=True), gc.vsep],
            [gc.vsep, gc.GButton("Save output Path", font="Sans, 20"), gc.GInput(value="path_output", xStretch=True), gc.vsep],
            [gc.vsep, gc.GButton("Save Add Second", font="Sans, 20"),  gc.GInput(value="video_second", xStretch=True), gc.vsep],
        [gc.hsep],
            [gc.Push, gc.GButton(title="Start Process"), gc.GButton(title="Stop Processes"), gc.Push],
        [gc.hsep],
            [gc.GLog(value="log", xStretch=True, yStretch=True, font="Sans, 10")],
        [gc.hsep] ]

    rightColumn = [
        [gc.hsep],
        [gc.GText(title="Mp4 Video list", xStretch=True, position="center")],
        [gc.GListBox(value="mp4List", xStretch=True, yStretch=True, noScroolBar=True)],
        [gc.hsep] ]

    layout = [ [gc.vsep,
                gc.GFrame(winLayout=rightColumn, xStretch=True, yStretch=True, border=0),
                gc.vsep,
                gc.GFrame(winLayout=leftColumn, xStretch=True, yStretch=True, border=0),
                gc.vsep] ]

    # [gc.GLog(value="log", xStretch=True, yStretch=True, font="Sans, 10")],
    gc.GWindow(mainWindow=layout)
    gc.GListBoxBorderSize(value="mp4List", border=0)



    def update():
        global pathInput, pathOutput, second, mp4List, videoProcess, videoProcessStop

        if gc.event == "Save input Path":
            try:
                pathInput = gc.GetValues["path_input"]
                gc.window["video_input"].update(pathInput)
                gc.window["path_input"].update("")
            except Exception as error:
                print(f"Error: {error}")

        if gc.event == "Save output Path":
            try:
                pathOutput = gc.GetValues["path_output"]
                gc.window["video_output"].update(pathOutput)
                gc.window["path_output"].update("")
                
                mp4List = os.listdir(pathOutput)
                gc.window["mp4List"].update(mp4List)
            except Exception as error:
                print(f"Error:{error}")

        if gc.event == "Save Add Second":
            try:
                second = int(gc.GetValues["video_second"])
                gc.window["second"].update(second)
            except Exception as error:
                print(f"Error:{error}")

        # start and stop process
        if gc.event == "Start Process":
            if pathInput != "" and pathOutput != "":
                try:
                    videoProcess = SplitVideo(input_file=pathInput, output_dir=pathOutput, stop=videoProcessStop, second=second)
                    videoProcess.update()
                except Exception as error:
                    print(f"Error:{error}")       

        if gc.event == "Stop Processes":
            try:
                pass
            except Exception as error:
                print(f"Error:{error}")

        """
        if gc.window.size[0] > 800:
            print(gc.window.size[0])
        else:
            print("yes")
        """

    gc.update(GUpdate=update)