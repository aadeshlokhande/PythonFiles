# Function

# def FunctionName(arguemts):
#     code 
#     return value 


# def greet(name):
#     print(f"Hello {name}")

# greet("aryan")


# def sum(a,b):
#     c = a + b 
#     # print(c)
#     return c

# ans = sum(1,3)
# print(ans)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# with argument with return 

# def strLen(name):
#     num = 0
#     for i in name:
#         num += 1 
#     return num 
    
# abc = strLen("vaanya")
# print(abc)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# with argument without return 

# def strLen(name):
#     num = 0
#     for i in name:
#         num += 1 
#     print(num)
    
# strLen("vaanya")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# without argument with return 

# def strLen():
#     name = input("nam bta apna = ")
#     num = 0
#     for i in name:
#         num += 1 
#     return num
    
# abc = strLen()
# print(abc)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# without argument without return 

# def strLen():
#     name = input("nam bta apna = ")
#     num = 0
#     for i in name:
#         num += 1 
#     print(num)
    
# strLen()
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# *args, **kwargs 


# def totalSum(*a):
#     ans = 0
#     for i in a:
#         ans += i 
#     print(ans)

# totalSum(10,20,34,65,34,23,65,76)


# def abc(name, age, *marks):
#     print(type(name), name)
#     print(type(age), age)
#     print(type(marks), marks)

# abc("aryan", 20, 94,93,95,96,92,91)


# def abc(**a):
#     print(a["name"])
#     print(a["age"])
#     print(a["marks"])
# abc(name = "aryan", age = 20, marks = [12,43,23,43,23,12])


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# default args

# def greet(name = "user"):
#     print(f"hello {name}")

# greet("krishna")
# greet()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def input(a):
#     print("bhula",a)

# input("enter a number = ")


