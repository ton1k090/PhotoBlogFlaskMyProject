from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from blog import app
from flask_login import UserMixin

from blog.extension import db


# Создание Моделей
class Category(db.Model):
    '''Модель категорий постов'''
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    posts = db.relationship('Post', back_populates='category') # Связывание моделей между собой

    def __repr__(self):
        return self.title


class Post(db.Model):
    '''Модель постов'''
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())
    category_id = mapped_column(ForeignKey('category.id')) # Связывание айди поста с айди категории
    category = db.relationship('Category', back_populates='posts') # Связывание моделей между собой
    picture = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return self.title


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500))
    is_staff = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.username


