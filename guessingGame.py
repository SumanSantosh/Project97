
import random


secret_number = random.randint(1, 10)

chances_left = 5

print("Hey there! Guess a number between 1 to 10 which I am thinking of: ")


for i in range(1, 10):
  
  guess = int(input("Take a guess: "))
  

  if guess < secret_number:
    print("Guess is too low!")
  elif guess > secret_number:
    print("Guess is too high!")
  else:
    
    break

  chances_left = chances_left - 1
  print("Chances Left: " + str(chances_left))



if guess == secret_number:
  print("You guessed it right!")
else:
  print("You lose!")
  print("The number I thought was " + str(secret_number))