from time import time

apples = int(time())
number = apples % 20 + 1

guess = int(input("Enter a Number Guess: "))
if guess == number:
  print("you win")
else:
  print("your guess was bad and you should feel bad")