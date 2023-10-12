import random

user_guess = int(input("Guess the number between 1 and 100: "))
secret_number = random.randint(1, 100)

while user_guess != secret_number:

    if user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    user_guess = int(input("Guess the number between 1 and 100: "))

print('Congratulations')
