import random

user = input("Enter your choice (stone, paper, scissor): ").lower().strip()
choices = ["stone", "paper", "scissor"]
computer = random.choice(choices)
print(f"You chose {user} and the computer chose {computer}.")

if user == computer:
    print("It's a draw!")
elif (user == "stone" and computer == "scissor") or (user == "paper" and computer == "stone") or (user == "scissor" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
