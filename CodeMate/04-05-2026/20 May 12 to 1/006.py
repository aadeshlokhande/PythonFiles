# Random Library

# import random

# print(random.random())

# print(random.randint(1,6))
# print(random.randint(1,6))

# lst = [10,20,30,40,50,60]
# print(random.choice(lst))

# lst = ["head", "tail"]
# print(random.choice(lst))

# lst = [10,20,30,40,50,60]
# random.shuffle(lst)
# print(lst)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩


# Rock 
# paper 
# scissor

# rock <--> paper ---> paper
# paper <--> scissor ---> scissor
# scissor <--> rock ---> rock


# import random

# choices = ["rock", "paper", "scissors"]
# uwin = 0
# cwin = 0
# round = 1
# while uwin<3 and cwin<3:
#     print(f"\n\nRound No. {round}")
#     round+=1
#     user = input("Enter rock, paper, or scissors: ")
#     computer = random.choice(choices)
#     print("computer chose:", computer)
#     if user == computer:
#         print("Tie!")
#     elif user == "rock" and computer == "scissors":
#         uwin += 1
#         print(f"user win! ---> points = {uwin}")
#     elif user == "paper" and computer == "rock":
#         uwin += 1
#         print(f"user win! ---> points = {uwin}")
#     elif user == "scissors" and computer == "paper":
#         uwin += 1
#         print(f"user win! ---> points = {uwin}")
#     else:
#         cwin += 1
#         print(f"Computer wins! ---> points = {cwin}")


# if uwin==3:
#     print("user won".center(30,"@"))
# else :
#     print("Computer Won".center(30,"@"))