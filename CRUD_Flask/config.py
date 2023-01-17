import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')

SQALCHEMY_TRACK_MODIFICATIONS = False