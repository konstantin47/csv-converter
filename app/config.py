import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2409j1-0935gqae[rgaehrga983]'

    UPLOADED_PATH = os.path.join(basedir, 'uploads')
    DOWNLOAD_PATH = os.path.join(basedir, 'downloads')
