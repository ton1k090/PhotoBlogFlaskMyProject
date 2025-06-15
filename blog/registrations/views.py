from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from blog.extension import db
from blog.forms import Registration
from blog.models import User

registrations = Blueprint('registrations', __name__, url_prefix='/article', static_folder='../static')


@registrations.route('/registration', methods=['GET', 'POST'])
def register_page():
    form = Registration(request.form)

    if request.method == 'POST' and form.validate():
        user = User(
                    username=form.username.data,
                    password=form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Аккаунт создан! Пожалуйста войдите!')
            return redirect(url_for('auth.login_page'))
        except IntegrityError:
            db.session.rollback()
            flash('Пользователь с такими данными существует!', 'error')

    return render_template('blog/user_registrations.html', form=form)