#!/usr/bin/env python
#
# This illustrates the call-flow required to complete an OAuth request
# against the discogs.com API. The script will download and save a single
# image from the discogs.com API as an example.
# See README.md for further documentation.
#
import sys
from urllib.parse import parse_qsl
import oauth2 as oauth

# Your consumer key and consumer secret generated by discogs when an application is created
# and registered . See http://www.discogs.com/settings/developers . These credentials
# are assigned by application and remain static for the lifetime of your discogs application.
# the consumer details below were generated for the 'discogs-oauth-example' application.
# TODO: remove secrets from here
consumer_key = "xsvlQuYcSWCicyBvwpXR"
consumer_secret = "aejCRjXyqebtqemXwChfKISWRHHifkjG"

# The following oauth end-points are defined by discogs.com staff. These static endpoints
# are called at various stages of oauth handshaking.
request_token_url = 'https://api.discogs.com/oauth/request_token'
authorize_url = 'https://www.discogs.com/oauth/authorize'
access_token_url = 'https://api.discogs.com/oauth/access_token'

# A user-agent is required with Discogs API requests. Be sure to make your user-agent
# unique, or you may get a bad response.
user_agent = 'discogs_api_example/1.0'

# create oauth Consumer and Client objects using
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# pass in your consumer key and secret to the token request URL. Discogs returns
# an ouath_request_token as well as an oauth request_token secret.
resp, content = client.request(request_token_url, 'POST', headers={'User-Agent': user_agent})

# we terminate if the discogs api does not return an HTTP 200 OK. Something is
# wrong.
if resp['status'] != '200':
    sys.exit('Invalid response {0}.'.format(resp['status']))

request_token = dict(parse_qsl(content.decode('utf-8')))

print(' == Request Token == ')
print(f'    * oauth_token        = {request_token["oauth_token"]}')
print(f'    * oauth_token_secret = {request_token["oauth_token_secret"]}')
print()


def get_access_token():
    print(f'Please browse to the following URL {authorize_url}?oauth_token={request_token["oauth_token"]}')

    accepted = 'n'
    while accepted.lower() == 'n':
        print()
        accepted = input(
            f'Have you authorized me at {authorize_url}?oauth_token={request_token["oauth_token"]} [y/n] :')
        oauth_verifier = input('Verification code : ')

    token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    client = oauth.Client(consumer, token)

    resp, content = client.request(access_token_url, 'POST', headers={'User-Agent': user_agent})
    access_token = dict(parse_qsl(content.decode('utf-8')))
    print(' == Access Token ==')
    print(f'    * oauth_token        = {access_token["oauth_token"]}')
    print(f'    * oauth_token_secret = {access_token["oauth_token_secret"]}')
    print(' Authentication complete. Future requests must be signed with the above tokens.')

    return access_token


def get_client(access_token=None):
    if access_token == None:
        access_token = get_access_token()

    token = oauth.Token(key=access_token['oauth_token'],
            secret=access_token['oauth_token_secret'])
    client = oauth.Client(consumer, token)

    return client