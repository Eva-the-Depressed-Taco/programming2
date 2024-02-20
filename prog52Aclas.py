class Shape:
  def __init__(self, length, width):
  self.lenght = length
  self.width = width
  self._area = 0
  self._perim = 0


  def calculate(self):
    self._area = self.length * self.width
    self._perim = self.length * 2 + self.width * 2

  def setlength(self, length):
    self.length = length

  def getArea(self):
    return self._area
  def getPerim(self):
    return self._perim

def main():
  len = int(input("Enter length"))
  wid = int(input("Enter length"))
  shape = Shape(len, wid)
  shape.calculate
  print("Area", shape.getarea())
  print("Perim", shape.getPerim())
  pass



if __name__ == "__main__":
  main()