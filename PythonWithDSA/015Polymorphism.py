# ████████████████████ Polymorphism ████████████████████

# poly - many
# morphism - forms

# compile time
# function overloading
# def calc(a,b,op):
#     if(op=="+"):
#         print(a+b)
#     if(op=="-"):
#         print(a-b)
#     if(op=="*"):
#         print(a*b)
#     if(op=="/"):
#         print(a/b)

# calc(10,20,"*")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# a = "hello arjun"
# a = (3,5,7,9,0,6)
# a = [12,43,65,45,34]
# print(len(a))
# print(dir(a))
# print(type(a))

# def add(val1, val2, Type):
#     if(Type=="str"):
#         print(f"{val1} {val2}")
#     if(Type == "int"):
#         print(f"{val1} + {val2} = {val1+val2}")

# add(10,20,"int")
# add("Adesh","Lokhande","str")

# add("Adesh","Lokhande") -------> try this
# add(12,23)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# square = a * a
# circle = 3.14 * a * a
# area(4) --> 16
# area(4,3.14) --> 16


# def area(a, pi=0):
#     if pi==0:
#         print(f"area of square is {a*a}")
#     if pi==3.14:
#         print(f"area of circle is {pi*a*a}")
#     if(pi not in (0,3.14)):
#         print(f"Area of rectangle is {a*pi}")
    
# area(4,5)
# area(4)
# area(4,3.14)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# run time 
# function overriding

# class Parent:
#     def info(self):
#         print("I am a Parent Class")
    
# class Child(Parent):
#     def info(self):
#         super().info()
#         print("I am a Child Class")

# santa = Child()
# santa.info()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# class Abc:
#     def pop(self):
#         print("this is ABC class")

# Abc.pop() #------> calling methods without creating object




# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# data.json
# dic = {
#     "student1" : {
#         "name" : "arjun",
#         "age" : 21,
#         "mobile" : {
#             "jio" : 9874324234234,
#             "airtel" : 987324978394
#         }
#     }
# }
# print(dic["student1"]["mobile"]["jio"])
# student1 --> mobile ---> jio 



