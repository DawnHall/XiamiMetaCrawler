__author__ = 'xlrtx'
import top.api.rest as rest

API_PAGE = 1
API_LIMIT = 100
API_TIME_OUT = None
'''
TOP Api Hub

There is no internal state so no need for class
'''


def api_wrapper(config_func):
    def wrapper(*args, **kwargs):
        api = config_func(*args, **kwargs)
        return api.getResponse(timeout=API_TIME_OUT).items()[0][1]['data']

    return wrapper


def page_wrapper(warp_type):
    def inner_page_wrapper(config_func):
        def wrapper(*args, **kwargs):
            next_page = 1
            max_page = 2
            all_albums = []
            result = None
            while next_page != max_page:
                if next_page == 2:
                    break
                kwargs['page'] = next_page
                result = config_func(*args, **kwargs)
                all_albums += result[warp_type]
                next_page = result['next']
                max_page = result['page_number']
            result[warp_type] = all_albums
            return result

        return wrapper

    return inner_page_wrapper


@page_wrapper('albums')
@api_wrapper
def get_rank_new_album(album_type, page=API_PAGE, limit=API_LIMIT):
    api = rest.AlibabaXiamiApiRankNewAlbumGetRequest()
    api.type = album_type
    api.limit = limit
    api.page = page
    return api


@page_wrapper('albums')
@api_wrapper
def get_rank_new_albums(page=API_PAGE, limit=API_LIMIT):
    api = rest.AlibabaXiamiApiRankNewAlbumsGetRequest()
    api.limit = limit
    api.page = page
    return api


@api_wrapper
def get_rank_songs(rank_type):
    api = rest.AlibabaXiamiApiRankSongsGetRequest()
    api.type = rank_type
    return api


@api_wrapper
def get_album_detail(album_id, full_des='true'):
    api = rest.AlibabaXiamiApiAlbumDetailGetRequest()
    api.id = album_id
    api.full_des = full_des
    return api


@api_wrapper
def get_artist_detail(artist_id, description='show'):
    api = rest.AlibabaXiamiApiArtistDetailGetRequest()
    api.id = artist_id
    api.description = description
    return api


@page_wrapper('comment_list')
@api_wrapper
def get_comment_song(song_id, page=API_PAGE, limit=API_LIMIT):
    api = rest.AlibabaXiamiApiCommentSongGetRequest()
    api.id = song_id
    api.page = page
    api.limit = limit
    return api


@api_wrapper
def get_tag_tags(object_id, object_type):
    api = rest.AlibabaXiamiApiTagTagsRequest()
    api.object_id = object_id
    api.object_type = object_type
    return api
