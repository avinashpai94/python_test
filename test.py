import  bitlyapi
import  sys

API_USER = "o_1bqf5gdhav"
API_KEY = "R_e3ec11466903417bb8da9ab27310550f"

b = bitlyapi.BitLy(API_USER,API_KEY)

usage = """Usage: python shortener.py [url] e.g python shortener.py http://www.google.com"""

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

longurl = sys.argv[1]

response = b.shorten(longurl=longurl)

print(response['url'])
