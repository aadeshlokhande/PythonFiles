# ████████████████████ Conditional Statements ████████████████████

# ████████████████████ if ████████████████████

# syntax
# if (condition):
#     code #:-----> space(indentation)


# age = 90

# if age>18:
#     print("helloo")
#     print("helloo")
#     print("helloo")
#     print("helloo")
#     print("helloo")

# print("Aadesh")

# age = int(input("Enter your age = "))

# if (age >= 18):
#     print("Adult",end = " ")

# print("Boy")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ if else ████████████████████

# syntax
# if condition:
#     code
# else:
#     code 


# num = 450
# if num<100:
#     print("yes")
# else:
#     print("No")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# age = int(input("enter your age = "))
# if(age>18):
#     print("you can vote...")
# else:
#     print("you can't vote")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# num = int(input("enter a number = "))
# if (num > 0):
#     print("+ve number")
# else:
#     print("-ve number")

# <------------------- 0 ---------------->
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# number = int(input("enter a number = "))

# if number%2 == 0:
#     print("even number")
# else:
#     print("Odd number")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# num = int(input("bhgwan ke nampe dede re baba = "))
# if num>9 and num<100:
#     print("Yes")
# else:
#     print("No")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# name = input("enter your name = ")

# if name=="abhas" or name=="akshay":
#     print("Hiiiiiii")
# else:
#     print("Bye Bye")

# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛ Homework ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛
# ⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛⊛


# 1.Ek number input lo aur check karo ki wo positive hai ya negative.

# 2.Ek number input lo aur check karo ki wo even hai ya odd.

# 3.Ek person ki age input lo aur check karo voting ke liye eligible hai ya nahi (age ≥ 18).

# 4.Do numbers input lo aur batao kaunsa bada hai.
# a  = int(input("enter a number = "))
# b  = int(input("enter a number = "))
# if(a>b):
#     print(a,"is greater")
# else:
#     print(b, "is greater")

# 5.Teen numbers input lo aur sabse bada number find karo.
# a = int(input("enter a number = "))
# b = int(input("enter a number = "))
# c = int(input("enter a number = "))

# if a>b and a>c:
#     print(a,"is greater")

# if b>a and b>c:
#     print(b, "is greater")

# if c>a and c>b:
#     print(c,"is greater")

# 6.Ek number input lo aur check karo ki wo 5 se divisible hai ya nahi.

# 7.Ek year input lo aur check karo ki wo leap year hai ya nahi.

# 8.Ek character input lo aur check karo ki wo vowel hai ya consonant.
# ch = input("enter a char = ")
# if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#     print(ch, "is vowel")
# else:
#     print(ch,"is consonant")

# 9.Ek student ke marks input lo aur check karo ki wo pass hai ya fail (passing marks = 35).
# mark = int(input("enter a mark = "))
# if mark>=35:
#     print("Pass")
# else:
#     print("Fail")

# 10.Ek student ke marks input lo aur grade decide karo (A, B, C ya Fail).
# fail = 0-34
# c = 35-70
# b = 70-90
# a = 90 - 100

# marks=int(input("enter student marks"))
# if marks>=0 and marks<=34:
#     print("fail")
# if marks>=35 and marks<70:
#     print("C grade")
# if marks>=70 and marks<90:
#     print("B grade")
# if marks>=90 and marks<=100:
#     print("A grade")
# if marks>100:
#     print("100 se jyada marks nhi milte")
# if marks<0:
#     print("gadhe 0 se kam marks nhi mil sakte")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# 11.Ek number input lo aur uska absolute value print karo.
# num = int(input("enter a number = "))

# if num<0:
#     num = -num

# print(num)


# + * + = +
# + * - = - 
# - * + = - 
# - * - = + 


# 12.Ek number input lo aur check karo ki wo 3 aur 5 dono ka multiple hai ya nahi.

# 13.Do strings input lo aur check karo ki wo equal hai ya different.

# 14.Do numbers input lo aur smallest number print karo.

# 15.Ek number input lo aur check karo ki wo zero, positive, ya negative hai.

# 16.Ek character input lo aur check karo ki wo uppercase hai ya lowercase.

# 17.Ek triangle ke 3 sides input lo aur check karo ki wo valid triangle hai ya nahi.

# 18.Ek person ki age input lo aur check karo ki wo child, teenager, adult, ya senior citizen hai.

# 19.Do numbers input lo aur user se operator (+, -, *, /) input lo. Result calculate karo (simple calculator).

# 20.Ek number input lo aur check karo ki wo prime number hai ya nahi.