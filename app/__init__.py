from flask import Flask
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('app.config.Config')


login_manager = LoginManager()	#lets the app know we're using a login manager
login_manager.init_app(app)

import views
