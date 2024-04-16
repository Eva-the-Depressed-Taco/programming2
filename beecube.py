import math
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
  print("Number of bees: {:,.0f}".format(bees))
  #print("Cubed bees:", beeL)
elif caltype == "bees":
  bees = int(input("Number of bees: "))
  BeRoot = math.pow(bees, 1/3)
  millLength = BeRoot * 30
  meterLength = BeRoot * 30 / 1000
  killoL = BeRoot * 30 / 1000000
  lightL = BeRoot * 30 / (1000000 * 9460730472600)

  # Determine the appropriate unit based on the magnitude of length
  if lightL >= 1:
      print("The cube would be {:.10f} lightyears by {:.10f} lightyears by {:.10f} lightyears".format(lightL, lightL, lightL))
  elif killoL >= 1:
      print("The cube would be {:.10f} kilometers by {:.10f} kilometers by {:.10f} kilometers".format(killoL, killoL, killoL))
  elif meterLength >= 1:
      print("The cube would be {:.2f} meters by {:.2f} meters by {:.2f} meters".format(meterLength, meterLength, meterLength))
  else:
      print("The cube would be {:.2f} millimeters by {:.2f} millimeters by {:.2f} millimeters".format(millLength, millLength, millLength))

  
 

    
    



  
