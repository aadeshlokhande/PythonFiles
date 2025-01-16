# polymorphism

# poly-----> many
# morphism -----> forms

# a = "hello"

# a = (12,43,54,65)

# print(len(a))
# print(type(a))

# RDJ ---> ironman ----> tony stark

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# compile time polymorphism
# function overloading  

"""
# c++
calc() ----> "hello"
calc(int a) -----> a*a = 9
calc(float a) ---> a*a*a
calc(int a, int b) ---> a + b

calc(3,4) ----> call
"""

# def calc(op, a,b):
#     if(op=="+"):
#         print(a+b)
#     if(op=="-"):
#         print(a-b)
#     if(op=="*"):
#         print(a*b)
#     if(op=="/"):
#         print(a/b)

# calc("/", 10,20)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def add(dt, a,b):
#     if(dt == "str"):
#         print(f"{a} {b}")
#     if(dt == "int"):
#         print( a + b )

# add("str", "aadesh", "lokhande")
# add("int", 12,23)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def add(a,b):
#     if(type(a)==type("") and type(b)==type("")):
#         print(f"{a} {b}")

#     if(type(a)==type(0) and type(b)==type(0)):
#         print( a + b )

# add("aadesh", "90")
# add(12,53)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# run time polymorphism
# function overriding

# class Mom:
#     def info(self):
#         print("I am a Mom class")

# class Dad:
#     def info(self):
#         print("I am a dad class")

# class Child(Mom, Dad):
#     def info(self):
#         print("I am a child class")

# aryan = Child()
# aryan.info()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

class Student:
    def __init__(self, n):
        self.name = n 

    def printData(self):
        print(f"My name is {self.name}")
    
aadesh = Student("Aadesh")
aryan = Student("aryan")
parth = Student("parth")
krishna = Student("krishna")
vaanya = Student("vaanya")
ishika = Student("ishika")

lst = [aadesh, aryan, krishna, parth, ishika, vaanya]

for i in lst:
    i.printData()