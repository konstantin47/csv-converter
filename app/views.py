import os
from random import choice
import string

from flask import (
    render_template,
    make_response,
    request,
    redirect,
    url_for,
    flash,
    send_file,
)
from flask_login import current_user, login_user, login_required, logout_user

from app import app, db
from app.utils import fix_file, get_new_filename
from app.models import User
from app.forms import LoginForm, RegistrationForm


@app.route('/', methods=['POST', 'GET'])
def upload():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if request.method == 'POST':
        f = request.files.get('file')
        if f.filename.split('.')[-1] != 'csv':
            return 'CSV only!', 400

        folder = request.cookies.get('folder_name')

        up_path = os.path.join(app.config['UPLOADED_PATH'], folder)
        filename = get_new_filename(up_path)
        csv = os.path.join(app.config['UPLOADED_PATH'], folder, filename+'.csv')
        txt = os.path.join(app.config['DOWNLOAD_PATH'], folder, filename+'.txt')

        f.save(csv)
        fix_file(csv, txt)

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('upload'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('upload'))

    resp = make_response(render_template('login.html', form=form))
    fname = ''.join(choice(string.ascii_lowercase) for _ in range(1, 10))
    resp.set_cookie('folder_name', fname)

    # Creating dirs
    os.makedirs(os.path.join(app.config['UPLOADED_PATH'], fname))
    os.makedirs(os.path.join(app.config['DOWNLOAD_PATH'], fname))

    return resp


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/new-user', methods=['POST', 'GET'])
def new_user():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if request.method == 'POST':
        pass
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        u = User(username=username)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('upload'))

    return render_template('new_user.html', form=form)


@app.route('/download')
@login_required
def download():
    folder = request.cookies.get('folder_name')
    path = os.path.join(app.config['DOWNLOAD_PATH'], folder)
    files = [f for f in os.listdir(path)]
    old_nums = [int(file.split('.')[0]) for file in files]
    last = str(max(old_nums))
    return redirect(url_for('file', filename=last+'.txt'))


@app.route('/file/<path:filename>')
def file(filename):
    folder = request.cookies.get('folder_name')
    return render_template('file.html', folder=folder, filename=filename)


@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    path = os.path.join(app.config['DOWNLOAD_PATH'], folder, filename)
    return send_file(path, as_attachment=True)
