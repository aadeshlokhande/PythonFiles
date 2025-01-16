ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

num = int(input("Enter A Number = "))

thousands = int(num / 1000)
num = num % 1000
hundreds = int(num / 100)
num = num % 100
tens_place = int(num / 10)
ones_place = int(num % 10)

ans = ""

if (thousands > 0):
    ans = ans + f"{ones[thousands]} thousand "

if (hundreds > 0):
    ans = ans + f"{ones[hundreds]} hundred "

if (tens_place == 1 and ones_place > 0):
    ans = ans + f"{teens[ones_place]} "
else: 
    if (tens_place > 0) :
        ans = ans + f"{tens[tens_place]} "
    if (ones_place > 0) :
        ans = ans + f"{ones[ones_place]} "
    
print(ans.title())