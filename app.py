from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection


class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")

        while True:
            print("\nWhat would you like to do?")
            print("1 - List all albums")
            print("2 - List all artists")
            print("3 - Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_all_albums()
            elif choice == "2":
                self.list_all_artists()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def list_all_albums(self):
        album_repo = AlbumRepository(self._connection)
        albums = album_repo.all()

        if albums:
            print("\nHere is the list of albums:")
            for album in albums:
                print(
                    f"* {album.title} (Released in {album.release_year}, Artist ID: {album.artist_id})"
                )
        else:
            print("No albums found in the library.")

    def list_all_artists(self):
        artist_repo = ArtistRepository(self._connection)
        artists = artist_repo.all()

        if artists:
            print("\nHere is the list of artists:")
            for artist in artists:
                print(f"* {artist.name} (Genre: {artist.genre}, ID: {artist.id})")
        else:
            print("No artists found in the library.")


if __name__ == "__main__":
    app = Application()
    app.run()
