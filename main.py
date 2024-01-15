from art import rock, paper, scissors

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]

print("Welcom to the ROCK, PAPER, SCISSORS PYTHON GAME \n\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

object_user_choice = choices[user_choice]

print(f"\nThe user has chosen: {object_user_choice} ")

computer_choice = random.choice(choices)
computer_choice_index = choices.index(computer_choice)

print (f"The computer has chosen: {computer_choice}")

if (computer_choice == "rock" and object_user_choice == "scissors") or (computer_choice == "scissors" and object_user_choice == "paper") or ( computer_choice == "paper" and object_user_choice == "rock"):
  print("The computer win :(")
elif computer_choice_index == user_choice:
  print("Draw !!!!")
else:
  print("You beat the computer, You WIN !")
  
