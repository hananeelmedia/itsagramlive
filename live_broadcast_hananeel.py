import os
from dotenv import load_dotenv
from pathlib import Path
import argparse
import subprocess
from ItsAGramLive import ItsAGramLive

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

live = ItsAGramLive(
    username=os.getenv('IGL_USERNAME'),
    password=os.getenv('IGL_PASSWORD')
)

if live.login():
    print("You'r logged in")

    if live.create_broadcast():

        self.is_running = True

        while self.is_running:
            cmd = input('command> ')

            if cmd == "start":
                self.start_broadcast()

                ffmpeg_cmd = "ffmpeg " \
                         "-rtbufsize 256M " \
                         "-re " \
                         "-i '{file}' " \
                         "-i '/root/itsagramlive/video/frame.png' " \
                         "-c:a aac " \
                         "-ar 44100 " \
                         "-b:a 128k " \
                         "-pix_fmt yuv420p " \
                         "-profile:v baseline " \
                         "-filter_complex '[0:v]scale=w=1080:h=1920:force_original_aspect_ratio=decrease,[1:v]overlay=(W-w)/2:(H-h)/2' " \
                         "-bufsize 6000k " \
                         "-vb 1000k " \
                         "-maxrate 4500k " \
                         "-deinterlace " \
                         "-vcodec libx264 " \
                         "-preset veryfast " \
                         "-g 30 -r 30 " \
                         "-f flv '{stream_server}{stream_key}'".format(file=os.getenv('IGL_FILENAME'),
                                                                       stream_server=live.stream_server,
                                                                       stream_key=live.stream_key)

                print('CTRL+C to quit.')
                try:
                    subprocess.call(ffmpeg_cmd, shell=True)
                except KeyboardInterrupt:
                    pass
                except Exception as error:
                    print(error)
                    live.end_broadcast()
                    self.is_running = False

                live.end_broadcast()
                self.is_running = False

            elif cmd == "stop":
                self.stop()
                self.is_running = False

            else:
                print(
                    'Available commands:\n\t '
                    '"start"\n\t '
                    '"stop"\n\t ')

        