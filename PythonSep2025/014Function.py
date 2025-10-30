# ████████████████████ Functions ████████████████████

# build-in  ---> pre-define
# int()
# print()
# input()
# str()
# list()
# tuple()
# dic()
# set()


# user define

# def FunctionName(argument):
#     code 
#     return value 

# FunctionName(values)

# example
# def greet():
#     print("Hello buddy... Good morning")

# if
#     greet()
# 50 line 
# greet 
# 100 lines 
# greet 

# greet()
# greet()
# greet()
# greet()




# def greet(name):
#     print(f"Hello {name}... Good morning")

# greet("khushi")
# greet("aadesh")

# def greet(name,age):
#     print(f"Hello {name}... my age is {age}")

# greet("khushi",90)
# greet("aadesh",74)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# with argument with return 

# def add(a,b):
#     c = a + b 
#     return c

# ans = add(2,7)
# print("answer = ",ans)

# print("answer = ",add(10,20))
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# with argument without return 

# def add(a,b):
#     c = a + b 
#     print(f"{a} + {b} = {c}")

# add(2,7)
# add(20,70)



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# without argument with return 

# def add():
#     a = int(input("Enter a number = "))
#     b = int(input("Enter a number = "))
#     c = a + b 
#     return c 


# a = add()
# print(a)
# print(add())

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# without argument without return

# def add():
#     a = int(input("num = "))
#     b = int(input("num = "))
#     v = a + b 
#     print(v)
# add()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ Homework ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# 24 function 

# sub 
# multi 
# div 
# mod 
# sqaure
# cube 

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# keyword argument

# def info(name, roll, std):
#     print(f"My name is {name}")
#     print(f"My roll number is {roll}")
#     print(f"My std is {std}")

# # info("khushi", 103, 12)
# info(std=12, roll=1201, name="Dukhi")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# Default argument

# def add(a=0,b=0):
#     c = a + b 
#     print(c)
# add()

# def greet(name="Buddy"):
#     print(f"Good Morning {name}")
# greet()
# greet("Aman")
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# *args and **kwargs

# ARGS

# def add(name, *args):
#     totalSum = 0
#     for i in args:
#         totalSum =  totalSum+i
#     print(totalSum)


# add("Aadesh",1,5,4,6,8,6,4,3,2)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# **KWARGS

# def abc(**kwargs):
#     for i in kwargs:
#         print(i, kwargs[i])

# abc(name="Aadesh", roll="5466", std = "12th")

