from datetime import datetime

from flask_blog import db, uploaded_images


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('author.id'))
    posts = db.relationship('Post', backref= 'blog', lazy ='dynamic')

    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def __repr__(self):
        return "<Blog %r>" % self.name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    image = db.Column(db.String(255))
    slug = db.Column(db.String(256), unique=True)
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)

    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    @property
    def imgsrc(self):
        return uploaded_images.url(self.image)

    def __init__(
            self,
            blog,
            author,
            title,
            body,
            category,
            image= None,
            slug= None,
            publish_date=None,
            live=True
    ):

        self.blog = blog
        self.author = author
        self.title = title
        self.body = body
        self.category = category
        self.slug = slug
        self.live = live
        self.image = image

        if publish_date is None:
            self.publish_date = datetime.utcnow()
        else:
            self.publish_date = publish_date

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    posts = db.relationship('Post', backref= 'category', lazy ='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r>" % self.name