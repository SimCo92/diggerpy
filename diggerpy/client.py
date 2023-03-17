import requests

from diggerpy.models import Artist, Label, Release, SearchResults


class NotFoundError(Exception):
    pass


class DiscogsClient:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token = None

    def authenticate(self):
        # Auth with consumer_key and consumer_secret
        response = requests.post(
            "https://api.discogs.com/oauth/request_token",
            auth=(self.consumer_key, self.consumer_secret),
        )
        token = dict(item.split("=") for item in response.text.split("&"))
        self.token = token["oauth_token"]

        print(
            f"Go to https://www.discogs.com/oauth/authorize?oauth_token={self.token} to authorize the app",
        )

    def get_token(self, oauth_verifier):
        # Get token after user authorizes the app
        response = requests.post(
            "https://api.discogs.com/oauth/access_token",
            auth=(self.consumer_key, self.consumer_secret, self.token),
            data={"oauth_verifier": oauth_verifier},
        )
        token = dict(item.split("=") for item in response.text.split("&"))
        self.token = token["oauth_token"]
        print(f"Access Token: {self.token}")

    def _get(self, url):
        headers = {"Authorization": f"Discogs token={self.token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def search(self, query, **params):
        url = f"{self.base_url}/database/search"
        params["q"] = query
        response = self._get(url, params=params)
        return SearchResults.from_json(response)

    def get_artist(self, artist_id):
        url = f"{self.base_url}/artists/{artist_id}"
        try:
            response = self._get(url)
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise NotFoundError(f"Artist {artist_id} not found")
            else:
                raise
        return Artist.from_json(response)

    def get_label(self, label_id):
        url = f"{self.base_url}/labels/{label_id}"
        try:
            response = self._get(url)
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise NotFoundError(f"Label {label_id} not found")
            else:
                raise
        return Label.from_json(response)

    def get_release(self, release_id):
        url = f"{self.base_url}/releases/{release_id}"
        try:
            response = self._get(url)
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise NotFoundError(f"Release {release_id} not found")
            else:
                raise
        return Release.from_json(response)
