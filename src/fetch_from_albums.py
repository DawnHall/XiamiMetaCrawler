__author__ = 'xlrtx'
from multiprocessing.dummy import Pool as ThreadPool
import time
import utils.func as func


pool = ThreadPool(16)  # If param not given, should be size of CPUs


print '---------------------------------------'
print 'Fetching new albums'
print '---------------------------------------'
tic = time.time()

print '..fetching albums'
albums = func.get_albums()

print '..fetching artist_detail for albums', len(albums)
albums = pool.map(func.album_get_artist_detail, albums)

print '..fetching album_detail from albums', len(albums)
albums_detail = pool.map(func.album_to_album_detail, albums)

print '..deriving songs from album_detail'
songs = reduce(func.reduce_albums_detail_to_songs, albums_detail, [])

print '..fetching tags for songs', len(songs)
songs = pool.map(func.song_get_tags, songs)

print '..fetching comments for songs', len(songs)
songs = pool.map(func.song_get_comments, songs)

print '..write db'
pool.map(func.put_song_to_db, songs)

print '..done, cost', time.time() - tic, 's'
pool.close()
pool.join()
