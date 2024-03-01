import random


number = random.randint(1, 21)
guess = int(input("Enter a Number Guess: "))
if guess == number:
  print("you win")
else:
  print("your guess was bad and you should feel bad")