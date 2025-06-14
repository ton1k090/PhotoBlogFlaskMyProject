from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import Post

article = Blueprint("article", __name__, url_prefix="/", static_folder="../static")


@article.route('/article', methods=['GET'])
def article_list():
    # articles: Post = Post.query.all()
    return render_template(
        'blog/single.html'
    )


@article.route('/<int:article_id>/', methods=['GET'])
def article_detail(article_id):
    _article: Post = Post.query.filter_by(id=article_id)


    if _article is None:
        raise NotFound
    return render_template(
        'blog/single.html',
        article=_article,
    )