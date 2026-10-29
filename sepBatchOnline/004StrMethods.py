# string methods

# dandar method
# a = "If you cry for me... I'll die for you "
# a = "in kutto ke samne mat nachna basanti."
# print(dir(a))
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.swapcase())

# print(a.replace("Aadesh", "Parth"))
# print(a.split())
# print(a.split("mat"))
# print(a.strip())
# print(a.center(40))

# a = "aadesh"
# print(a.center(10,"$"))

# a = "abcdef"
# print("-".join(a))

# a = ['If', 'you', 'cry', 'for', 'me...', "I'll", 'die', 'for', 'you']
# b = " ".join(a)
# print(b)

# b = a.encode()
# print(b)
# c = b.decode()
# print(c)


# print(a.index('k'))
# print(a.count('mat'))
# print(a.find("kutto"))
# ans = a.endswith("basanti.")
# ans = a.startswith("in kutto")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# a = "hello bhai... kaise ho"
# b = a.encode() 
# b'hello'

# print(b)
# c = b.decode()
# print(c)

# "aadesh123"

# "pio2943kjshdf987324jd"
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# import bcrypt

# a = "Aadesh<SIT>@1209"

# salt = bcrypt.gensalt()
# encryptPass = bcrypt.hashpw(a.encode('utf-8'), salt).decode('utf-8')
# print(encryptPass)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# format 
# name = "parth"
# age = 34


# lol = "my name is {} and my age is {} year old".format(name,age)
# print(lol)
# lol = f"my name is {name} and my age is {age} year old."
# print(lol)


# a = 10
# b = 20 
# print(f"{a} + {b} = {a+b}")