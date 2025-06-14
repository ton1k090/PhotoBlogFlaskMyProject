from flask import Blueprint, render_template

index = Blueprint("index", __name__, url_prefix="/", static_folder="../static")




@index.route('/')
@index.route('/index')
def main_page():
    '''главная страничка'''
    return render_template('blog/index.html', title='Главная',)


