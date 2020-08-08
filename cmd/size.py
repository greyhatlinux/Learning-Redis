from connection import redis 
from style import style

def sizeDB():
    style("REDIS db size")
    print(redis.dbsize())