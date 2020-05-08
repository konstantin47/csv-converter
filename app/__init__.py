from flask import Flask
from flask_dropzone import Dropzone
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
# from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix

from app.config import Config

app = Flask(__name__, static_url_path='/static')

app.config.from_object(Config)

# app.config['REVERSE_PROXY_PATH'] = '/converter'
# ReverseProxyPrefixFix(app)

login = LoginManager(app)
dropzone = Dropzone(app)
Bootstrap(app)

from app import views
