import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-+;:\|,.0123456789'
password = ""

print("Generate Your Password")
UserChoice = input("Do you want to generate a Random Password? (Yes or No): ").lower().strip()

if UserChoice == "yes" or UserChoice == "y":
    for letters in range(10):
        password =password + random.choice(chars)
    print("Generated Password:", password)
else:
    print("Okay!")
