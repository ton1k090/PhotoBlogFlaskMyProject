from flask import Blueprint, render_template

from blog.models import Post, Gallery

index = Blueprint("index", __name__, url_prefix="/", static_folder="../static")




@index.route('/')
@index.route('/index')
def main_page():
    posts = Post.query.all()
    gallery = Gallery.query.all()
    '''главная страничка'''
    return render_template('blog/index.html', title='Главная', posts=posts, gallery=gallery)


