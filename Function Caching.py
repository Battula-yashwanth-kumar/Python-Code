#  caching means storing the data in a place from where it can be servered faster. In the case of data that has been frequently used, the computer assigns a cache memory, si ti does not load it again and again from the main memeory.

import time
from functools import lru_cache

@lru_cache(maxsize=32) # it can store max 32 unique values. (3,2,1,6) but not the same values again. As it is not a new values its execution will be faster.
def some_work(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print("running")
    some_work(3)
    some_work(1)
    some_work(2)
    print("done calling")
    print("recalling")
    some_work(3)

