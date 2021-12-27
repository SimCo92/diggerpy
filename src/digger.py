from .settings import Settings
import secrets as secrets
import sys
from urllib.parse import parse_qsl
import oauth2 as oauth

class Digger:
    """Class to be instantiated to use the script"""

    def __init__(
            self,
            consumer_key = None,
            consumer_secret = None,
            oauth_token = None,
            oauth_token_secret = None,
    ):
        consumer_key = secrets.consumer_key
        consumer_secret = secrets.consumer_secret
        Settings.Digger_is_running = True

        self.consumer = oauth.Consumer(consumer_key, consumer_secret)




    def get_access_token(self):
        # TODO: remove secrets from here
        request_token_url = 'https://api.discogs.com/oauth/request_token',
        authorize_url = 'https://www.discogs.com/oauth/authorize',
        access_token_url = 'https://api.discogs.com/oauth/access_token',
        # A user-agent is required with Discogs API requests. Be sure to make your user-agent
        # unique, or you may get a bad response.
        user_agent = 'discogs_api_example/1.0'

        # create oauth Consumer and Client objects using
        consumer = self.consumer
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

        print(f'Please browse to the following URL {authorize_url}?oauth_token={request_token["oauth_token"]}')

        accepted = 'n'
        while accepted.lower() == 'n':
            print()
            accepted = input(
                f'Have you authorized me at {authorize_url}?oauth_token={request_token["oauth_token"]} [y/n] :')
            oauth_verifier = input('Verification code : ')

        token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)

        return token

    def get_client(self, access_token=None):

        if access_token == None:
            access_token = self.get_access_token()

        token = oauth.Token(key=access_token['oauth_token'],
                            secret=access_token['oauth_token_secret'])
        client = oauth.Client(self.consumer, token)

        return client




