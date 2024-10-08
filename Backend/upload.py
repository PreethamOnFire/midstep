from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

Student_Upload = 'Student_Upload'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'png', 'jpg', 'jpeg', 'gif'}

app.config['Backend/Student_Upload'] = Student_Upload

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['Backend/Student_Upload'], filename))
            
            # Run the Python script with the filename as an argument
            result = subprocess.run(['python3', 'mainUpdate.py', filename], capture_output=True, text=True)
            
            return f'File uploaded and processed. Result: {result.stdout}'
    return render_template('upload.html')

if __name__ == '__main__':
    os.makedirs(Student_Upload, exist_ok=True)
    app.run(debug=True)