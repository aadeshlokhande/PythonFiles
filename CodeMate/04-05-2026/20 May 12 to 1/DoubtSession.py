# Doubt Session


# * * * * *
# * *   * *
# *   *   *
# * *   * *
# * * * * *

# for i in range(1,6):
#     print("#",end=" ")
#     for j in range(1,6):
#         if(i==1 or j==1 or i==5 or j==5 or i==j or (i+j)==6):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

#         * 
#       * *
#     * * *
#   * * * *
# * * * * *
# for i in range(1,6):
#     # print("#",end=" ")
#     for j in range(1,6):
#         if((i+j)>=6):
#             print("*", end=" ")
#         else:
#             print("", end=" ")
#     print()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

#1 = _____*
#2 = ____***
#3 = ___*****
#4 = __*******
#5 = _*********

# for i in range(1,6):
#     for j in range(i,6):
#         print(" ", end="")
#     for j in range((i*2)-1):
#         print("*",end="")
#     print()




# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 


# for i in range(1,6):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i,6):
#         print("*",end=" ")
#     print()
# for i in range(1,6):
#     for j in range(i,6):
#         print(" ", end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 20 25 
# 6 12 18 24 30 36 
# 7 14 21 28 35 42 49 
# 8 16 24 32 40 48 56 64 
# 9 18 27 36 45 54 63 72 81 
# 10 20 30 40 50 60 70 80 90 100


# for i in range(1,11):
#     for j in range(1,i+1):
#         print(i*j, end=" ")
#     print()





def addition(num1, num2):
    print(num1+num2)
    