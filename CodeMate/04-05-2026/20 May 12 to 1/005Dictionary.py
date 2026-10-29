# ████████████████████ Dictionary ████████████████████

# {key : value} ---> mutable

# itemDict = {"Dhaniya":"10Rs", "aalu":"2 KG", "bhindi":"0.5 kg", "baigan":"2 Kg"}

# print(itemDict)
# print(len(itemDict))
# print(type(itemDict))
# print(itemDict["aalu"])

# itemDict["bhindi"] = "1 Kg"
# itemDict["pyaj"] = "3 kg"
# print(itemDict)

# print(dir(itemDict))
# print(itemDict.keys())
# print(itemDict.values())
# print(itemDict.items())

# itemDict.clear()
# abc = itemDict.copy()
# print(abc)

# a = [10,20,30]
# abc = dict.fromkeys(a,"Not available")
# abc[10] = 1200
# print(abc)


# keys = ["name", "age", "city"]
# student = dict.fromkeys(keys, "Not Available")
# print(student)

# student = {"name": "Adesh", "age": 25}
# print(student.get("name"))
# print(student.get("city"))



# student = {"name": "Adesh", "age": 25}
# value = student.pop("age")
# print(value)
# print(student)


# student = {
#     "name": "Adesh",
#     "age": 25,
#     "city": "Nagpur"
# }
# item = student.popitem()
# print(item)
# print(student)


# student = {"name": "Adesh"}
# student.update({"age": 25, "city": "Nagpur"})
# print(student)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# abc= {
#     "gm" : "good morning",
#     "gn" : "good night"
# }

# print(abc["gn"])


# studentsInfo = {
#     "roll 1" : {
#         "name" : "Aman",
#         "age" : 21,
#         "contact" : {
#             "phone" : 9278342432,
#             "home" : 9232654643
#         }
#     },
#     "roll 2" : "aadesh"
# }

# print(studentsInfo["roll 1"]["contact"]["home"])


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ SET ████████████████████
# {} ---> random sequence ---> unique


# a = {10,20,30,10,20,50,30,40}
# print(a)

# a = [10,20,30,10,20,50,30,40]
# print(a)
# a = list(set(a))
# a.sort()
# print(a)


