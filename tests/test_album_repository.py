from lib.album_repository import AlbumRepository
from lib.album import Album

# test that a full album list is returned when
# all() is called on AlbumRepository


def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums[:4] == [
        Album("Doolittle", 1989, 1),
        Album("Surfer Rosa", 1988, 1),
        Album("Waterloo", 1974, 2),
        Album("Super Trouper", 1980, 2),
    ]

    assert albums[-1] == Album("Ring Ring", 1973, 2)


# calling find() on the album repository with a specific id
# returns the correct album back


def test_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result1 = repository.find(2)
    result2 = repository.find(3)
    assert result1 == Album("Surfer Rosa", 1988, 1)
    assert result2 == Album("Waterloo", 1974, 2)


# test create method
def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    new_album = Album("New Album", 2023, 4)
    repository.create(new_album)
    result = repository.all()
    assert result[-1] == Album("New Album", 2023, 4)


# test delete
def test_delete(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert result[:4] == [
        Album("Surfer Rosa", 1988, 1),
        Album("Waterloo", 1974, 2),
        Album("Super Trouper", 1980, 2),
        Album("Bossanova", 1990, 1),
    ]
