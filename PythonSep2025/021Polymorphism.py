# polymorphism

# a = "10.0"
# b = [12,43,76]
# c = (12,43,65)
# d = {12,43,76}
# e = {1:10,2:20,3:30}

# print(type(a))
# print(len(c))

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def printData(self):
#         print(f"my name is {self.name} and my age is {self.age} year old")

# khushi = Student("Khushi",20)
# pratik = Student("Pratik",19)
# aadesh = Student("Adesh",89)
# shubham = Student("Shubham",120)

# StudentList = [khushi,pratik,aadesh,shubham]

# for i in StudentList:
#     i.printData()







# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩




# compile time 
# function overloding

# def calc(a,b,op):
#     if op=="+":
#         print(a+b)
#     if op=="-":
#         print(a-b)
    
# num1 = int(input("enter a number = "))
# num2 = int(input("enter a number = "))
# operator = input("enter a operator = ")
# calc(num1, num2,operator)


# run time 
# function overriding

# class parent:
#     def info(self):
#         print("Mera pass gadi hai")
    
# class child(parent):
#     def infoo(self):
#         print("mere pass mobile hai")
    
# chikku = child()
# chikku.info()