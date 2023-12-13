#!/home/jack/miniconda3/envs/cloned_base/bin/python
from flask import Flask, render_template, request, redirect, url_for
import os
import os

uploads_directory = 'uploads'

# Check if the 'temp' directory exists
if not os.path.exists(uploads_directory):
    # If it doesn't exist, create it
    os.mkdir(uploads_directory)
    print(f"The '{uploads_directory}' directory has been created.")
else:
    print(f"The '{uploads_directory}' directory already exists.")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Create a folder named 'uploads' in your project directory

@app.route('/', methods=['GET', 'POST'])
def indexk():
    project_loaded = False
    project_name = ""

    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']

        if file.filename != '' and file.filename.endswith('.kdenlive'):
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Set the project as loaded
            project_loaded = True
            project_name = file.filename

    return render_template('indexk.html', project_loaded=project_loaded, project_name=project_name)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
