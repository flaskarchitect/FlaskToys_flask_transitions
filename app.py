#!/home/jack/miniconda3/envs/cloned_base/bin/python
from flask import Flask, render_template, request, redirect
import subprocess
import os
from icecream import ic
import random
import glob
import datetime
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    video = find_video()
    return render_template("index.html",video=video)

@app.route('/execute', methods=['POST','GET'])
def execute():
    input_file = request.form['input_file']
    output_file = request.form['output_file']
    ic(input_file)
    ic(output_file)
    # Ensure the input file exists
    #if not os.path.exists(input_file):
    #    return "Error: Input file does not exist."

    # Build and execute the FFmpeg command
    command = f"FFmpeg -hide_banner -loop 1 -i /home/jack/Desktop/tempp/static/resources/{input_file} -vf 'unsharp=5:5:1.0:5:5:0.0,scale=10000:1536,scroll=horizontal=0.0001,crop=1024:1536:0:0,scale=512x768',format=yuv420p -t 58 -y /home/jack/Desktop/tempp/static/scrolls/{output_file}"
    subprocess.run(command, shell=True)

    video = find_video()
    return render_template("index.html",video=video)

@app.route('/mk_video', methods=['POST','GET'])
def mk_video():
    image_files = request.form['image_files']
    ic(image_files)
    vid_file_name = "static/videos/"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.mp4'
    command2 = f"ffmpeg -framerate 2 -i {image_files}%05d.jpg -c:v libx265 -r 30 -pix_fmt yuv420p -t 38 -y {vid_file_name}"
    subprocess.run(command2, shell=True)
    video = find_video()
    return render_template("index.html",video=video)



@app.route('/zoom_n_overlay', methods=['POST','GET'])
def zoom_n_overlay():
    input_dir = request.form['input_dir']
    ic(input_dir)
    command2 = f"./zoom_overlay {input_dir}"
    subprocess.run(command2, shell=True)
    video = find_video()
    return render_template("index.html",video=video)

@app.route('/pad_effect', methods=['POST','GET'])
def pad_effect():
    input_directory = request.form['input_directory']
    ic(input_directory)
    command3 = f"./PadEffect {input_directory}"
    subprocess.run(command3, shell=True)
    video = find_video()
    return render_template("index.html",video=video)
def find_video():
    video =random.choice(glob.glob("static/videos/*.mp4"))
    video = video.replace("static/","")
    return video    

if __name__ == '__main__':
    app.run(debug=True)
