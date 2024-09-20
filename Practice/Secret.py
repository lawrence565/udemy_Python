import random

secret = random.randint(1, 100)
ceil = 100
floor = 0
guessing = True

while guessing:
    user_guess = int(input(f"Guess a number between {floor} and {ceil}: "))
    if user_guess < floor or user_guess > ceil:
        print(f"Please guess within the range {floor} to {ceil}")
        continue

    if user_guess > secret:
        ceil = user_guess
    elif user_guess < secret:
        floor = user_guess
    else:
        print("You're success!!!!")
        guessing = False
