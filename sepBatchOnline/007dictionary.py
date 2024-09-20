# dictionary - {key : value} -> mutable


# itemList = {"tamater":"2Kg", "baigan":"5Kg", "kaddu":"500Gm"}
# print(itemList["tamater"])
# print(itemList)
# print(itemList.keys())
# print(itemList.values())
# print(itemList.items())
# itemList["lehsun"] = "10Rs"
# itemList["baigan"] = "10Kg"
# print(itemList)
# itemList.update({"aalu":"3kg", "gavar":"500gm"})
# print(dir(itemList))
# print(itemList)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# itemList.clear()
# lol = itemList.copy()
# itemList.fromkeys()
# print(itemList)
# print(lol)


# a = [12,23,54]
# b = "hello"

# dictDemo = dict.fromkeys(a,b)

# print(dictDemo)
# print(itemList.get("baigan"))
# itemList.pop("kaddu")
# itemList.popitem()
# print(itemList)

# studentData = {
#     101 : {"name" : "Vaanya Bajaj",
#     'contact' : {
#         "airtel" : "9187938193813",
#         "jio" : "9187391873291"
#     },
#     "subject" : ["marathi", "hindi", "english", "history", "geography", "science"]},
# }

# print(studentData[101]["contact"]["jio"])
# print(studentData[101]["subject"][2][-3])


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# set ----> {}

# a = {12,23,54,65,23,12}
# print(dir(a))
# a = {21,43,76,98,56,35}
# print(len(a))
# print(a)


# a = [12,23,43,65,76,544,12]
# a = list(set(a))
# print(a)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦
# a = {10,20,30,40}
# b = {30,20,50}
# an = a.intersection(b)
# # an = a.union(b)
# print(an)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# a = {"gm" : "good morning", "gn":"good night"}

# var = input("enter = ")
# print(a[var])