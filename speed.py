import subprocess
import uuid
import shutil
import os


def speed_up():
    output_fast = 'static/videos/output_fast.mp4'
    command2 = [
        "ffmpeg", "-i", "gifs/All_gifs2.mp4", "-vf", "setpts=0.09*PTS", "-an", "-y", "static/videos/output_fast.mp4"
    ]
    # Join the command into a single string for printing
    command_str2 = " ".join(command2)
    print("Command2:", command_str2)
    # Run ffmpeg
    subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    uid = str(uuid.uuid4())  # Generate a unique ID using uuid
    mp4_zoom =  f"/home/jack/Desktop/HDD500/collections/vids/Zoom_Fast_{uid}.mp4"
    title_image_path = "/mnt/HDD500/EXPER/static/assets/Title_Image02.png"
    shutil.copyfile(output_fast, mp4_zoom)
    # Clean up the file list
    print("Video Created at: ",mp4_zoom)

speed_up()    
