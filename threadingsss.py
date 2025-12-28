import threading
from threading import *

def delayed():
    print("this function will execute later")


t = threading.Timer(3, delayed)
t.start()







# print(threading.active_count())
# print(threading.main_thread())

# t1 = Thread(target, arg)
# t1.start()
# t1.join()

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")

    
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")

# t1 = Hello()
# t2 = Hi()

# t1.start()
# t1.join()
# t2.start()
# # t2.join()

# print(threading.active_count())