
import random


secret_number = random.randint(1, 10)

chances_left = 5

print("Hey there! Guess a number between 1 to 10 which I am thinking of: ")


while chances_left > 0:

    guess = int(input("Take a guess: "))

    if guess == secret_number:
        print("You guessed it right!")

    elif guess < secret_number:
        print("Guess is too low!")

    elif guess > secret_number:
        print("Guess is too high!")

    chances_left = chances_left - 1
    print("Chances Left: " + str(chances_left))


if chances_left == 0:
    print("You have lost the game")
