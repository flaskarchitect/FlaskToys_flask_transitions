#!/home/jack/miniconda3/envs/cloned_base/bin/python
import subprocess
import uuid
import shutil
import os
from random import choice, randint
from sys import argv
def minterpolate_video(DIR):
    # Create a unique ID using uuid
    uid = str(uuid.uuid4())

    # Define the directory containing MP3 files
    MUSIC_DIR = "/home/jack/Desktop/FlaskAppArchitect_Flask_App_Creator/static/MUSIC/"

 # Use glob to get a list of image files in the specified directory
    image_files = glob.glob(os.path.join(DIR, '*.jpg'))

    # Shuffle the list of image files
    shuffled_images = random.sample(image_files, len(image_files))

    # Build the ffmpeg command using the shuffled images
    subprocess.run([
        'ffmpeg', '-framerate', '17', '-pattern_type', 'glob', '-i', f'{DIR}*.jpg',
        '-c:v', 'libx265', '-r', '30', '-pix_fmt', 'yuv420p', '-y', 'start.mp4'
    ])

    subprocess.run([
        'ffmpeg', '-hide_banner', '-i', 'start.mp4',
        '-filter:v', "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=10'",
        '-c:v', 'libx264', '-r', '20', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-y', 'output2.mp4'
    ])

    subprocess.run([
        'ffmpeg', '-hide_banner', '-i', 'output2.mp4',
        '-filter:v', "setpts=7*PTS,minterpolate='fps=25:scd=none:me_mode=bidir:vsbmc=1:search_param=200'",
        '-y', 'final2l.mp4'
    ])

    subprocess.run([
        'ffmpeg', '-hide_banner', '-i', 'final2l.mp4',
'-filter:v', "setpts=7*PTS,minterpolate='fps=25:scd=none:me_mode=bidir:vsbmc=1:search_param=200'",'-t',' 36',
        '-y', 'final5l.mp4'
    ])

    # Use os.path.join to join paths
    random_mp3 = choice([f for f in os.listdir(MUSIC_DIR) if f.endswith('.mp3')])

    # Print the path of the randomly selected MP3 file
    print(f"Randomly selected MP3 file: {os.path.join(MUSIC_DIR, random_mp3)}")

    # Function to get a random number between 50 and 100
    def get_random_seconds():
        return randint(50, 100)

    # Function to get a random music file from the MUSIC array
    def get_random_music():
        return choice([f for f in os.listdir(MUSIC_DIR) if f.endswith('.mp3')])

    # Get random init seconds and music file
    init_seconds = get_random_seconds()
    random_music = get_random_music()

    # Run ffmpeg command
    mp4_show = f"/home/jack/Desktop/HDD500/collections/vids/Minterpolate_{uid}.mp4"
    subprocess.run([
        'ffmpeg', '-i', 'final5l.mp4', '-ss', str(init_seconds), '-i', os.path.join(MUSIC_DIR, random_music),
        '-af', 'afade=in:st=0:d=4', '-map', '0:0', '-map', '1:0', '-shortest', '-y', mp4_show
    ])

    # Use shutil.copyfile to copy the final video
    vid_filename = "static/videos/minterpolate.mp4"
    shutil.copyfile(mp4_show, vid_filename)

    return mp4_show
if __name__=="__main__":
    # Replace 'your_directory' with the actual directory path
    minterpolate_video(argv[1])
