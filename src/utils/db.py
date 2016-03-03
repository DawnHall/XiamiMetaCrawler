from pymongo import MongoClient
__author__ = 'xlrtx'


class DB:
    def __init__(self, db_name):
        self.__client = MongoClient()
        self.__db = self.__client[db_name]
        self.__col_songs = self.__db['new_songs']

    def add_song(self, song):
        key = {'_id': song['_id']}
        self.__col_songs.update(key, song, upsert=True)

    def drop_col_songs(self):
        self.__db.drop_collection('new_songs')

    def get_songs(self):
        return self.__col_songs.find()

    def del_song(self, song_id):
        return self.__col_songs.delete_one({'_id': song_id})
