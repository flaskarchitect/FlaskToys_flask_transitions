from flask import Flask, render_template, request, redirect, url_for, session
import secrets
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
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

    return render_template('indexk.html', project_loaded=project_loaded, project_name=project_name, project_content=project_content)

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
            return redirect(url_for('indexk'))

    return redirect(url_for('indexk'))

if __name__ == '__main__':
    app.run(debug=True)
