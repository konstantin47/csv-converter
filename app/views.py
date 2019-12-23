import os
import uuid

from flask import (
    render_template,
    make_response,
    request,
    send_file,
    jsonify,
)

from app import app
from app.utils import fix_file


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        if f.filename.split('.')[-1] != 'csv':
            return 'CSV only!', 400

    return render_template('index.html')


@app.route("/getfile", methods=["POST"])
def getfile():
    fileob = request.files["file"]

    if fileob.filename.split('.')[-1] != 'csv':
        return 'CSV only!', 400

    filename = str(uuid.uuid4())
    save_path = os.path.join(app.config["UPLOADED_PATH"], filename+'.csv')
    fileob.save(save_path)

    old_files = os.listdir(app.config['DOWNLOAD_PATH'])
    if old_files:
        old_file_names = [int(f.split('.')[0]) for f in old_files]
        fname = str(max(old_file_names) + 1)
    else:
        fname = '1'
    fname += '.txt'

    txt = os.path.join(app.config['DOWNLOAD_PATH'], fname)
    fix_file(save_path, txt)

    response = jsonify(filename=fname)
    return make_response(response, 201)


@app.route('/file/<filename>')
def file(filename):

    return render_template('file.html', filename=filename)


@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(app.config['DOWNLOAD_PATH'], filename)
    return send_file(path, as_attachment=True)
