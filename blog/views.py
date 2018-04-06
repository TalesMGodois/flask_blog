from flask import url_for, render_template, flash, abort, session
from slugify import slugify
from werkzeug.utils import redirect

from author.decorators import login_required, author_required
from author.models import Author
from blog.form import SetupForm, PostForm
from blog.models import Blog, Category, Post
from flask_blog import app, db
import bcrypt


@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return redirect(url_for('admin'))


@app.route('/admin')
@author_required
def admin():
    if session.get('is_author'):
        return render_template('blog/admin.html')
    else:
        abort(403)


@app.route('/setup', methods=['GET','POST'])
def setup():
    form = SetupForm()
    error = ""

    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)

        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(author)
        db.session.flush()

        if author.id:
            blog = Blog(
                form.name.data,
                author.id
            )

            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"

        if author.id and blog.id:
            db.session.commit()
            flash("Blog created")
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error creating blog"

    return render_template('blog/setup.html', form=form, error=error)



@app.route('/post', methods=['GET', 'POST'])
@author_required
def post():
    error = False
    form = PostForm()
    try:
        if form.validate_on_submit():
            if form.new_category.data:
                new_category = Category(form.new_category.data)
                db.session.add(new_category)
                db.session.flush()
                category = new_category

            elif form.category.data:
                category_id = form.category.data
                category = Category.query.filter_by(id=category_id).first()

            else:
                category = None

            blog = Blog.query.first()
            author = Author.query.filter_by(username=session['username']).first()
            title = form.title.data
            body = form.body.data
            slug = slugify(title)
            post = Post(blog,author,title,body,category,slug)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('article',slug=slug))

        return render_template('blog/post.html', form=form)
    except ValueError:
        error = "Problemas ao salvar a informação"
        return render_template('blog/post.html',error= error)


@app.route('/article/<string:slug>')
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()

    return render_template('blog/article.html',post= post)
