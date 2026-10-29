# num = int(input("enter a number = "))

# if(num==0):
#     print("Even Number")
# elif(num==1):
#     print("Odd Number")
# elif(num==2):
#     print("Even Number")
# elif(num==3):
#     print("Odd Number")
# .
# .
# .
# elif(num==1000):
#     print("Odd Number")
# else:
#     print("work in progress")



file = open("main.py","w")
file.write('num = int(input("enter a number = "))\nif(num==0):\n\tprint("Even Number")\n')
num = 1
for i in range(500):
    file.write(f'elif(num=={num}):\n\tprint("Odd Number")\n')
    num+=1
    file.write(f'elif(num=={num}):\n\tprint("Even Number")\n')
    num+=1
file.write('else:\n\tprint("work in progress")')
file.close()










