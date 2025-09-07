# Nested for loop


# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()




# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(i):
#         print("*", end = " ")
#     print()


# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# 1
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

# for i in [1,2,3,4,5]:
#     for j in range(i,0,-1 ):
#         print(j, end=" ")
#     print()


# 1 2 3 4 5
# 2 3 4 5
# 3 4 5 
# 4 5 
# 5

# for i in range(1,6):
#     for j in range(i,6):
#         print(j, end=" ")
#     print()


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

# a = 0
# for i in range(1,5):
#     for j in range(i):
#         a += 1
#         print(a, end = " ")
#     print()

# =====================================================

# *
# * *
# * * *
# * * * *
# * * * * *

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# * * * * *
# * * * *
# * * *
# * *
# *

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1


# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

# 1 - 10 tables

# 1 - 100 counting
# 1 2 3 ......10
# 11 12 13.....20
# 21 22 23......30
# .
# .
# .
# 91 92 93......100

# ====================================================

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()


# a = 0
# for i in range(1,11):
#     for j in range(1,11):
#         a += 1
#         print(a, end = "\t")
#     print()



# ==============================================

# ASCII 
# A - 65 + 26
# a - 90


# number system 
# binary - 2 - 0,1
# octal - 8 - 0...7
# dec - 10 - 0...9
# hexa dec - 16 - 0...15, 0..9, a..f 

# A ---> 65 

# a ---> 97
# A ----> 65 


# a = ord("a")
# print(a)

# a = chr(97)
# print(a)


# a 
# b b 
# c c c 
# d d d d 
# e e e e e 

# a = ord('a')
# for i in range(1,6):
#     for j in range(i):
#         print(chr(a), end= " ")
#     a += 1
#     print()



# a 
# a b 
# a b c 
# a b c d 
# a b c d e 

# for i in range(1,6):
#     a = ord('a')
#     for j in range(i):
#         print(chr(a), end= " ")
#         a += 1
#     print()