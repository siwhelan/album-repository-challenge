from lib.album import Album


# test album construction -
# album should contain title (str) release_year (int), artisit_id (int)
def test_album_construction_fields():
    album = Album("Parklife", 1994, 5)
    assert album.artist_id == 5
    assert album.title == "Parklife"
    assert album.release_year == 1994
