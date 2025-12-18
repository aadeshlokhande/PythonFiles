# 9. Write a program to swap two numbers using a third variable.

# a = 10 
# b = 20 
# print(f"Before swapping a = {a} and b = {b}")

# without using 3rd variable
# a = a+b # a = 30
# b = a-b # b = 10
# a = a-b # a = 20

# using 3rd variable
# c = a 
# a = b 
# b = c 

# using tuple property
# a,b = b,a

# print(f"After swapping a = {a} and b = {b}")
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 47. Write a program to print ASCII value of a character.



# 48. Write a program to convert ASCII code to character.



# binary -->          2 --> 0,1 
# octal -->           8 --> 0...7
# decimal -->         10--> 0..9
# hexadecimal -->     16--> 0..9, a,b,c,d,e,f 

# 10 ---> 1010
# a ---> 65
# ANSI ---> ASCII 

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# chr() ----> dec to char
# ord() ---> char to dec 
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# a = 'A'
# print(ord(a))

# _ = 65
# print(chr(_))

# a = "Aadesh"
# for i in a:
#     print(ord(i))


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# 70. Write a program to find average of numbers in a list.
# a = [45,76,87,45,34,65,87,98,67,56,654]
# totalSum = 0
# length = len(a)
# for i in a:
#     totalSum += i 

# print(totalSum/ length)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 78. Write a program to calculate BMI.

# w = int(input("Enter a w = "))
# h = float(input("Enter a h = "))
# ans = w / (h*h)
# print(f"{w}/{h*h} = {ans}")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# for i in range(1,6):
# 	for j in range(1,6):
# 		if(i==1 or i==5 or j==1 or j==5 ):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()



# ████████████████████████████████████████
# 1. Write a program to check if a number can be written as sum of two prime numbers.

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# found = False

# for i in range(2, num):
#     if is_prime(i) and is_prime(num - i):
#         print(f"{num} = {i} + {num - i}")
#         found = True
#         break

# if not found:
#     print("Number cannot be written as sum of two prime numbers")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# 2. Write a program to find all pairs in a list whose sum is equal to a given number (without using any library).
# 10 = (9,1), (8,2), (7,3),....

# num = int(input("enter a number = ")) # 15
# lst = []
# for i in range((num//2)+1):
#     lst.append((i,num-i))
# print(lst)


# numbers = [2, 4, 3, 5, 7, 8, 9]
# target = 10
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if target == numbers[i]+numbers[j]:
#             print(f"{target} = {numbers[i]} + {numbers[j]}")



# 5. Write a program to check if a number has all unique digits or not.
# 435637 ---> not 
# 3245 ---> yes 

# num = int(input("enter a number = "))
# s = str(num)
# ns = set(s)
# if(len(s) == len(ns)):
#     print("YES")
# else:
#     print("NO")


# "1234" --> 4
# {1,2,3,4} ---> 4 
# YES

# "1232" --> 4
# {1,2,3} ---> 3 
# NO 