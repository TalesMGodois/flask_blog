from flask_blog import app

from flask import render_template

from author.form import RegisterForm


@app.route('/login')
def login():
    return 'hello =D'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form =RegisterForm()
    return render_template('author/register.html', form=form)
