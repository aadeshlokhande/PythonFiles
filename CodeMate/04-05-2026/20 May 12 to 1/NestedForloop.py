# Nested for loop

# 1 5 = *
# 2 4 = * *
# 3 3 = * * *
# 4 2 = * * * *
# 5 1 = * * * * *

# for i in range(1,6):
#     for j in range(i):
#         print("*",end = " ")
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


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()


# 5
# 5 4 
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j, end=" ")
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

# a = 1
# for i in range(1,5):
#     for j in range(i):
#         print(a,end=" ")
#         a += 1
#     print()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# 1 5 = 5
# 2 4 = 4 5
# 3 3 = 3 4 5
# 4 2 = 2 3 4 5
# 5 1 = 1 2 3 4 5 

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j, end=" ")
#     print()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# 1 2 3 ... 10 
# 11 12 13...20
# 21 22 23....30
# .
# .
# .
# 91 92 93.....100

# a = 1
# for i in range(1,11):
#     for j in range(1,11):
#         print(a,end="\t")
#         a = a + 1
#     print()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 1 2 3 4....10
# 2 3 6 8....20
# 3 6 9 12...30
# .
# .
# .
# 10 20 30 ....100

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()




