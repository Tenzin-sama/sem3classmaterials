"""same program as earlier oct10CW1, but slightly different approach"""
from threading import *
from time import sleep


class A:
    def hello(self):
        for x in range(5):
            print("hello", current_thread().getName())
            sleep(1)


class B:
    def hi(self):
        for i in range(5):
            print("HI", current_thread().getName())
            sleep(1)


oa = A()
ob = B()
t1 = Thread(target=oa.hello)  # creating a new thread
t2 = Thread(target=ob.hi)  # creating another thread
t1.start() # starts the function defined in t1 thread
sleep(0.5)  # pauses here for 0.5 seconds
t2.start()  # starts t2 thread
t1.join()  # deletes the thread after the function within has completed
t2.join()

print("BYE", current_thread().getName())
