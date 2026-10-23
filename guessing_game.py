import random

secret = random.randint(1, 20)
tries = 0
guess = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20.")

while guess != secret:
    guess = int(input("Enter your guess: "))
    tries = tries + 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Congratulations! You found the number.")
        print("Number of tries:", tries)