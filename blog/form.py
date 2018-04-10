from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import validators, StringField, TextAreaField, SelectField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from author.form import RegisterForm
from blog.models import Category
from flask_blog import db


class SetupForm(RegisterForm):
    name = StringField('Blog name',[
        validators.Required(),
        validators.Length(max=80)
    ])


def categories():
    return [(row.id, row.name) for row in Category.query.all()]


class PostForm(FlaskForm):

    _categories = categories()

    image = FileField('Image', [
        FileAllowed(['jpg', 'png'], 'Images Only')
    ])

    title = StringField('Title',[
        validators.Required(),
        validators.Length(max=80)
    ])

    body = TextAreaField('Content', [validators.Required()])

    category = SelectField('Category', choices= _categories, coerce=int)

    new_category = StringField('Category')
