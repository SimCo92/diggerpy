class SearchResults:
    """A class representing search results returned from the Discogs API.

    Attributes:
        results (list): A list of search results.
    """

    def __init__(self, results):
        self.results = results

    @classmethod
    def from_json(cls, data):
        """Create a SearchResults object from JSON data.

        Args:
            data (dict): A dictionary containing search results data.

        Returns:
            SearchResults: A SearchResults object.
        """
        return cls(data["results"])


class Artist:
    """A class representing an artist from the Discogs API.

    Attributes:
        id (int): The artist ID.
        name (str): The artist name.
        profile (str): The artist profile.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.profile = data.get("profile", "")

    @classmethod
    def from_json(cls, data):
        """Create an Artist object from JSON data.

        Args:
            data (dict): A dictionary containing artist data.

        Returns:
            Artist: An Artist object.
        """
        return cls(data)


class Label:
    """A class representing a label from the Discogs API.

    Attributes:
        id (int): The label ID.
        name (str): The label name.
        profile (str): The label profile.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.profile = data.get("profile", "")

    @classmethod
    def from_json(cls, data):
        """Create a Label object from JSON data.

        Args:
            data (dict): A dictionary containing label data.

        Returns:
            Label: A Label object.
        """
        return cls(data)


class Release:
    """A class representing a release from the Discogs API.

    Attributes:
        id (int): The release ID.
        title (str): The release title.
        artists (list): A list of Artist objects representing the release's artists.
        labels (list): A list of Label objects representing the release's labels.
        year (str): The release year.
        genres (list): A list of genres associated with the release.
        styles (list): A list of styles associated with the release.
        tracklist (list): A list of track objects representing the release's tracklist.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.artists = [Artist.from_json(a) for a in data["artists"]]
        self.labels = [Label.from_json(label) for label in data["labels"]]
        self.year = data.get("year", "")
        self.genres = data.get("genres", [])
        self.styles = data.get("styles", [])
        self.tracklist = data.get("tracklist", [])

    @classmethod
    def from_json(cls, data):
        """Create a Release object from JSON data.

        Args:
            data (dict): A dictionary containing release data.

        Returns:
            Release: A Release object.
        """
        return cls(data)
