# ████████████████████ Inheritance ████████████████████

# parent class ---> base class 
# child class ---> derive class

# ████████████████████ single ████████████████████
# class Parent:
#     def ParentQuality(self):
#         print("paisa kamana")
    
# class Child(Parent):
#     def ChildQuality(self):
#         print("Masti Krna")

# jethalal = Parent()
# jethalal.ParentQuality()

# tappu = Child()
# tappu.ChildQuality()
# tappu.ParentQuality()

# employee ---> name, age, roll, salary, leaves = 12, id, ......100 chije
# programmer ---> leaves = 15


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ Multiple ████████████████████

# class Daddy:
#     def DadQuality(self):
#         print("cricket")

# class Mummy:
#     def MomQuality(self):
#         print("Cooking")

# class Child(Daddy, Mummy):
#     def Childquality(self):
#         print("Dancing")

# Khushi = Child()
# Khushi.Childquality()
# Khushi.MomQuality()
# Khushi.DadQuality()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ Multilevel ████████████████████
# Grandparent ---> parent ----> child 

# class GrandParent:
#     def grandParentQuality(self):
#         print("Story telling")

# class Parent(GrandParent):
#     def parentQuality(self):
#         print("Hard Working")
    
# class Child(Parent):
#     def childQuality(self):
#         print("Enjoy.. fun... chill...")

# champaklal = GrandParent()
# champaklal.grandParentQuality()

# jethalal = Parent()
# jethalal.parentQuality()
# jethalal.grandParentQuality()

# tappu = Child()
# tappu.childQuality()
# tappu.parentQuality()
# tappu.grandParentQuality()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ Heirarchical ████████████████████ 

# class Parent:
#     def parentQuality(self):
#         print("Hard working")
    
# class Child1(Parent):
#     def Child1Quality(self):
#         print("Enjoy.. fun... chill...")

# class Child2(Parent):
#     def Child2Quality(self):
#         print("Khana banana")
    
# chin1 = Child1()
# chin2 = Child2()

# chin2.Child2Quality()
# chin2.parentQuality()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# hybrid

# class A:
#     def a(self):
#         print("class A")

# class B:
#     def b(self):
#         print("class B")

# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ Homework ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛


# 1. Ek base class Animal banao aur Dog class ko usse inherit karo.
# 2. Vehicle base class banao aur Car subclass me color attribute add karo.
# 3. Shape base class banao, Circle aur Square ko inherit karwao.
# 4. Parent class Person banao, Student subclass me rollno add karo.
# 5. Employee base class se Manager subclass banao aur bonus calculate method add karo.
# 6. Bird base class banao, Sparrow subclass me fly method override karo.
# 7. Calculator class banao aur ScientificCalculator subclass me extra methods add karo.
# 8. BankAccount base class banao, SavingsAccount me interest method add karo.
# 9. Parent class Laptop banao aur GamingLaptop subclass me GPU attribute add karo.
# 10. Animal base class me sound method banao aur Cat subclass me override karo.
# 11. Appliance base class banao aur WashingMachine aur Fridge ko inherit karwao.
# 12. User base class banao, Admin subclass me delete_user method add karo.
# 13. Shape class banao aur Rectangle subclass me area method override karo.
# 14. Product base class banao, Book subclass me author attribute add karo.
# 15. Transport base class banao, Bus subclass me seats attribute add karo.
# 16. Device base class banao, Mobile subclass me call method add karo.
# 17. Parent class Course banao aur PythonCourse subclass me duration add karo.
# 18. Fruit base class banao, Mango subclass me season attribute add karo.
# 19. Parent class Animal me eat method rakho, Cow subclass me override karo.
# 20. Account base class banao, PremiumAccount subclass me cashback feature add karo.
# 21. Parent class Game banao, Cricket subclass me players method add karo.
# 22. Shape base class me draw method banao aur Triangle subclass me override karo.
# 23. Appliance base class me warranty method rakho, TV subclass me override karo.
# 24. Book base class banao, Novel subclass me genre attribute add karo.
# 25. Parent class Customer banao, RegularCustomer subclass me discount method add karo.
# 26. Device base class banao, SmartWatch subclass me steps_count attribute add karo.
# 27. Parent class Animal banao, Elephant subclass me weight attribute add karo.
# 28. Vehicle base class me start method banao, Bike subclass me override karo.
# 29. SchoolMember base class banao, Teacher subclass me subject attribute add karo.
# 30. FileHandler base class banao, TextFileHandler subclass me read_text method add karo.
