# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# with open("abc.txt","r") as file:
#     data = file.read()
#     print(data)

# file.read()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ████████████████████ file handling ████████████████████
# read 
# file = open("abc.txt")
# data = file.read()
# file.close()

# print(data.upper())
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# write
# file = open("abc.txt", "w")
# file.write("ganpati bappa morya...")
# file.close()

# append
# file = open("abc.txt", "a")
# file.write("\nganpati bappa morya...")
# file.close()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# a = 7

# guess the number = 5
# your number is lesser
# guess the number = 8
# your number is greater
# guess the number = 6 
# your number is lesser
# you lose

# you won

# a = 3
# for i in range(1,4):
#     num = int(input("enter a number = "))
#     if(num==a):
#         print(f"you won in {i} moves")
#         break 
#     elif(num>a):
#         print("your number is greater")
#     elif(num<a):
#         print("you number is lesser")
# else:
#     print("You Lose")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# import random
# a = random.randint(1,10)
# for i in range(1,5):
#     if(i<4):
#         num = int(input("enter a number = "))
#         if(num==a):
#             print(f"you won in {i} moves")
#             break 
#         elif(num>a):
#             print("your number is greater")
#         elif(num<a):
#             print("you number is lesser")
#     else:
#         print(f"You Lose\nValue is {a}")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦
# data.txt
# Yeh problem usually static files usually se related usually hoti hai.

# OUTPUT
# {"yeh":1, "usually":3}

# f1 = open("abc.txt", "r")
# text = f1.readline()
# f1.close()
# words = text.split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# print(freq)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# file = open("abc.txt", "r")
# data = file.read()
# lwrData = data.lower()

# lst = lwrData.split()
# dic = {}
# print(lst)
# for word in lst:
#     if word in dic:
#         dic[word] = dic[word] + 1
#     else:
#         dic[word] = 1

# print(dic)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# file = open("abc.txt", "r")
# data = file.read()
# lwrData = data.lower()
# dic = {}

# for ch in lwrData:
#     if ch in dic:
#         dic[ch] = dic[ch] + 1
#     else:
#         dic[ch] = 1
# print(dic)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩



