from typing import Dict
import MySQLdb
import config
from DBUtils.PooledDB import PooledDB




def create_conn_pool(conf:Dict):

    _pool = PooledDB(creator=MySQLdb, mincached=1,maxcached=20, host=config.DBHOST,
                     port=config.DBPORT, user=config.DBUSER, passwd=config.DBPWD,
                    db=config.DBNAME,charset=config.DBCHAR)
    return _pool

def get_dest_connect():
    global _dest_pool
    if not _dest_pool:
        _dest_pool=create_conn_pool().connection()
    return _dest_pool

def get_src_connect():
    global _src_pool
    if not _src_pool:
        _src_pool=create_conn_pool().connection()
    return _src_pool

db= get_dest_connect()
cursor=db.cursor()
cursor.execute("SELECT * FROM stock")
print(cursor.fetchone())
