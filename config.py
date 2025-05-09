import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:kien170025436069@localhost/ahp_honda"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('ahphondaihihhiohoalsdalsd!@$!$@%#$%#$$!#!@#!kawasdaidaso2aaskdakl{(&&$%@#)}') or os.urandom(24)