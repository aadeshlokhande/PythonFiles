# ████████████████████ Collection Of Data  ████████████████████

# var = 10
# var = 10.7
# var = "10.7"

# ████████████████████ String ████████████████████

# a s f h r f h r 
# S G R D G 
# 1 3 5 6 
# % # % & $ @ 
# "hello"

# a = 'hello'
# a = "hello"
# a = "this is my mom's mobile"
# a = 'modi said "hello mitro..."'
# print(a)

# a = '''hello asdasdd'''
# a = """hello"""

# a = str(190254)
# print(a)
# print(type(a))

# ████████████████████ slicing ████████████████████
# var = "awaj dur dur tak jani chahiye...."

# var = "Aadesh Lokhande"

# print(type(var))
# print(var)
# print(var[4])
# print(var[-4])
# print(var[1:4])
# print(var[-6:-2])
# print(var[1:13:2])
# print(var[13:1:-2])
# print(var[2:])
# print(var[:13])
# print(var[:])
# print(var)
# v = var[14::-1]
# print(v)

# ████████████████████ String Methods ████████████████████

# pushpa = "dam hai toh rok ke dikha shakawat"

# print(type(pushpa))
# print(len(pushpa))
# print(dir(pushpa))

# print(pushpa.capitalize())
# print(pushpa.upper())
# print(pushpa.title())
# print(pushpa.lower())
# print(pushpa.swapcase())

# print(pushpa.center(20,"█"))
# print(pushpa.ljust(20,"█"))
# print(pushpa.rjust(20,"█"))

# print(pushpa.count("a"))
# print(pushpa.index('m'))

# print(pushpa.find("ai"))

# print(pushpa.encode())
# print(pushpa.isalnum())

# pushpa = "dam hai toh rok ke dikha shakawat"
# a = pushpa.split()
# print(a)
# b = " ".join(a)
# a = pushpa.replace("rok", "tok")
# print(a)

# a = "     hello asda asdad    "
# print(a.strip())

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# a = "123123pop "
# utf-8
# utf-16

# import string

# print(string.__doc__)
# print(dir(string))
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ Tuple ████████████████████

# non-mutable
# (values/objects)

# a = (12,43,65,87,65,87,65,87)
# a = 54,76,45,32
# print(a)
# print(type(a))
# print(a[1])
# print(a[-1] * 10)

# print(dir(a))
# print(a.count(87))
# print(a.index(87))

# (a,b,c) = (10,20,30)
# a,b,c = 10,20,30

# a = tuple("hello")
# print(a)

# s1 = 943634543,934534543,9345353,94353534,934534534
# s1[index]

# student = (id, pass)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ████████████████████ LIST ████████████████████

# [values/ objects]
# mutable


# a = [12,32,"sadada", (12,54, ["1232"]),12,65]
# a = [10,20,30]
# print(a)
# print(type(a))
# print(len(a))
# print(a[1])

# itemList = ["tamater", "aalu", "baigan"]
# print(itemList)
# itemList.append("mirchi")
# print(itemList)
# itemList.insert(1,"adrak")
# print(itemList)
# itemList.remove("baigan")
# itemList.pop(3)
# print(itemList)
# itemList.clear()


# print(itemList)
# items2 = itemList.copy()
# print(id(itemList))
# print(id(items2))
# print("itemlist = ",itemList)
# print("items2= ",items2)

# print(itemList.count("aalu"))
# itemList.extend(["bhindi", "shimla mirch", "kaddu"])

# a = itemList.index("aalu")
# itemList.sort()
# itemList.reverse()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# dictionary
# set



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# def multi10(var):
#     return var*10
# lst1 = [2,5,8,6]
# # lst2 = map(multi10,lst1)
# lst2 = []
# for i in lst1:
#     lst2.append(multi10(i))
# print(lst2)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩