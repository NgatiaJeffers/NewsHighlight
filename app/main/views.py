from flask import render_template, request, url_for
from . import main
from ..request import get_news_source



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    all_sources = get_news_source()
    title = 'Falling Sky News'

    return render_template('index.html', source = all_sources, title = title)