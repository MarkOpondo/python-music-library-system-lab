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

        Song.add_to_artist_count(self.artist)
        Song.add_to_genre_count(self.genre)

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
    def add_to_genre_count(cls, genre):
        if genre and genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else: 
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist and artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

track1 = Song("Houdini", "Eminem", "Hip-Hop")
track2 = Song("Not Like Us", "Kendrick Lamar", "Hip-Hop")

print(f"Total Song Units: {Song.count}") # 2
print(f"Unique Artist Inventory: {Song.artist_count}")  # 2
print(f"Unique Genre Matrix: {Song.genre_count}")    # 1
print(f"Track Details: {track1}") # "Houdini", "Eminem", "Hip-Hop"