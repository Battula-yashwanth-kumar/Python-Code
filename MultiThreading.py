import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1=time.perf_counter()
    #normal Code 
    # func(5)
    # func(2)
    # func(1)
    
    #code with multithreading
    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2=time.perf_counter() #calculate the performance time
    print(time2-time1)

# main()

# instead of manully writing all the threads  u can use ThreadPoolExecutor

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # f1=executor.submit(func,5)
        # f2=executor.submit(func,2)
        # f3=executor.submit(func,1)
        # print(f1.result())
        # print(f2.result())
        # print(f3.result())

        # instead of using them, we can use map method
        l=[3,5,1,2]
        results=executor.map(func,l)
        for result in results:
            print(result)


poolingDemo()

