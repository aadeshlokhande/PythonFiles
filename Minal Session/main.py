# print 

# file1 = open("abc.txt", "w")
# print("hello minal kaise ho\n"*100,file=file1)
 
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# intro - 
# comments -
# operator ----> homework
# 3 month ---> 10 

# ==============================================

# 5
# 45
# 345
# 2345
# 12345

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end="")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     print("* "*i)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if(i>=j):
#             print("*",end=" ")
#         else:
#             print("-",end=" ")
#     print()


# 80%

# * - - - - 
# * * - - -
# * * * - -
# * * * * -
# * * * * *


# num = 5
# 5x5
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# num = 3
# * * *
# *   *
# * * *
# num = int(input("enter a number = "))

# for i in range(1,num+1):
#     for j in range(1,num+1):
#         if(i==1 or i==num or j==1 or j==num):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# seconds = int(input("Enter a sec = "))
# 1 hr = 3600
# 1 min = 60
# 400 - 360 = 40
# 1 hr : 6 min : 40 sec 

# hr = seconds // 3600
# rem = seconds % 3600
# min = rem // 60
# seconds = rem % 60
# print(f"{hr}Hr : {min}Min : {seconds}Sec")

# ==============================================================


# 15 - May - 2025


# import calendar

# a = calendar.month(2025,4)
# print(a)
# a = calendar.calendar(2025)
# print(a)
# =====================================


# recursion

# 996
# def greet(a = 1):
#     print(a,"Hello")
#     greet(a+1)

# greet()


# def greet(a):
#     if(a>=1):
#         print("Hello minal....")
#         greet(a-1)
    
# greet(10)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def count(a,b = 1):
#     if (b<=a):
#         print(b)
#         count(a,b+1)
# count(7)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# factorial

# 5! = 5x4x3x2x1
# 4! = 4x3x2x1

# 5! = 5 x 4!
# n! = n * (n-1)!

# 1! = 1 
# 0! = 1

# def fact(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         return num * fact(num - 1)
    
# number = int(input("enter a number = "))
# ans = fact(number) # 5
# print(f"factorial of {number} is {ans}.")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 12345

# a = 98769
# print(str(a)[(len(str(a))//2)])

# len = 5 
# len // 2 = 2 

num = int(input("Enter a number = "))
a1 = num
lenOfnum = 0
a = -1

while num > 0:
    digit = num % 10
    num = num // 10
    lenOfnum += 1

for i in range((lenOfnum // 2)+1):
    a = a1 % 10
    a1 = a1 // 10

print(a)