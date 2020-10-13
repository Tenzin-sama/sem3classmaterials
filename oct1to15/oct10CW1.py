"""first classwork on threading"""
from threading import *
from time import sleep


class A(Thread):

    def run(self):
        for i in range(5):
            print("HELLO", current_thread().getName())
            sleep(1)


class B(Thread):

    def run(self):
        for i in range(5):
            print("HI", current_thread().getName())
            sleep(1)


oa = A()
ob = B()
oa.start()
sleep(0.5)
ob.start()
oa.join()
ob.join()
print("BYE", current_thread().getName())
