from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user
from werkzeug.exceptions import NotFound
from werkzeug.security import check_password_hash

from blog.forms import UserLogin
from blog.models import User, UserMixin

auth = Blueprint("auth", __name__, url_prefix="/", static_folder="../static")


@auth.route("/login", methods=["GET", "POST"]) # Поддерживает методы гет и пост
def login_page():
    '''Функция авторизации'''
    if request.method == "GET":
        form = UserLogin(request.form)
        return render_template("blog/user_login.html", form=form)

    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Check your login details")
        return redirect(url_for("auth.login_page"))
    login_user(user)
    return redirect(url_for("index.main_page", pk=user.id))