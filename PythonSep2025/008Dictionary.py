# ████████████████████ Dictionary  ████████████████████

# dic --> {key:value, key1:value,}
# mutable

# itemdic = {"aalu" : "2Kg", "tamater":"1kg", "dhaniya":10}
# print(itemdic)
# itemdic.clear()
# itemdic["tamater"] = "20Kg"
# itemdic.setdefault("bhindi","5Kg")
# a = itemdic.copy()
# itemdic["pop"] = 10
# print(a)

# print(itemdic)


# print(type(itemdic))
# print(itemdic["Aalu"])
# itemdic["mirchi"] = "30Rs"
# itemdic["dhaniya"] = 50
# print(itemdic)

# print(itemdic.keys())
# print(itemdic.values())
# print(itemdic.items())

# [('aalu',2kg),(tamater,1kg),()]

# print(dir(itemdic))
# print(itemdic.get("aalu"))

# itemdic.pop("aalu")
# print(itemdic)
# itemdic.update({"bhindi":"3kg", "adrak":30})
# print(itemdic)



# a = [10,20,30,40,50,60]
# newDic = dict.fromkeys(a, "hello")
# print(newDic)

# a = "hello bhai kaisa hai, mujhe bhul toh nhi gya"
# dic = dict.fromkeys(a,0)
# print(dic)
# for ch in a:
#     dic[ch] += 1
# print(dic)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ set ████████████████████

# a = {10,20,10,30,40,20,30,40,50,20}
# print(a)

# a = "adesh lokhande, njai kaisa hai"
# b = set(a)
# print(b)

# a = {12,32,54,65,76,87}
# b = {12,32,54,65,45,34}
# c = a.union(b)
# c = a.intersection(b)

# print(c)
# print(dir(a))