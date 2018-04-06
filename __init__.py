from flask import Flask
from flaskext.markdown import Markdown
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('settings')
db = SQLAlchemy(app)


# Migrations
migrate = Migrate(app, db)

Markdown(app)

from blog import  views
from author import  views

