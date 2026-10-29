# Conditional Statements

# ████████████████████ if ████████████████████ 

# if (condition):
#     code 
# code 

# age = int(input("enter your age = "))
# if age>=20:
#     print("Adult",end=" ")
# print("Boy")




# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ if else  ████████████████████

# if condition:
#     code 
# else:
#     code 


# example 1
# num = int(input("enter a number = "))
# if num==10:
#     print("number is 10")
# else:
#     print("number is not 10")

# example 2
# age = int(input("enter your age = "))
# if(age>18):
#     print("you can drive")
# else:
#     print("you can't drive")

# example 3

# num = int(input("enter a number = "))
# if(num>0):
#     print("+ve number")
# else:
#     print("-ve number")
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# 10 ---> 10.0
# 12.5 ---> 12

# var = input("enter a number = ")
# try:
#     a = int(var)
# except:
#     a = float(var)

# print(type(a))
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# a = float(input("enter a number = "))
# b = round(a)
# if a==b:
#     print("int value")
# else:
#     print("float value")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# if else ladder (elif)

# |_|
# |_|
# |_|
# |_|
# |_|
# | |



# if condition:
#     code 
# elif condition:
#     code 
# elif condition:
#     code 
# elif condition:
#     code 
# else:
#     code




# num = int(input("enter a number = "))
# if num==1:
#     print("ONE")
# elif num==2:
#     print("TWO")
# elif num==3:
#     print("THREE")
# elif num==4:
#     print("FOUR")
# else:
#     print("invalid number")
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# import keyword as ky
# # print(ky.kwlist)
# keyw=input("Enter the string=")

# if keyw in ky.kwlist:
#     print("This is a keyword in python")
# else:
#     print("This is not a keyword in Python")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# nested if else 

# if condition:
#     code
#     if condition:
#         code 
#     else:
#         code 
# else:
#     code
#     if condition:
#         code 
#     else:
#         code



# example
# age = int(input("enter your age = "))

# if age>=0 and age<=80:
#     if age>=18:
#         print("you can drive")
#     else:
#         print("you can't drive")
# else:
#     print("invalid age")


# if condition:
#     if Condition:
#         if condition:
#             code
#         else:
#             code
#     else:
#         code 
# else:
#     code 
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# GOA
# paisa >= 10000
# fds >= 5
# permission == 1 

# paisa = int(input("apka budget kitna hai = "))
# if paisa>=10000:
#     fds = int(input("kitne fds hai = "))
#     if fds>=5:
#         permission = int(input("abba ne permission di hai ky 1/0 = "))
#         if permission==1:
#             print("aap GOA ja sakte hai...")
#         else:
#             print("aap GOA nhi ja sakte")
#     else:
#         print("aur kuch fds add kro")
# else:
#     print("bhag ja bhikmange....")
    


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# match case

# match value:
#     case value1:
#         code 
#     case value2:
#         code 
#     case value3:
#         code 
#     case value4:
#         code 
#     case value5:
#         code 


# num = int(input("enter a number = "))

# match num:
#     case 1:
#         print("ONE")
#     case 2:
#         print("TWO")
#     case 3:
#         print("THREE")
#     case 4:
#         print("FOUR")
#     case _:
#         print("invalid number")



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ Homework ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛

# ████████████████████ if else ████████████████████
# get 2 numbers and print largest
# get 2 numbers and print smallest
# get a number and check its even or odd 
# get year and check its leap or not 

# ████████████████████ if else Ladder ████████████████████

# get a number and print monthname
# 3 ----> march
# 5 ---> may

# get percentage and print grades
# 23% ---> fail 

# get number and print day (1-7)

# get number and print day

# ████████████████████ Nested if else ████████████████████
# get 3 numbers and print largest number

