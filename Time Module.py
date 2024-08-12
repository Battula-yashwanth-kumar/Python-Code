import time
initial=time.time()
print(initial) #print us the seconds of time that have elapsed since the unix epoch
k=0
while(k<45) :
  time.sleep(2)
  print(k)  #delays then execution of further commands for given specific seconds
  k+=1
localtime=time.asctime(time.localtime(time.time()))
print(localtime) #is used to convert the number of seconds to local time.this function takes sec as input
