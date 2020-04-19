from flask import Flask,request,render_template,send_from_directory, flash, make_response
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


basepath = os.path.dirname(__file__)
filepath = os.path.join(basepath, 'my_files')  


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        upload_path = os.path.join(filepath, file.filename)
        if file:
            file.save(upload_path)
        else:
            flash("请先选择文件")
    myfiles = os.listdir(filepath)
    return render_template('index.html', comments=myfiles)


@app.route('/download/<file_name>')
def download(file_name):
    response = make_response(send_from_directory(filepath, file_name, as_attachment=True))
    # 解决中文文件名报错问题
    response.headers["Content-Disposition"] = "attachment; filename{}".format(file_name.encode().decode('latin-1'))
    return response


