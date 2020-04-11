from flask import Flask,request,render_template,send_from_directory
import os

app = Flask(__name__)
basepath = os.path.dirname(__file__)
filepath = os.path.join(basepath, 'my_files')  


@app.route('/', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        upload_path = os.path.join(filepath, file.filename)
        file.save(upload_path)

        
    myfiles = os.listdir(filepath)
    return render_template('index.html', comments=myfiles)


@app.route('/download/<file_name>')
def download(file_name):
    return send_from_directory(filepath, file_name, as_attachment=True)

