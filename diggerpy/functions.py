import urllib
import json
import sys
from DiggerPy.client import get_client, user_agent

def get_search(search_obj, access_token=None):
    """
    Take a search_obj as input and return a list of result in dict
    """
    client = get_client(access_token)
    url = 'https://api.discogs.com/database/search?' + urllib.parse.urlencode(search_obj)

    resp, content = client.request(url, headers={'User-Agent': user_agent})

    if resp['status'] != '200':
        sys.exit('Invalid API response {0}.'.format(resp['status']))

    json_content = json.loads(content.decode('utf-8'))
    return json_content


def get_search_v2(search_obj, access_token=None):
    """
    Take an search_obj as input
    Similar to get_search() but it takes the first result and returns the master release infos
    """
    client = get_client(access_token)
    url = 'https://api.discogs.com/database/search?' + urllib.parse.urlencode(search_obj)

    resp, content = client.request(url, headers={'User-Agent': user_agent})

    if resp['status'] != '200':
        sys.exit('Invalid API response {0}.'.format(resp['status']))

    json_content = json.loads(content.decode('utf-8'))
    item = json_content['results'][0]

    resp2, content2 = client.request(item['master_url'], headers={'User-Agent': user_agent})
    json_content2 = json.loads(content2.decode('utf-8'))

    return json_content2
