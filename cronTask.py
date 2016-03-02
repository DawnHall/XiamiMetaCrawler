__author__ = 'xlrtx'
import subprocess


def call_script(path_bin, path_script):
    retry = 3
    while retry:
        try:
            subprocess.call([path_bin, path_script])
            break
        except Exception, e:
            print e.message
            retry -= 1


python_bin = 'bin/python'

script_fetch_albums = 'src/fetch_from_albums.py'
script_fetch_songs = 'src/fetch_from_songs.py'
script_write_sql = 'src/write_sql.py'

call_script(python_bin, script_fetch_albums)
call_script(python_bin, script_fetch_songs)
call_script(python_bin, script_write_sql)
