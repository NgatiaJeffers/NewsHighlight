from flask import render_template, request, url_for
from . import main
from ..request import get_news_source, get_news_headlines



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    all_sources = get_news_source()
    title = 'Falling Sky News'

    return render_template('index.html', sources = all_sources, title = title)


@main.route('/source/<source>')
def news_headlines(source):
    '''
    Function pulls/gets the top and breakng news
    '''

    title = "Falling Sky News"
    news_headlines = get_news_headlines(source)
    return render_template('articles.html', title = title, headlines = news_headlines)