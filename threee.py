from threading import Thread
from time import sleep

class Mythread:
    def maketea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Add sugar and tea")
        sleep(3)
        print("Done")

    def task2(self):
        print("Add Milk")
        sleep(3)
        print("Done")

    def task3(self):
        print("Filter it")
        sleep(3)
        print("Done")

o = Mythread()

t = Thread(target=o.maketea)
t.start()
t.join()