from flask import Blueprint, render_template, request

from blog.forms import Registration
from blog.models import User

registrations = Blueprint('registrations', __name__, url_prefix='/article', static_folder='../static')


@registrations.route('/registration', methods=['GET', 'POST'])
def register_page():
    form = Registration(request.form)
    return render_template("blog/user_registrations.html", form=form)