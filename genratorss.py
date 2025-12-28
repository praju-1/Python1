# def test(n):
#     l =[]
#     for i in range(n):
#         l.append(i)
#     return l


# print(test(6))

def test1(n):
    for i in range(n):
        yield i**2
    print(i)

print(test1(5))

# for i in test1(5):
#     print(i)