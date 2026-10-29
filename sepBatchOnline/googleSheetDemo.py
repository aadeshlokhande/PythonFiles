import pygsheets 

gc = pygsheets.authorize(service_file="hackathon1209-c0f6575e82d9.json")

sh = gc.open('This is demo sheet')

wks = sh.sheet1

# data = [
#     ['Naam', 'Umra', 'Shehar'],
#     ['Aadesh', '25', 'Nagpur'],
#     ['Shubham', '28', 'Pune'],
#     ['Pratik', '22', 'Mumbai']
# ]

# wks.update_values('A1', data)

print("Data successfully Google Sheets mein store ho gaya!")
