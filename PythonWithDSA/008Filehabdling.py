# ████████████████████ File Handling ████████████████████

# write mode 

# fileVar = open("abc.txt", "w")
# fileVar.write("abrakadabra")
# fileVar.close()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# read mode 

# fileVar = open("aadesh.txt", "r")
# data = fileVar.read()
# print(data)

# for i in range(8):
#     data = fileVar.readline()
#     print(i, data,end="")

# data = fileVar.readlines()

# print(data)
# fileVar.close()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# append mode 

# fileVar = open("abc.txt", "a")
# fileVar.write("abrakadabra")
# fileVar.close()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def writeData(n,a):
#     file = open("students.txt", "a")
#     file.write(f"{name},{age}\n")
#     file.close()

# name = input("enter a name = ")
# age = int(input("enter a age = "))

# writeData(name,age)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ ATM ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛

# deadline ---> 4 sep

# pin.txt ---> 1122 ----> 1234
# bal.txt ---> 12000 --> 10000 ----> 12000

# press 1 : withdraw
    # enter a pin = 1122
        # enter a amount = 2000
            # transaction done
            # current balance = 10000
        # low balance
    # wrong pin  

# press 2 : check balance
    # enter a pin = 1122
        # current balance = 10000
    # wrong pin  

# press 3 : change pin 
    # enter a pin = 1122
        # enter a new pin = 1234
        # confirm your pin = 1234
        # pin match nhi hori(gali)
        # pin changed
    # wrong pin  

# press 4 : deposit
    # enter a pin = 1234
        # enter a amount = 2000
        # current balance = 12000
    # wrong pin
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 2003 lines
# deadline ---> 6 sep

# a = int(input("enter a number = "))
# if a==0:
#     print("even number")
# elif a==1:
#     print("odd number")
# elif a==2:
#     print("even number")
#     .
#     .
#     .
#     .
# elif a==1000:
#     print("even number")
# else:
#     print("kam chal raha hai.... ")


