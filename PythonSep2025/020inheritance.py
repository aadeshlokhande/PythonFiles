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