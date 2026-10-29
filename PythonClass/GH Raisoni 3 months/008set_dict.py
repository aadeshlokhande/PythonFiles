# ████████████████████ Set ████████████████████

# {} ----> set 
# unorder
# store unique values

# a = {12,31,12,13,14,14,12}
# a = {50,40,60,20,10,30,90}
# print(len(a))
# print(a)

# ls = [50,40,60,20,10,40,60,20,10,40,60,20,10,40,60,20,10,40,60,20,10,30,90]
# ls = list(set(ls))
# print(ls)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ████████████████████ Dictionary ████████████████████

# {key:value} ---> dictionary
# mutable

# itemDict = {"baigan":"3Kg", "aalu":"5Kg","Dhaniya":"20Rs", "pasta":"2Kg"}
# print(itemDict)
# print(type(itemDict))
# print(itemDict["aalu"])
# print(dir(itemDict))
# print(itemDict.get("aalu"))

# itemDict["lassi"] = "3 glass"
# itemDict["aalu"] = "3KG"
# print(itemDict)

# print(itemDict.keys())
# print(itemDict.values())
# print(itemDict.items())

# itemDict.update({"adrak":"200 gm"})
# print(itemDict)

# itemDict.pop("aalu")
# print(itemDict)


# a = "Aadesh"
# lol = dict.fromkeys(a,0)
# print(lol)


# studentInfo = {
#     "stud1" : {
#         "name" : "hardik",
#         "age" : 68,
#         "percent" : 93,
#         "contact" : {
#             "home" : 9345345234,
#             "office" : 92434234234
#         }
#     }
# }
# print(studentInfo["stud1"]["contact"]["home"])
