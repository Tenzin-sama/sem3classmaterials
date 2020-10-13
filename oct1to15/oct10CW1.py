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
oa.start()  # starts the function defined in oa thread
sleep(0.5)  # sleep pauses the program for (x) seconds (0.5 seconds here)
ob.start()
oa.join()  # closes the oa thread after it is completed
ob.join()
# current_thread().getname() returns the name of the thread this code is in
print("BYE", current_thread().getName())
