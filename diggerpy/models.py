
# TODO: check which class parameter is mandatory and set None the others

class SearchItem:
    """
    Item returned from get_search()
    """
    def __init__(self, country, year, format, label, type, genre, style, id, barcode, user_data, master_id, master_url,
                 uri, catno, title, thumb=None, cover_image=None, resource_url=None,community=None,
                 format_quantity=None, formats=None):
        self.country = country
        self.year = year
        self.format = format
        self.label = label
        self.type = type
        self.genre = genre
        self.style = style
        self.id = id
        self.barcode = barcode
        self.user_data = user_data
        self.master_id = master_id
        self.master_url = master_url
        self.uri = uri
        self.catno = catno
        self.title = title
        self.thumb = thumb
        self.cover_image = cover_image
        self.resource_url = resource_url
        self.community = community
        self.format_quantity = format_quantity
        self.formats = formats

    def __repr__(self):
         return f"""
                country = {self.country},
                year = {self.year},
                format = {self.format},
                label = {self.label},
                type = {self.type},
                genre = {self.genre},
                style = {self.style},
                id = {self.id},
                barcode = {self.barcode},
                user_data = {self.user_data},
                master_id = {self.master_id},
                master_url = {self.master_url},
                uri = {self.uri},
                catno = {self.catno},
                title = {self.title},
                thumb = {self.thumb},
                cover_image = {self.cover_image},
                resource_url = {self.resource_url},
                community = {self.community},
                format_quantity = {self.format_quantity},
                formats = {self.formats}
                """

class Master:
    """
    Master release model
    """
    def __init__(self, id, main_release, most_recent_release, resource_url, uri, versions_url, main_release_url,
                 most_recent_release_url, num_for_sale, lowest_price, images, genres, styles, year, tracklist, artists,
                 title, notes=None, data_quality=None, videos=None):
        self.id = id
        self.main_release = main_release
        self.most_recent_release = most_recent_release
        self.resource_url = resource_url
        self.uri = uri
        self.versions_url = versions_url
        self.main_release_url = main_release_url
        self.most_recent_release_url = most_recent_release_url
        self.num_for_sale = num_for_sale
        self.lowest_price = lowest_price
        self.images = images
        self.genres = genres
        self.styles = styles
        self.year = year
        self.tracklist = tracklist
        self.artists = artists
        self.title = title
        self.notes = notes
        self.data_quality = data_quality
        self.videos = videos

    def __repr__(self):
        return f"""
                id = {self.id},
                main_release = {self.main_release},
                most_recent_release = {self.most_recent_release},
                resource_url = {self.resource_url},
                uri = {self.uri},
                versions_url = {self.versions_url},
                main_release_url = {self.main_release_url},
                most_recent_release_url = {self.most_recent_release_url},
                num_for_sale = {self.num_for_sale},
                lowest_price = {self.lowest_price},
                images = {self.images},
                genres = {self.genres},
                styles = {self.styles},
                year = {self.year},
                tracklist = {self.tracklist},
                artists = {self.artists},
                title = {self.title},
                data_quality = {self.data_quality},
                videos = {self.videos}
                """

    def get_tracklist(self):
         return [d['title'] for d in self.tracklist]

    def get_videos(self):
        return [{'title': d['title'], 'video': d['uri']} for d in self.videos]


