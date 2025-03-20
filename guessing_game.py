import random

def guess_the_number(limit):
    target_number = random.randint(1, limit)
    attempts = 0
    guess = -1

    print(f"Welcome to the Guessing Game! Try to guess the number between 1 and {limit}.")
    
    while guess != target_number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess > target_number:
            print("Oops! Your guess is too high. Try again.")
        elif guess < target_number:
            print("Oops! Your guess is too low. Try again.")
        else:
            print(f"Great job! You guessed the number {target_number} in {attempts} attempts.")

max_limit = int(input("Enter the maximum limit for the number: "))
guess_the_number(max_limit)
