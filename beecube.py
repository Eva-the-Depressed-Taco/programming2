caltype = input("would you like to enter a base length or number of bees? length/bees: ")
if caltype == "length":
  unit = input("Enter a unit, millimeters, meters, kilometers, lightyears: ")

  if unit == "millimeters":
      millimeters = int(input("Enter Length: "))
      beeL = millimeters / 30

  elif unit == "meters":
      meters = int(input("Enter Length: "))
      beeL = meters * 1000 / 30

  elif unit == "kilometers":
      kilometers = int(input("Enter Length: "))
      beeL = kilometers * 1000 * 1000 / 30

  elif unit == "lightyears":
      lightyears = int(input("Enter Length: "))
      beeL = lightyears * 9460730472600 * 1000 * 1000 / 30

  bees = beeL ** 3
  print("Number of bees:", bees)
  #print("Cubed bees:", beeL)
elif caltype == "bees":
  print("feature unavalibe:")