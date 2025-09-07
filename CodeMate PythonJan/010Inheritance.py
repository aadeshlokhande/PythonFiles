# INHERITANCE
# ===========================================
# class abc:
#     def funA():
#         print("hello Buddy")
#
# abc.funA()

# =========================================
# single


# class A ----> 50 function
# class B ---> 50 function + 3 function

# parent ---> base
# child ----> derive

# class A:
#     def Fun_a(self):
#         print("I am a Func A from A class")
#
#     def Fun_B(self):
#         print("I am a Func B from A class")
#
# class B(A):
#     def Fun_c(self):
#         print("I am a Func C from B class")
#
# # obA = A()
# # obA.Fun_B()
#
# obB = B()
# # print(dir(obB))
# obB.Fun_a()
# obB.Fun_B()
# obB.Fun_c()
# ===========================================

# class Parent:
#     def parentQuality(self):
#         print("Paisa kamana")

# class Child(Parent):
#     def childQuality(self):
#         print("paisa udana... masti krna")

# jethalal = Parent()
# jethalal.parentQuality()
# jethalal.childQuality()

# tappu = Child()
# tappu.childQuality()
# tappu.parentQuality()

# ==========================================================
# multiple

class Dad:
    def dadQuality(self):
        print("Maths")

class Mom:
    def momQuality(self):
        print("singing")

class Child(Mom,Dad):
    def childQuality(self):
        print("masti....")

aman = Child()
aman.dadQuality()
aman.momQuality()
aman.childQuality()






# ====================================================
# multilevel
# heirarchical