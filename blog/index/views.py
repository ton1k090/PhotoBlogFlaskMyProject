from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.sql.functions import user

from blog.extension import db
from blog.forms import ContactForm
from blog.models import Post, Gallery, Contact

index = Blueprint("index", __name__, url_prefix="/", static_folder="../static")


@index.route('/')
@index.route('/index', methods=['GET', 'POST'])
def main_page():
    '''главная страничка'''
    form = ContactForm(request.form)
    posts = Post.query.all()
    gallery = Gallery.query.all()

    if request.method == 'POST' and form.validate():
        contact = Contact(first_name=form.first_name.data,
                          last_name=form.last_name.data,
                          email=form.email.data,
                          message=form.message.data)
        try:
            db.session.add(contact)
            db.session.commit()
            flash('Сообщение отправлено!')
            return redirect(url_for('index.main_page'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR!', 'error')

    return render_template('blog/index.html',
                           title='Главная',
                           posts=posts,
                           gallery=gallery,
                           form=form
                           )





