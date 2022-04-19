from flask import Flask, Blueprint, request, render_template, redirect
from flaskr.db import get_movies

bp = Blueprint('movies', __name__, url_prefix='/')

@bp.route('movies/')
def movie_list():
    movies = get_movies()
    return render_template('movies.html', movies=movies)

@bp.route('/')
def sendRedirect():
    return redirect('movies/')