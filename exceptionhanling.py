a = 10
b = 2
from random import *
try:
    print(a/b)
    try:
        print(random())
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
finally:
    print("this will always execute")

# d = {"e":e}
# print(d)
# print(c)