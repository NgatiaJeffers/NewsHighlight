from .main import main
import urllib.request, json
from .models import Everything

# # Getting the API KEY
api_key = None
source_url = None
top_headlines_url = None
everything_url = None
tech_url = None

def configure_request(app):
    global api_key, source_url, top_headlines_url, everything_url, tech_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['SOURCE_API_BASE_URL']
    top_headlines_url = app.congig['TOP_HEADLINES_API_BASE_URL']
    everything_url = app.config['EVERYTHING_API_BASE_URL']
    tech_url = app.config['TECH_API_BASE_URL']



def get_news_source():
    '''
    Function that gets the json response to our url request, fetching all the sources data.
    and we'll return all the required news source.
    '''

    news_url = source_url.format(api_key)

    with urllib.request.urlopen(news_url) as url:
        source_data = url.read()
        source_response = json.loads(source_data)
        source_results = None

        if source_response ['source']:
            source_items = source_response['source']
            source_results = process_source_data(source_items)

        return source_results


def process_source_data(source_list):
    '''
    Function that proces the source result and transform them to a list of objects

    Args:
        Each source will  required to have diff definations
    '''

    source_processed = []
    for item in source_list:
        id = item.get('id')
        name = item.get('name')
        url = item.get('url')
        description = item.get('description')
        new_source = Source(id, name, url, description)
        source_processed.append(new_source)

    return source_processed