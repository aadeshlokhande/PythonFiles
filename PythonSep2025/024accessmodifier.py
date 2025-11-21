# ████████████████████ Access modifier ████████████████████

# public(name), private(__name) , protected(_name)


# ████████████████████ public ████████████████████
# class Student:
#     def abc(self):
#         print("this is abc function")

# khushi = Student()
# khushi.abc()



# ████████████████████ Protected ████████████████████

# class demo:
#     def __init__(self):
#         self._age = 23
    
# class Child(demo):
#     def printData(self):
#         print(self._age)

# prem = Child()
# prem.printData()
# print("Public age = ",prem._age)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ Private ████████████████████

class Student:
    def __privateDetail(self):
        self.address = "USA"
        self.contact = 95443463463
    
    def details(self):
        self.name = "khushi"
        self.age = 20
        self.address = None
        self.contact = None
        self.__privateDetail()

    def printData(self):
        print(self.name)
        print(self.age)
        print(self.address)
        print(self.contact)

ob = Student()
ob.details()
ob.printData()





# Private variable
# class Student:
#     def __init__(self):
#         self.__age = 23

#     def printData(self):
#         print(self.__age)

# khushi = Student()
# khushi.abc()
# # print(khushi.__age)
# khushi.printData()