__author__ = 'xlrtx'
from pymongo import MongoClient


class DB:
    def __init__(self, db_name):
        self.__client = MongoClient()
        self.__db = self.__client[db_name]
        self.__col_songs = self.__db['new_songs']

    def add_song(self, song):
        key = {'_id': song['_id']}
        self.__col_songs.update(key, song)
        pass
