# ████████████████████ Tuple ████████████████████

# collection of objects
# () ---> tuple
# non mutable

# a = (10,12.23,"12",12,43,54,23,12)
# a = 10,20,30
# a = tuple("hello")
# print(a)
# print(type(a))

# print(dir(a))
# print(a.count("12"))
# print(a.index(12))

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ████████████████████ List ████████████████████
# collection of objects
# [] ---> list 
# mutable

# itemlist = ["baigan", "tinde", "kaddu", "aalu"]
# print(itemlist)
# print(type(itemlist))
# print(itemlist[2])
# print(dir(itemlist))

# itemlist.append("adrak")
# itemlist.insert(1,"mirchi")

# itemlist.remove("kaddu")
# itemlist.pop(2)
# itemlist.clear()
# ls = itemlist.copy()

# print(id(ls))
# print(id(itemlist))

# ls.pop(0)
# itemlist.pop(0)
# print("ls",ls)

# ls = [10,20,30]
# itemlist.extend(ls)
# itemlist.append(ls)
# a = itemlist.count("aalu")
# print(a)

# a = itemlist.index("aalu")
# print(a)


# itemlist.sort(reverse=True)
# print(itemlist)
# itemlist.reverse()
# print(itemlist)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# a = [12,34,[12,(12,34,65,23,23,[12,43,"Hello bhai",34],45),34,65,34],65,34,23]
# print(len(a))
# print(a)
# print(a[2])
# print(a[2][1])
# print(type(a[2][1]))
# print(a[2][1][5])
# print(a[2][1][5][2])
# print(type(a[2][1][5][2]))
# print(a[2][1][5][2][1:5])


# a = [12,34,[12,(12,[12,43,"Hello bhai",34],45),34],23]
# var = a[2][1][1][2][4]
# print(var)
# print(type(var))