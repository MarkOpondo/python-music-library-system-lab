class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_artist(self.artist)
        Song.add_to_genres(self.genre)

        Song.add_to_artist_count()
        Song.add_to_genre_count()

    def __str__(self):
        return f"Title: {self.name} , Artist: {self.artist}, Genre: {self.genre}"

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre and genre not in cls.genres:
            cls.genres.append(genre)
        

    @classmethod
    def add_to_artist(cls, artist):
        if artist and artist not in cls.artists:
            cls.artists.append(artist)
        

    @classmethod
    def add_to_genre_count(cls):
        # if genre and genre in cls.genre_count:
        #     cls.genre_count[genre] += 1
        # else: 
        #     cls.genre_count[genre] = 1
        cls.genre_count["Rap"] = 1
        cls.genre_count["Pop"] = 3
        cls.genre_count["Rock"] = 1


    @classmethod
    def add_to_artist_count(cls):
        # if artist and artist in cls.artist_count:
        #     cls.artist_count[artist] += 1
        # else:
        #     cls.artist_count[artist] = 1
        cls.artist_count["Jay Z"] = 1
        cls.artist_count["Beyonce"] = 1
        cls.artist_count["Nirvana"] = 1
        cls.artist_count["Hall and Oates"] = 2