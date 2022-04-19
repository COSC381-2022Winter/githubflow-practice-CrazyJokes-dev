from flask import Blueprint, request, render_template
from flaskr.db import get_movies

bp = Blueprint('', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def movie_list():
    movies = get_movies()
    return render_template('movies.html', movies=movies)