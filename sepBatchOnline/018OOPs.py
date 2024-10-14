# OOPs

# class 
# object 
# inheritance
# polymorphism
# abstraction 
# encapsulation

# Car ---> baleno ----> 
# mobile ----> iphone14pro -----> 3 

# single 
# multiple
# multilevel
# heirarchical


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩



# class Student:
#     "this is a student  classs"
#     def getData(self, r, a, n):
#         self.roll = r
#         self.age = a 
#         self.name = n

#     def printdata(self):
#         print(self.roll)
#         print(self.age)
#         print(self.name)

# vaanya = Student()
# vaanya.getData(102, 21, "vaanya")

# vaanya.getData(a = 21,r = 102, n = "vaanya")

# parth = Student()
# parth.getData(103, 22, "parth")
# vaanya.printdata()

# print(vaanya.__doc__)
# print(dir(vaanya))
# ishika = Student()

# print(type(ishika))
# print(ishika)
# 200
# ishika.roll = 101
# ishika.age = 21 
# ishika.name = "ishika"

# print(ishika.age)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# brand
# price 
# model 


# class Car:
#     def carInfo(self, brand, price, model):
#         self.brand = brand
#         self.price = price
#         self.model = model
        
#     def printCarInfo(self):
#         print(self.brand)
#         print(self.price)
#         print(self.model)

# baleno = Car()
# baleno.carInfo("suzuki", 800000, "baleno")

# poloGT = Car()
# poloGT.carInfo("polo", 900000, "pologt")

# x1 = Car()
# x1.carInfo("BMW", 3500000, "X1")

# poloGT.printCarInfo()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# constructor - __init__()


# class Hello:
#     def greet(self):
#         print("Hello")
    
# parth = Hello()
# parth.greet()


# class Hello:
#     def __init__(self,a):
#         print("Hello",a)
    
#     def pop(self):
#         print("buddy")
    
# parth = Hello("Parth")
# aryan = Hello("Aryan")
# aryan.pop()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# class Car:
#     def __init__(self, brand, price, model):
#         self.brand = brand
#         self.price = price
#         self.model = model
        
#     def printCarInfo(self):
#         print(self.brand)
#         print(self.price)
#         print(self.model)

# baleno = Car("suzuki", 800000, "baleno")
# poloGT = Car("polo", 900000, "pologt")
# x1 = Car("BMW", 3500000, "X1")

# poloGT.printCarInfo()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# destructor - __del__()


# class Abc:
#     def __init__(self):
#         print("file is open")

    
#     def readfile(self):
#         print("reading file")

#     def writefile(self):
#         print("writing file")

#     def __del__(self):
#         print("file closed")
    

# obj1 = Abc()

# # obj1.readfile()
# obj1.writefile()



# class Abc:
#     def __init__(self, n):
#         self.name = n
#         print("Hello", self.name)
    
#     def hwy(self):
#         print("how are you", self.name)

#     def __del__(self):
#         print("Bye bye", self.name)
    

# chandu = Abc("chandu")
# chandu.hwy()

# print(f"my name is {chandu.name}")



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ATM 

# bal.txt = 12000 =  10000 = 18000
# pin.txt = 1234 = 1122

# press 1 : withdraw
    # enter your pin = 1234
        # enter a amount = 2000
            # transaction done
            # current balance = 10000
        # low balance
    # wrong pin

# press 2 : check balance
    # enter your pin =  1234
        # current balance = 10000
    # wrong pin

# press 3 : change pin 
    # enter your pin =  1234
        # enter new pin = 1122
        # confirm your pin = 1122
            # pin changed
        # pin doesnt match
    # wrong pin

# press 4 : deposit
    # enter your pin = 1234
        # enter a amount = 8000
            # current balance = 18000
    # wrong pin

# print("thank you for using our service")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# file = open("abc.txt", "r")
# a = file.read()
# file.close()

# file = open("abc.txt", "w")
# file.write("hello budy")
# file.close()

# file = open("abc.txt", "a")
# file.write("hello budy")
# file.close()
