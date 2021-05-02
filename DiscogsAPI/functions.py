import discogs_client
import pandas as pd
import time
import requests
import json
from models import DiscogsOBJ




# df = pd.read_csv("YT_liked_videos_2019-08-21.csv")

# Consumer Key	xsvlQuYcSWCicyBvwpXR
# Consumer Secret	aejCRjXyqebtqemXwChfKISWRHHifkjG

# df_result = pd.DataFrame(columns=['styles','label','year','country','community'])
    

def search_string(string, key, secret):

    if key or secret is None:
        print("please provide Discogs key and secret")
        return 0

    link = f"https://api.discogs.com/database/search?q={string}&key={key}secret={secret}"
    return link


def connect(link, seconds=30, timeout=300):
    """
    take link as input and iterate if response is error
    """
    # TODO: add timeout and error hendler
    response = requests.get(link)._content.decode('utf-8') # Decode using the utf-8 encoding
    response_json = json.loads(response)

    while 'message' in response_json.keys():

        print("error response - waiting 60 second and retrying")
        time.sleep(seconds)
        response = requests.get(link)._content.decode('utf-8') # Decode using the utf-8 encoding

    return response



def parse_response(response):
    """
    take a discogs response and parse the result if any
    """
    response_json = json.loads(response)

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