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