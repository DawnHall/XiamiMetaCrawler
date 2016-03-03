from utils.db import DB
import pymysql
import config
__author__ = 'xlrtx'


def gen_sql_statement(song):
    key_str = ''
    val_str = ''
    for k, v in song.iteritems():
        if k == '_id':
            k = 'song_id'
        key_str += k + ', '
        if v is not None:
            if isinstance(v, basestring):
                val_str += '\'' + pymysql.escape_string(v) + '\''
            else:
                val_str += str(v)
        else:
            val_str += 'NULL'
        val_str += ', '
    key_str = key_str.strip(', ')
    val_str = val_str.strip(', ')
    return 'INSERT INTO xiami_music (' + key_str + ') VALUES (' + val_str + ')'


def write_song_to_sql(cur, in_song):
    statement = gen_sql_statement(in_song)
    cur.execute(statement)
    print cur.description
    return False


sql_conn = pymysql.connect(**config.mysql)
sql_cur = sql_conn.cursor()
mongo_db = DB('xiami')

songs = mongo_db.get_songs()
checks = []  # Check if ths song has been imported to sql
for song in songs:
    check = {'saved': False, 'song': song}
    if write_song_to_sql(sql_cur, song):
        check['saved'] = True
    checks += check
    break

sql_conn.close()
