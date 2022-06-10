import time
from functools import lru_cache

@lru_cache(maxsize=32)     # maxsize=32 means, it should store 32 values in the cache
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)          # actually, sleep() is used here just to illustrate the matter. The delay could be because of fetching the value everytime which takes n secs
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)           # It should have taken 3 secs but it won't because the value is loaded in the cache
    print("Called again")