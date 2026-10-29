# ████████████████████ List ████████████████████
# List ---> [] ---> mutable

# itemlist = ["dhaniya", "baigan", "aalu", "bhindi"]

# print(itemlist)
# print(type(itemlist))
# print(itemlist[1])
# print(itemlist[1:3])

# methods
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# print(dir(itemlist))
# itemlist.append("pyaj")
# itemlist.insert(1,"Mirchi")
# print(itemlist)
# itemlist.remove("bhindi")
# itemlist.pop(4)
# print(itemlist)

# a = itemlist.count("aalu")
# print(a)
# itemlist.clear()
# print(itemlist)

# newList = itemlist.copy()
# itemlist.pop(2)
# print("newList =",newList)

# newlist = [12,43,65]
# itemlist.extend(newlist)
# print(itemlist)

# a = itemlist.index("aalu")
# print(a)

# itemlist.sort()
# itemlist.reverse()
# print(itemlist)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# lst = ["hello", 12,[12,43,"23235345",["nhi bhai",345345],65],54,756.453]

# print(lst)
# print(len(lst))
# print(lst[2])
# print(len(lst[2]))
# print(lst[2][3])
# print(len(lst[2][3]))
# print(lst[2][3][0])
# print(lst[2][3][0][2])


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# ████████████████████ Tuple ████████████████████

# tuple --> () ---> non-mutable
# a = (12,43,76,12,43,12,343,65,34)

# print(a)
# print(type(a))
# print(dir(a))
# print(a[2])
# print(a.index(343))
# print(a.count(12))

# a = 12,34,65
# print(a)

# (a,b,c) = (12,13,14)
# print(b)