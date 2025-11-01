# File Handling

# RAM
# fast
# expensive ---> 8 gb ---> 2000
# volatile
# a = 10

# ROM -----> hard disk
# slow
# 512 GB -----> 2000
# non volatile
# data ---> file ---> ROM
# ===========================================

# read mode 
# file = open("abc.txt","r")
# data = file.read()
# print(data.upper())
# file.close()

# file = open("abc.txt","r")
# for i in range(8):
#     a = file.readline()
#     print(a.upper())
    
# =========================================
# write mode 

# file = open("xyz.txt","w")
# file.write("kitne aadmi the....")
# file.close()
# =========================================

# append mode 

# file = open("ijk.txt","a")
# file.write("abrakadabra..\n")
# file.close()
# ===========================================

# get name, and, rollnumber and store it into Student.txt file 
# open file and read all the data from file 

# ATM 
# pin.txt ----> 1122 --->1234
# balance.txt ---> 12000 ---> 10000 ----> 12000

# press 1: withdraw
    # enter a pin = 1122
    #     enter a amount = 2000 
    #         your transaction successfull
    #         your current balance = 10000
    #     low balance
    # wrong pin 

# press 2: check balance
# enter a pin = 1122
    # balance = 10000
# wrong pin     

# press 3: change pin 
# enter a pin = 1122
#     enter a new pin = 1234
#     confirm you pin = 1234
#         pin changed
#     pin match nhi ho rahi hai.... 
# wrong pin 

# press 4: deposit
# enter a pin = 1234
    # enter a amount = 2000 
    # your current balance = 12000
# wrong pin 


