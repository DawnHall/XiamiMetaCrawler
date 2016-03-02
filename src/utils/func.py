#   TODO maybe implement cache?
__author__ = 'xlrtx'
import utils.api as api
from utils.db import DB

db = DB('xiami')

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
    cur_language = cur['language']
    cur_gmt_publish = cur['gmt_publish']
    for cur_song in cur_songs:
        cur_song['area'] = cur_area
        cur_song['language'] = cur_language
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


def format_song(song):
    tmp = {
        '_id': 'song_id',
        'song_name': 'song_name',
        'album_id': 'album_id',
        'album_name': 'album_name',
        'artist_id': 'artist_id',
        'artist_name': 'artist_name',
        'lyric': 'lyric',
        'lyric_text': 'lyric_text',
        'singers': 'singers',
        'length': 'length',
        'play_count': 'play_counts',
        'recommend_count': 'recommends',
        'tags': 'tags',
        'tags_count': 'tags_count',
        'comments': 'comments',
        'publish_ts': 'publish_ts',
        'language': 'language',
        'area': 'area'
    }
    for k, v in tmp.iteritems():
        if v in song:
            tmp[k] = song[v]
        else:
            tmp[k] = None
    return tmp


def put_song_to_db(song, db_xiami=db):
    song = format_song(song)
    db_xiami.add_song(song)
    return True
