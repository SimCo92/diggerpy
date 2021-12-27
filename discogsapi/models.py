
class DiscogsOBJ:
    def __init__(self, title, artist=None, album=None, genre=None, year=None, label=None, country=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = year
        self.label = label
        self.country = country


class Song(DiscogsOBJ):
    def __init__(self, title, artist=None, album=None):
        self.title = title
        self.artist = artist
        self.album = album

class Release(DiscogsOBJ):
    def __init__(self, name, artist=None, genre=None, year=None, label=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.year = year
        self.label = label



