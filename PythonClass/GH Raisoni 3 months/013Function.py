# Function

# def add(a=1,b=1):
#     c = a*b 
#     print(a,"x",b,"=",c)

# add(10,b=20)

# print(10,20,30)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# *args , **kwargs

# def add(*a):
#     totalSum = 0
#     for i in a:
#         totalSum+=i 
#     print(totalSum)

# add(10,20,30,40,50)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def info(**dict):
#     print(dict)
# info(name = "hardik",age= 21, branch="AI")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# Recursion 

# def abc(a):
#     if(a>=1):
#         print("Hello")
#         abc(a-1)
# abc(5)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 1+2+3.....10 = 55


# def abc(ep,sp=1,total=0):
#     if sp<=ep:
#         total = total + sp
#         print(ep,sp,total)
#         abc(ep,sp+1,total)
#     else:
#         print("total sum =",total)
# abc(10)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# factorial
# 5! = 5x4x3x2x1 = 120
# 4! = 4x3x2x1

# 5! = 5 x 4! 
# n! = n x (n-1)! 

# 1! = 1 
# 0! = 1 

# def fact(a):
#     if(a==1 or a==0):
#         return 1
#     else:
#         return a * fact(a-1)

# num = int(input("enter a number = "))
# ans = fact(num)
# print(fact(num))

