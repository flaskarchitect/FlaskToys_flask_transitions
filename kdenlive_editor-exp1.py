#!/home/jack/Desktop/FlaskAppArchitect_Flask_App_Creator/env/bin/python
from flask import Flask, render_template, request, session
import secrets
import os
import subprocess
import datetime
import logging
from moviepy.editor import VideoFileClip

# Set up logging
logging.basicConfig(filename='flask_app_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

def save_file_with_date():
    output_directory="static/videos"
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Get the current date and time
        current_datetime = datetime.datetime.now()
        date_suffix = current_datetime.strftime("%Y_%m_%d_%H_%M")

        # Construct the new file name with date suffix
        output_file_name = f"{date_suffix}.mp4"

        # Construct the full output file path
        output_file_path = os.path.join(output_directory, output_file_name)

        # Check if the source video file exists
        if not os.path.exists(source_video_path):
            raise FileNotFoundError(f"Source video file '{source_video_path}' not found.")

        # Use moviepy to create a copy of the video file with the new name
        video_clip = VideoFileClip(source_video_path)
        video_clip.write_videofile(output_file_path, codec="libx264", audio_codec="aac")

        logging.info(f"File saved successfully as '{output_file_path}'")

        return output_file_path

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'static/videos'
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def indexk():
    project_loaded = False
    project_name = ""
    project_content = ""

    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']

        if file.filename != '' and file.filename.endswith('.kdenlive'):
            # Set the project as loaded
            project_loaded = True
            project_name = file.filename

            # Save the uploaded file path to the session
            session['project_filename'] = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

            # Read the content of the uploaded file
            with open(session['project_filename'], 'r') as f:
                project_content = f.read()

    # Replace 'source_video.mp4' with the actual file path of your source video
    source_video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'source_video.mp4')
    output_video = save_file_with_date(app.config['OUTPUT_FOLDER'], source_video_path)

    if output_video:
        output_video = output_video.replace("static/", "")
    else:
        # Handle the case where saving the file failed
        # You may want to redirect the user or display an error message
        output_video = ""

    return render_template('indexk.html', project_loaded=project_loaded, project_name=project_name, project_content=project_content, video_path=output_video)

@app.route('/save_project', methods=['POST'])
def save_project():
    if request.method == 'POST':
        edited_content = request.form.get('edited_content')

        # Check if 'project_filename' is present in the session
        if 'project_filename' in session:
            # Get the file path from the session
            file_path = session['project_filename']

            # Save the edited content back to the file
            with open(file_path, 'w') as f:
                f.write(edited_content)
        else:
            # Handle the case when 'project_filename' is not in the session
            # You might want to redirect the user or display an error message
            output_video = os.path.join(app.config['OUTPUT_FOLDER'], 'melt_output_file.mp4')
            output_video = output_video.replace("static/", "")
            return render_template('indexk.html', video_path=output_video)

    output_video = os.path.join(app.config['OUTPUT_FOLDER'], 'melt_output_file.mp4')
    output_video = output_video.replace("static/", "")
    return render_template('indexk.html', video_path=output_video)

@app.route('/view_melt')
def view_melt():
    # Run the melt command to generate the video
    input_kdenlive = session.get('project_filename', None)  # Correct key
    if input_kdenlive:
        output_video = os.path.join(app.config['OUTPUT_FOLDER'], 'melt_output_file.mp4')
        melt_command = f'melt {input_kdenlive} -consumer avformat:{output_video}'

        try:
            subprocess.run(melt_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            return f"Error running melt command: {e}"
        output_video = output_video.replace("static/", "")
        return render_template('view_melt.html', video_path=output_video)

    return "No Kdenlive project loaded."

if __name__ == '__main__':
    app.run(debug=True)
