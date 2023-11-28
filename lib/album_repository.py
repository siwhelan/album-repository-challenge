from lib.album import Album


class AlbumRepository:
    # init with connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from albums")
        albums = []
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def find(self, artist_id):
        rows = self._connection.execute(
            "SELECT * FROM albums WHERE id = %s", [artist_id]
        )
        row = rows[0]
        return Album(row["title"], row["release_year"], row["artist_id"])

    def create(self, album):
        rows = self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
            [album.title, album.release_year, album.artist_id],
        )

    def delete(self, id):
        self._connection.execute("DELETE from albums WHERE id = %s", [id])
