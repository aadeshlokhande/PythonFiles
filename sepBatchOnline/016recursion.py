# inline function

# def abc(a):
#     anc = a * a 
#     return anc

# abc = lambda a : a*a
# print(abc(8))


# abc = lambda a,b : print(a + b)

# abc(3, 6)
# abc(4, 6)
# abc(5, 6)
# abc(7, 6)
# abc(8, 6)


# recursion

# def greet():
#     print("Hello ankita", end= " ")
#     greet()

# greet()


# def greet(a):
#     if(a>0):
#         print("Hello ankita")
#         greet(a-1)

# greet(10)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# *
# * *
# * * *
# * * * *
# * * * * *

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# def ptrn(a,b=1):
#     if(b<=a):
#         print("* "*b)
#         ptrn(a,b+1)

# ptrn(5)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# def table(a,b = 1):
#     if(b<=10):
#         print(f"{a} x {b} = {a*b}")
#         table(a,b+1)

# table(5)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# 5! = 5x4x3x2x1
# 4! = 4x3x2x1

# 5! = 5x4!
# n! = n x (n-1)!

# 1! = 1 
# 0! = 1 

# def factorial(num):
#     # if(num==1 or num==0):
#     if(num in [0,1]):
#         return 1
#     else:
#         return num * factorial(num-1)

# a = int(input("enter a number = "))
# ans = factorial(a)
# print(ans)


