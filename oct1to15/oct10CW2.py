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
t1 = Thread(target=oa.hello)
t2 = Thread(target=ob.hi)
t1.start()
sleep(0.5)
t2.start()
t1.join()
t2.join()

print("BYE", current_thread().getName())
