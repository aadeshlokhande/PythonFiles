# nested for loop

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()


# 1 = *
# 2 = * *
# 3 = * * *
# 4 = * * * *
# 5 = * * * * *

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# ===============================

# 1 = * * * * *
# 2 = * * * *
# 3 = * * *
# 4 = * *
# 5 = *

# for i in range(1,6):
#     for j in range(i, 6):
#         print("*", end=" ")
#     print()





# 5 = * * * * *
# 4 = * * * *
# 3 = * * *
# 2 = * *
# 1 = *

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end = " ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()



# ==================================



# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print( j,end=" ")
#     print()


# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5


# for i in range(5,0,-1):
#     for j in range(i,6):
#         print( j,end=" ")
#     print()


# =================================
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i*j}",end="\t")
#     print()


# 1 2 3 4 ....10
# 11 12 13 14.....20
# 21 22 23......30
# .
# .
# .
# 91 92 93......100

# a = 0
# for i in range(1,11):
#     for j in range(1,11):
#         a += 1
#         print(a,end="\t")
#     print()