

# for item in collection:
#     print(item)
#     print(collection)
# l =(1, 2, 3, 4, 6 ,7, 8)
# l = {"Key":"Value", "Name": "John", "age":21}
# for i in l:
#     print(l[i])

# s = "Python is easy to learn"
# for i in s:
#     print(i, end="\t")

# 
# for i in l:
#     if (i == 30):
#         continue
#     print(i)


# l =[10, 20, 30, 40, 49, 20]
# for i in range(len(l)):
#     print(l[i])


# table
# n = int(input("Enter a value : "))
# for i in range(1,11):
#     print(n,"x", i, "=", n * i)

# intilization
# while (condtion):
#     # execution
#     increment/decrement

# print 1 to 10

# i = 1
# while(i<=10):
#     i += 1
#     print(i, end=" ")

# reverse list
# 
# l =[10, 20, 30, 40, 49, 20]
# a = 1
# b = len(l)-1
# while(b >= a):
#     print(l[a])
#     a -= 1


l =["hello", 12, 35, 23.5, 13.5, 56, "Good", "python", 45]

str_list =[]
num_list = []

for i in l:
    if type(i)==str:
        str_list.append(i)
    elif type(i)== int or type(i)==float:
        num_list.append(i)
print("String data ", str_list)
print("Numbers data : ",num_list)