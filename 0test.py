""" testing new scripts here """
from threading import *
from time import sleep


class Ex:
    def test(self):
        print("t1 hello\n")
        sleep(5)
        print("Hello there!\n")
        sleep(5)
        print("Are u there?\n")
        sleep(10)
        print("Ok, bye\n")


class Ex2:
    def sum(self):
        while True:
            resp = input()
            if resp == "x":
                break
            if resp != "":
                print("Your message:",resp)


obj = Ex()
obj2 = Ex2()
t1 = Thread(target=obj.test)
t2 = Thread(target=obj2.sum)
t1.start()
t2.start()
t1.join()
t2.join()
