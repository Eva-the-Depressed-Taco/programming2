#class Cl213f:
 # def __init__(self, kwh):
  #  self.kwh = kwh
   # self.cost = 0.0

  #def calc(self):


  #def __str__(self):
   # return f"the chost of {self.kwh} is"

def main():
  try:
    with open ("LangDat/prog213F", 'r') as f:
      for line in f:
        Idata = line.split(" ")
  except Exception as e:
    print ("Error", e)
  pass



if __name__ == "__main__":
  main()


