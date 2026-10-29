# Recursion 

# def abc():
#     print("Hello....")
#     abc() 

# abc() # ---> starting

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# def abc(a):
#     print("Hello")
#     if(a>1):
#         abc(a-1)
# abc(5)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# def count(a,b):
#     print(a)
#     if(a<b):
#         count(a+1,b)

# count(1,10)

# count(11,20)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# factorial

# 5! = 5x4x3x2x1
# 4! = 4x3x2x1 

# 5! = 5x4!

# n! = n * (n-1)!

# 1! = 1
# 0! = 1 

def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * factorial(num-1)

var = int(input("enter a number = "))
ans = factorial(var)
print("factorial =",ans)