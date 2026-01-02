import threading
import time

#import thread in python2 or _thread

def func():
    print("ran")
    time.sleep(1) #if this thread sleeps/hangs (we are waiting of it ) then we will switch to another thread (in this case printing the active threads i.e 2 ) then we will return back and print done.
    print ("done")

#in python if u just do a tuple like (5) it automatically removes the brackets, and evaluates it as a regular thing. but if u do (5,NONE) it will keep it as tuple and the fromed at it needs to be passed in.
x=threading.Thread(target=func)   #here args(4,) is a tuple #its a thread object
# thread objects works bit differenty then regular functions
x.start()  # this should be done to start a new thread
# NOte: This whole program main is already running in 1 thread and when we are doing threading and calling x (for now) and starting it with x.start then our current program has 2 active threads
print(threading.activeCount())  #print the active number of threads in our program.
