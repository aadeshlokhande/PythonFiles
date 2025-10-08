# ████████████████████ Inheritance ████████████████████


# # Single
# class Parent:
#     def parentQuality(self):
#         print("Paisa kamana...")

# class Child(Parent):
#     def childQuality(self):
#         print("Paisa Udana...")
    
# # jethalal = Parent()
# # jethalal.parentQuality()

# tappu = Child()
# tappu.childQuality()
# tappu.parentQuality()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# multiple
# class Dad:
#     def dadQuality(self):
#         print("Finance Management")
    
# class Mom:
#     def momQuality(self):
#         print("Khana Banana...")

# class Child(Dad, Mom):
#     def childQuality(self):
#         print("Masti krna...")

# manthan = Child()

# manthan.childQuality()
# manthan.momQuality()
# manthan.dadQuality()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# Multilevel

# class GrandParent:
#     def grandParentQuality(self):
#         print("Story telling")

# class Parent(GrandParent):
#     def parentQuality(self):
#         print("guitar")

# class Child(Parent):
#     def childQuality(self):
#         print("Chaman dhokla...")

# aman = Child()
# aman.childQuality()
# aman.parentQuality()
# aman.grandParentQuality()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# Heirarchical

# class Parent:
#     def parentQuality(self):
#         print("Singing")

# class Child1(Parent):
#     def child1Quality(self):
#         print("guitar")

# class Child2(Parent):
#     def child2Quality(self):
#         print("dance")

# bablu = Parent()
# bablu.parentQuality()

# chin1 = Child1()
# chin1.child1Quality()
# chin1.parentQuality()

# chin2 = Child2()
# chin2.child2Quality()
# chin2.parentQuality()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# Hybrid

# class A:
#     def a(self):
#         print("A class")
    
# class B(A):
#     def b(self):
#         print("B class")

# class C(A):
#     def c(self):
#         print("C class")

# class D(B,C):
#     def d(self):
#         print("D Class")

# ob = D()

# print(dir(ob))

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩