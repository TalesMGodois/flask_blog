from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, SelectField
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

    title = StringField('Title',[
        validators.Required(),
        validators.Length(max=80)
    ])

    body = TextAreaField('Content', [validators.Required()])

    category = SelectField('Category', choices= _categories, coerce=int)

    new_category = StringField('Category')
