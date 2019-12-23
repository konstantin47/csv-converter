import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2409j1-0935gqae[rgaehrga983]'

    UPLOADED_PATH = os.path.join(basedir, 'uploads')
    DOWNLOAD_PATH = os.path.join(basedir, 'downloads')

    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
