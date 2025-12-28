
# s = f.write("good evening\n")
# print(s)
# f.close()
# b = f.write("good evening\n")
# print(b)


# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print()

f = open("abc.txt","r")
print(f.read())
# print(f.read())
print(f.tell())
print(f.seek(45))
# print(f.tell())
print(f.read())