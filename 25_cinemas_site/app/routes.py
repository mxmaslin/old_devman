from flask import render_template

from app import app

from app.utils import (get_movies_list,
                       get_movie_threads,
                       get_composed_movie_instances,
                       )

NUM_MOVIES_TO_DISPLAY = 10


@app.route('/')
def movies():
    movies_list = get_movies_list()[:NUM_MOVIES_TO_DISPLAY]
    movie_threads = get_movie_threads(movies_list)
    movies = get_composed_movie_instances(movie_threads)
    movies.sort(key=lambda x: x.rating, reverse=True)
    return render_template('films_list.html', movies=movies)
