import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True

DB_USERNAME = 'bblog'
DB_PASSWORD = 'chacal'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' %(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True
