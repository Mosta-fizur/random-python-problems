import random

ur_choice = int(input("What do you want to pick? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))
if ur_choice == 0:
  print("You chose Rock")
  ur_choose = "rock"
elif ur_choice == 1:
  print("You chose Paper")
  ur_choose = "paper"
elif ur_choice == 2:
  print("You chose Scissors")
  ur_choose = "scissors"
else:
  print("You didn't choose a valid option")

options = ["rock", "paper", "scissors"]
com_choose = random.choice(options)
print("The computer chose", com_choose)
if ur_choose == com_choose:
  print("It's a tie!")
elif ur_choose == "rock" and com_choose == "paper":
  print("You lost!")
elif ur_choose == "rock" and com_choose == "scissors":
  print("You won!")
elif ur_choose == "paper" and com_choose == "rock":
  print("You won!")
elif ur_choose == "paper" and com_choose == "scissors":
  print("You lost!")
elif ur_choose == "scissors" and com_choose == "rock":
  print("You lost!")
elif ur_choose == "scissors" and com_choose == "paper":
  print("You won!")