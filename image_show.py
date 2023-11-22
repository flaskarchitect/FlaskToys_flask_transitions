#!/home/jack/miniconda3/envs/cloned_base/bin/python
import subprocess
import uuid
import shutil
import glob
from sys import argv
import datetime

def mk_video(DIR):
    vid_filename = 'static/videos/image_show.mp4'
    image_files = DIR
    print(image_files)
    #command2 = f"ffmpeg -framerate 2 -i {image_files} -c:v libx265 -r 30 -pix_fmt yuv420p -t 38 -y {vid_filename}"
    command2 = f"ffmpeg -framerate 2 -i {image_files}%05d.jpg -c:v libx265 -r 30 -pix_fmt yuv420p -t 38 -y {vid_filename}"
    subprocess.run(command2, shell=True)
    uid = str(uuid.uuid4())  # Generate a unique ID using uuid
    mp4_show =  f"/home/jack/Desktop/HDD500/collections/vids/Image_show_{uid}.mp4"
    shutil.copyfile(vid_filename, mp4_show)  
    return vid_filename
if __name__=="__main__":
    DIR = argv[1]
    mk_video(DIR)