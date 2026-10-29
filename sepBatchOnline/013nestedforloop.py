# nested for loop

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end = " ")
#     print()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# *
# * *
# * * *
# * * * *
# * * * * *
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# for i in range(1,6):
#     for j in range(i): # 0,1,2,3,4
#         print("*", end=" ")
#     print()
#     *
#    * *
#   * * * 
#  * * * *
# * * * * *

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 5 = 5
# 4 = 4 5 
# 3 = 3 4 5 
# 2 = 2 3 4 5 
# 1 = 1 2 3 4 5 

# for i in range(5,0, -1):
#     for j in range(i,6):
#         print(j, end=" ")
#     print()


# for i in [5,4,3,2,1]:
#     for j in range(i,6):
#         print(j, end=" ")
#     print()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 1 ----*
# 2 ---* *
# 3 --* * *
# 4 -* * * *
# 5 * * * * *

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()




#     * * * * 
# 1 * * * * * *
# 2 -* * * * *
# 3 --* * * *
# 4 ---* * *
# 5 ----* *
# 6 -----* 



# print(" ","* "*4," ")
# for i in [1,2,3,4,5,6]:
#     for j in range(1,i):
#         print(" ", end="")
#     for j in range(i,7):
#         print("*", end=" ")
#     print()


#5: 5 4 3 2 1 
#4: - 4 3 2 1
#3: - - 3 2 1
#2: - - - 2 1
#1: - - - - 1

# for i in [5,4,3,2,1]:
#     for j in range(i,5): # 1,2,3,4
#         print(" ",end=" ")

#     for j in range(i,0,-1): 
#         print(j, end=" ")
#     print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1 
# 1 
