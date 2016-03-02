#   TODO maybe implement cache?
__author__ = 'xlrtx'
import utils.api as api

trim = lambda x: x.strip().replace('|', '')

get_albums = lambda: api.get_rank_new_albums()['albums']


def album_get_artist_detail(album):
    area = api.get_artist_detail(album['artist_id'])['area']
    album['area'] = area
    return album


def album_to_album_detail(album):
    album_detail = api.get_album_detail(album['album_id'])
    album_detail['area'] = album['area']
    return album_detail


def reduce_albums_detail_to_songs(pre, cur):
    cur_songs = cur['songs']
    cur_area = cur['area']
    cur_gmt_publish = cur['gmt_publish']
    for cur_song in cur_songs:
        cur_song['area'] = cur_area
        cur_song['publish_ts'] = cur_gmt_publish
    return pre + cur_songs


def song_get_tags(song):
    in_tags = api.get_tag_tags(song['song_id'], 'song')['tags']
    tags = []
    tags_count = []
    for in_tag in in_tags:
        tags += [trim(in_tag['tag'])]
        tags_count += [str(in_tag['count'])]
    song['tags'] = '|'.join(tags)
    song['tags_count'] = '|'.join(tags_count)
    return song


def song_get_comments(song):
    comments = api.get_comment_song(song['song_id'])['comment_list']
    if 'commentlist' in comments:
        comments.remove('commentlist')  # Should be a bug caused by provider
    comments = [trim(comment['message']) for comment in comments]
    song['comments'] = '|'.join(comments)
    return song


def get_songs():
    query_types = ['music_all', 'music_oumei', 'music_ri', 'music_han', 'music_huayu', 'newmusic_all', 'newmusc_oumei',
                   'newmusic_ri', 'newmusic_han', 'newmusic_huayu', 'hito', 'jingge', 'uk', 'billboard', 'oricon',
                   'mnet',
                   'music_original', 'music_demo', 'momo']
    query_types_ignore = ['newmusc_oumei']
    songs = []
    for query_type in query_types:
        if query_type in query_types_ignore:
            continue
        songs += api.get_rank_songs(query_type)['songs']
    return songs


def song_get_album_detail(song):
    album_detail = api.get_album_detail(song['album_id'])
    song['publish_ts'] = album_detail['gmt_publish']
    song['language'] = album_detail['language']
    return song


def song_get_artist_detail(song):
    artist_detail = api.get_artist_detail(song['artist_id'])
    song['area'] = artist_detail['area']
    return song
