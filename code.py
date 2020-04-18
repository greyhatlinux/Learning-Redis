import json
import redis
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--get", "--GET", action="store", default = False, help="to get the value for the provided key")
parser.add_argument("--set", "--SET",action="store", default = False, help="to set the value for the provided key")
parser.add_argument("--expire", "--expire",action="store", default = False, help="to get the expiration value for the provided key")
parser.add_argument("--value","--VALUE", action= "store", help="value")
parser.add_argument("--zadd","--ZADD", action="store", default=True, help="ZADD key score member")
parser.add_argument("--key",  action="store")
parser.add_argument("--score", action="store")
parser.add_argument("--member", action="store")


# parser.add_argument("--zrank")
# parser.add_argument("--zrange")
arguments = parser.parse_args()

redis = redis.Redis()

if arguments.set:
    if arguments.value:
        if (arguments.expire):
            redis.setex(arguments.set, arguments.expire, arguments.value)
            print(arguments.set, "set to", arguments.value, "for", arguments.expire, "seconds")
        else:
            redis.set(arguments.set, arguments.value)
            print(str(arguments.set), ":" , str(arguments.value))

    else:
        print("value not given for the key :", arguments.set) 
        
if arguments.get: 
    if redis.get(arguments.get):
        print(redis.get(arguments.get).decode("utf-8"))
    else:
        print("No value in DB")

# if arguments.zadd:
#     if arguments.key:
#         if arguments.score:
#             if arguments.member:
#                 redis.zadd(arguments.key, arguments.score, arguments.member)
#                 print("zadd", arguments.key, arguments.score, arguments.member )
#             else:
#                 print("provide member for zadd")
#         else:
#             print("provide score for zadd")
#     else:
#         print("provide the key for zadd")
        


# print(arguments.get, arguments.value, arguments.set)
