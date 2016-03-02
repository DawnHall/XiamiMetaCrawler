__author__ = 'xlrtx'
from utils.db import DB
import pymysql
import config
# db = DB('xiami')
conn = pymysql.connect(**config.mysql)
cur = conn.cursor()
cur.execute('SELECT')
