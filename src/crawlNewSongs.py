__author__ = 'xlrtx'
from multiprocessing.dummy import Pool as ThreadPool
import time
import utils.api as api

query_types = ['music_all', 'music_oumei', 'music_ri', 'music_han', 'music_huayu', 'newmusic_all', 'newmusc_oumei',
               'newmusic_ri', 'newmusic_han', 'newmusic_huayu', 'hito', 'jingge', 'uk', 'billboard', 'oricon', 'mnet',
               'music_original', 'music_demo', 'momo']
query_types_ignore = ['newmusc_oumei']
# songs = []
# for query_type in query_types:
#     if query_type in query_types_ignore:
#         continue
#     songs += api.get_rank_songs(query_type)['data']['songs']

trim = lambda x: x.strip().replace('|', '')


def album_get_area(album):
    area = api.get_artist_detail(album['artist_id'])['area']
    album['area'] = area
    return album


def album_to_album_details(album):
    out_album_details = api.get_album_detail(album['album_id'])
    out_album_details['area'] = album['area']
    return out_album_details


def reduce_albums_details_to_songs(pre, cur):
    cur_songs = cur['songs']
    cur_area = cur['area']
    cur_gmt_publish = cur['gmt_publish']
    for cur_song in cur_songs:
        cur_song['area'] = cur_area
        cur_song['publish_ts'] = cur_gmt_publish
    return pre + cur_songs


def song_get_tags(in_song):
    in_tags = api.get_tag_tags(in_song['song_id'], 'song')['tags']
    tags = []
    tags_count = []
    for in_tag in in_tags:
        tags += [trim(in_tag['tag'])]
        tags_count += [str(in_tag['count'])]
    in_song['tags'] = '|'.join(tags)
    in_song['tags_count'] = '|'.join(tags_count)
    return in_song


def song_get_comments(in_song):
    comments = api.get_comment_song(in_song['song_id'])['comment_list']
    if 'commentlist' in comments:
        comments.remove('commentlist')  # Should be a bug caused by provider
    comments = [trim(comment['message']) for comment in comments]
    in_song['comments'] = '|'.join(comments)
    return in_song


pool = ThreadPool(16)  # If param not given, should be size of CPUs


print '---------------------------------------'
print 'Fetching new albums'
print '---------------------------------------'
tic = time.time()

print '..fetching albums'
albums = api.get_rank_new_albums()['albums']

print '..fetching area for albums', len(albums)
albums = pool.map(album_get_area, albums)

print '..fetching album_details from albums', len(albums)
albums_details = pool.map(album_to_album_details, albums)

print '..deriving songs from album_details'
songs = reduce(reduce_albums_details_to_songs, albums_details, [])

print '..fetching tags for songs', len(songs)
songs = pool.map(song_get_tags, songs)

print '..fetching comments for songs', len(songs)
songs = pool.map(song_get_comments, songs)
print '..done, cost', time.time() - tic, 's'


print '---------------------------------------'
print 'Fetching new songs'
print '---------------------------------------'
pool.close()
pool.join()
