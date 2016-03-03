from utils.db import DB
import pymysql
import config
__author__ = 'xlrtx'
# db = DB('xiami')
conn = pymysql.connect(**config.mysql)
cur = conn.cursor()
cur.execute('SELECT')
