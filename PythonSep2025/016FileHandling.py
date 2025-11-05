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


# num=int(input("enter a number"))
# file=open("ATM.txt","w")
# file.write("welcome to state bank of india")
# match(num):
# 	case 1:
# 	    print("----*withdraw*----")
# 	    pin=int(input("enter a pin"))
# 	    if(pin==112):
# 	      amoumt=int(input("enter amount="))
# 	    else:
# 	    	print("wrong pin")
# 	    print("your transaction successfully")
# 	case 2:
# 		print("----*check balance*----")
# 		pin=int(input("enter a pin"))
# 		if(pin==112):
# 			print("total balance=1000")
# 		else:
# 			print("wrong pin")
# 	case 3:
# 		print("----*change pin*----")
# 		pin=int(input("enter a pin"))
# 		if(pin==112):
# 		     newpin=int(input("enter a new pin"))
# 		     confirmpin=int(input("enter confirm pin"))
# 		else:
# 			print("wrong pin ")
# 		print("pin changed")
# 		if(pin==1234):
# 			print("pin match ho rahi h")
		
# 	case 4:
# 		print("----*deposite*----")
# 		pin=int(input("enter a pin"))
# 		if(pin==1234):
# 			amount=int(input("enter your amount"))
# 			print("your current balance=total balance-amount")
# 		else:
# 			print("wrong pin")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩



# def readPin():
#     file = open("pin.txt","r")
#     data = file.read()
#     file.close()
#     return int(data)

# def readBal():
#     file = open("balance.txt","r")
#     data = file.read()
#     file.close()
#     return int(data)

# def writePin(a):
#     file = open("pin.txt","w")
#     file.write(f"{a}")
#     file.close()

# def writeBal(a):
#     file = open("balance.txt","w")
#     file.write(f"{a}")
#     file.close()



# print("Welcome to Bank of India")

# print("Press 1: withdraw")
# print("Press 2: Check balance")
# print("Press 3: Change pin")
# print("Press 4: Deposit")
# choice = int(input("Enter your choice = "))

# match choice:
#     case 1:
#         upin = int(input("enter a pin = "))
#         pin = readPin()
#         if upin == pin:
#             amount = int(input("enter a amount = "))
#             bal = readBal()
#             if bal >= amount:
#                 print("Transacstion Done")
#                 bal = bal - amount
#                 print("current balance = ",bal)
#                 writeBal(bal)
#             else:
#                 print("Low balance")
#         else:
#             print("wrong pin")
        
#     case 2:
#         upin = int(input("enter a pin = "))
#         pin = readPin()
#         if upin==pin:
#             bal = readBal()
#             print("current balance =",bal)
#         else:
#             print("wrong pin")
        
#     case 3:
#         upin = int(input("enter a pin = "))
#         pin = readPin()
#         if pin == upin:
#             npin = int(input("enter a new pin = "))
#             cpin = int(input("confirm your pin = "))
#             if(npin==cpin):
#                 writePin(npin)
#                 print("pin changed")
#             else:
#                 print("pin doesn't match")
#         else:
#             print("wrong pin")
    
#     case 4:
#         upin = int(input("enter a pin = "))
#         pin = readPin()
#         if pin == upin:
#             amount = int(input("enter a amount = "))
#             bal = readBal()
#             bal = bal + amount
#             writeBal(bal)
#         else:
#             print("wrong pin")
        
# print("thank for using our service....")
