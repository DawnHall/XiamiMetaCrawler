from multiprocessing.dummy import Pool as ThreadPool
import time
import utils.func as func
__author__ = 'xlrtx'


pool = ThreadPool(16)  # If param not given, should be size of CPUs


print '---------------------------------------'
print 'Fetching new songs'
print '---------------------------------------'
tic = time.time()

print '..fetching songs'
songs = func.get_songs()

print '..fetching artist_detail for songs', len(songs)
songs = pool.map(func.song_get_artist_detail, songs)

print '..fetching album_detail from songs', len(songs)
songs = pool.map(func.song_get_album_detail, songs)

print '..fetching tags for songs', len(songs)
songs = pool.map(func.song_get_tags, songs)

print '..fetching comments for songs', len(songs)
songs = pool.map(func.song_get_comments, songs)

print '..write db'
pool.map(func.put_song_to_db, songs)

print '..done, cost', time.time() - tic, 's'
pool.close()
pool.join()

