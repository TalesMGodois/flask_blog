from flask import Flask
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flaskext.markdown import Markdown
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('settings')
db = SQLAlchemy(app)


# Migrations
migrate = Migrate(app, db)

#markdown
Markdown(app)

#images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)



from blog import  views
from author import  views

