eggs = int(input("Entr Number of Eggs to buy: "))
dozens = eggs/12
price = 0
if dozens > 0 and dozens <= 4: price = 0.50
if dozens > 4 and dozens <= 6: price = 0.45
if dozens > 6 and dozens <= 11: price = 0.40
if dozens > 11: price = 0.35
total = price * dozens
print("You owe: " + "$" + str(total))