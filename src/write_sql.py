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
    return 'INSERT IGNORE INTO xiami_music (' + key_str + ') VALUES (' + val_str + ')'


def write_song_to_sql(cur, in_song):
    statement = gen_sql_statement(in_song)
    cur.execute(statement)
    return False


print '---------------------------------------'
print 'Transferring mongo to mysql'
print '---------------------------------------'
sql_conn = pymysql.connect(**config.mysql)
sql_cur = sql_conn.cursor()
mongo_db = DB('xiami')

print '..flushing mongo collection to mysql'
songs = mongo_db.get_songs()
for song in songs:
    write_song_to_sql(sql_cur, song)

try:
    sql_conn.commit()
    print '..commit success, dropping mongo collection'
    sql_conn.close()
except Exception, e:
    print e.message
    print '..commit failed, rolling back, nothing\'s changed'
    sql_conn.rollback()
    sql_conn.close()
