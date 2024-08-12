# Coroutines are mostly used in cases  of time consuming programs such as tasks related to machine learning or deeplearning algorithms or in cases where  the program has to read a file containing a large number of data.
# In such situations we do  not want the program to read the file or data again and again, so we can use corotines to make the program more efficient and faster
# next() --> used to start the coroutines
# send() --> used to send data to coroutines
# close() --> to close the coroutine

def searcher():
    import time
    book="This a book ;las;,a' xKXLAX;SA' ALCK;ALC; ACLASC';QS;Q;' AC;ALSC;ASC';Q';Q;WQ;W'Q;;C';C;"
    time.sleep(4)
    while True:           # this is coroutines
        text=(yield) # similar to generator
        if text in book:   
            print("Found")
        else :
            print("Not Found")

search=searcher()
print("Search started")
next(search)
search.send("aclkclcl")
print("cs,c;c'w,'c'wv;,'wav;'")
search.send('book')
search.close()