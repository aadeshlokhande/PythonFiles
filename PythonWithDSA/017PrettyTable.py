# pip install prettytable ---> windows
# pip3 install prettytable ---> linux/macOS

# import prettytable
# table = prettytable.PrettyTable()

# from prettytable import PrettyTable
# table = PrettyTable(["name", "age", "Roll Number"])
# table.add_row(["manthan",69, 101])
# table.add_row(["vivan",23, 69])
# table.add_row(["shantanu",21, 106])
# table.add_row(["arjun",23, 107])
# table.add_row(["aarohi",19, 110])
# table.add_row(["bhoomi",20, 111])
# print(table)



# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# from prettytable import PrettyTable

# table = PrettyTable(list(range(1,11)))

# for i in range(1,11):
#     lst = []
#     for j in range(1,11):
#         lst.append(i*j)
#     table.add_row(lst)
# print("table")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

#  'info', 'mail', 'misc', 'open_web', 'playonyt', 'sc', 'search', 'send_hmail', 'send_mail', 'sendwhatmsg', 'sendwhatmsg_instantly', 'sendwhatmsg_to_group', 'sendwhatmsg_to_group_instantly', 'sendwhats_image', 'show_history', 'shutdown', 'system', 'text_to_handwriting', 'web_screenshot', 'whats'

# import pywhatkit as pk

# print(dir(pk))
# pk.search("demon slayer") 
# pk.playonyt("demon slayer infinity castle trailer hindi")
# pk.open_web()

# print(pk.info("tajmahal",lines=10))
# pk.text_to_handwriting("demon slayer infinity castle trailer hindi",save_to="pop.png")
# pk.image_to_ascii_art("img.png")


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# ████████████████████ Yeild ████████████████████

# def abc():
#     for i in range(1,6):
#         yield i 
    
# values = abc()
# for value in values:
#     print(value)

