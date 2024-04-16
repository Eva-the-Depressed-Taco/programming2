RDs = int(input("Entr Number of rubber ducks to buy: "))

price = 0
if RDs > 0 and RDs <= 99: price = 5.95
if RDs > 100 and RDs <= 199: price = 5.75
if RDs > 200 and RDs <= 299: price = 5.40
if RDs > 300: price = 5.15
total = price 
print("You owe: " + "$" + str(total))