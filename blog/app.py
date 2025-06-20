from json import load
from os import getenv, path

from flask import render_template, Flask
from flask_admin import Admin

from blog.extension import db, login_manager, migrate
from blog.models import User
from blog.admins import AdminAccess

CONFIG_PATH = getenv("CONFIG_PATH", path.join("../dev_config.json"))


def create_app():

    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)

    admin = Admin(app, template_mode='bootstrap4', index_view=AdminAccess())

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    '''Расширение Фласк'''

    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    migrate.init_app(app, db, compare_type=True)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    '''Зарегистрировать Блупринты ( приложения )'''
    from .index.views import index
    from .article.views import article
    from .auth.views import auth
    from .registrations.views import registrations

    app.register_blueprint(index)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(registrations)
