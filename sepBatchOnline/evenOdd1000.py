file = open("evenOdd1000.py","w")
file.write("""num = int(input("enter a number = "))\nif(num==0):\n\tprint("Even number")\n""")
num = 0
for i in range(1000):
    num += 1
    file.write(f"""elif(num=={num}):\n\tprint("Odd number")\n""")
    num += 1
    file.write(f"""elif(num=={num}):\n\tprint("Even number")\n""")
file.write("""else:\n\tprint("Out of range... (work in progress)")""")
file.close()