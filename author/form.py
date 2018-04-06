from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email', [validators.Required(), validators.Email()])

    username = StringField('Username',[
        validators.Required()
    ])

    password = PasswordField('Password',[
        validators.Required(),
        validators.EqualTo('confirm', message= 'Password must match')
    ])

    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
    username = StringField('Username',[
        validators.Required(),
        validators.Length(min=4,max=25)
    ])

    password = PasswordField('Password',[
        validators.Required(),
        validators.Length(min=4, max=80)
    ])

