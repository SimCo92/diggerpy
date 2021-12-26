import urllib
import json
import sys
from DiscogsAPI.client import get_client, user_agent

def get_search(a, access_token=None):
    client = get_client(access_token)
    url = 'https://api.discogs.com/database/search?' + urllib.parse.urlencode(a)
    print(url)

    resp, content = client.request(url, headers={'User-Agent': user_agent})

    if resp['status'] != '200':
        sys.exit('Invalid API response {0}.'.format(resp['status']))

    json_content = json.loads(content.decode('utf-8'))
    return json_content


def parse_DGS_Response(response_json):
    """
    take a discogs response and parse the result if any
    """

    if str('results') in response_json.keys():
        if len(response_json['results']) > 0:
            if str('title') in response_json['results'][0].keys():
                title = response_json['results'][0]['title']

            if str('style') in response_json['results'][0].keys():
                styles = response_json['results'][0]['style']

            if str('label') in response_json['results'][0].keys():
                label = response_json['results'][0]['label']

            if str('year') in response_json['results'][0].keys():
                year = response_json['results'][0]['year']

            if str('country') in response_json['results'][0].keys():    
                country = response_json['results'][0]['country']

            if str('community') in response_json['results'][0].keys():    
                community = str(response_json['results'][0]['community'])

    return title, styles, label, year, country, community


if __name__ == "__main__":
    access_token = {
        "oauth_token": "VqCZjgtMxxKeNncTXXOJyKOCugvwYTMzRqrnpbxO",
        "oauth_token_secret": "WDXHpfqcAgZahgkmbsEfaLevGlhVBvswHDwzyOsD"
    }
    search_params = (("q", ""), ("artist", "Queen"), ("title", "I want to break free"))
    result = get_search(search_params)
    print(parse_DGS_Response(result))