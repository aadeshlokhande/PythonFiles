# ████████████████████ LIST---> [] ████████████████████

# list is a mutable data type 

# a = [10,20,3.14, "aadesh"]
# print(type(a))
# print(a)
# print(a[3])



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# itemlist = ["mirchi", "aalu", "tamater", "bhindi"]
# print("Original =",itemlist)

# itemlist.insert(2,"baigan")
# itemlist.append("Kaddu")
# print(itemlist)
# itemlist.remove("bhindi")           # deleting data by value
# itemlist.pop(3)                     # deleting data by index

# print(itemlist)
# itemlist.clear()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# newlist = itemlist.copy()

# itemlist.append("lehsun")

# print(id(itemlist),itemlist)
# print(id(newlist), newlist)

# print(itemlist.count("aalu"))

# b = ["gobi", "matar", "panner"]
# itemlist.append(b)
# itemlist.extend(b)
# print(itemlist)


# print(itemlist.index("aalu"))
# itemlist.reverse()
# print(itemlist)
# itemlist.sort()
# itemlist.reverse()
# print(itemlist)


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# print(dir(itemlist))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# a = [12,43,454.756,45.765,[12,43,7623,[(12,"Abhas",43,56),54,65],654],65,"aadesh", 87]

# print(a[4][3][0][1][2])