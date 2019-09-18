from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
Bootstrap(app)

from app import routes, models