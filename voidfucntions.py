from functions import *


def something():
  print("hello world")

def printnums():
  x = 0
  while x < 10:
    print("x", x)
    x += 1
def main():
  something()
  printnums()
  A = add(1,2)
  q, r = divmod2(5, 10)
  print(q,r)
  pass



if __name__ == "__main__":
  main()