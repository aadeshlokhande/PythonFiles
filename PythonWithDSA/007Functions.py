# ████████████████████ Functions ████████████████████


# def FunctionName(args):
#     code



# def greet():
#     print("Hello user")
# greet()

# def greet(name):
#     print(f"Hello {name}")

# greet("aadesh")
# greet("vivan")
# greet("arjun")
# greet("manthan")
# greet("shantanu")

# def add(a,b):
#     print(a + b)

# add(10,20)

# print()
# input()
# int()
# list()
# tuple()
# set()
# dict()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# with argument with return

# def add(a,b):
#     c = a + b 
#     return c

# ans = add(10,20)
# print(ans)
# print(add(30,90))

# with argument without return

# def add(a,b):
#     c = a + b 
#     print(c)

# a = add(10,20)

# without argument with return
# def add():
#     a = 10
#     b = 20

#     c = a + b 
#     return c 

# value = add()
# print(value)


# without argument without return

# def add():
#     a = 10
#     b = 20
#     c = a + b 
#     print(c)

# add()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ Homework ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# sub 
# multi 
# div 
# mod 
# square
# cube 

# 24 programs

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ████████████████████ Default argument ████████████████████

# def add(a=0,b=0):
#     c = a + b 
#     print(c)

# add(10,20)
# add()
# add(30)
# add(30,20)

# ████████████████████ keyword argument ████████████████████

# def add(a=0,b=0):
#     c = a + b 
#     print(f"{a} + {b} = {c} ")

# add(b=10, a = 20)
# add(b=20)
# add(a=20)

# def info(name,age):
#     print(f"my name is {name} and my age is {age}.")

# info(age=69, name= "manthan")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ *args ████████████████████

# def add(*args):
#     totalSum = 0
#     for i in args:
#         totalSum += i 
#     print(totalSum)
# add(50,54,34)

# def abc(name, *marks):
#     print(f"my name is {name}",end=" ")
#     print("and my marks are ",end="")
#     for mark in marks:
#         print(mark, end=", ")

# abc("aadesh",54,76,56,45,34,65,76, 90)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ **kargs ████████████████████

# def info(**kargs):
#     print(kargs)

# info(maths = 90,bio = 78 )

# ████████████████████ Recursion ████████████████████


# def abc(a):
#     print(a,end=" ")
#     abc(a+1)
# abc(1)



# def abc(a):
#     if a<=10:
#         print(a,end=" ")
#         abc(a+1)
# abc(1)


# factorial
# 5! = 5x4x3x2x1 = 120
# 4! = 4x3x2x1 

# 5! = 5 x 4!

# n! = n x (n-1)!
# 1! = 1 
# 0! = 1


# def fact(a):
#     if a==1 or a==0:
#         return 1
#     else:
#         return a * fact(a-1)

# num = int(input("enter a number = "))
# ans = fact(num)
# print(ans)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 0,1,1,2,3,5,8,13,21,34

# pointer ---> id 

# ████████████████████████████████████████


# global and local variable
# a = 10 # ---> global 
# def abc():
#     print(a)
# abc()


# a = 100
# def abc():
#     # global a 
#     a = 10
#     print(id(a))

# print(a) #----> 100
# abc() #----> update by 10
# print(id(a)) 
# print(a) #---> 10




