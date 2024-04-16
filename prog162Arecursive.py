import sys
sys.setrecursionlimit(5000)

def factloop(n):
  product = 1
  for num in range(n, 0, -1):
    product *= num
  return product
def fact(n):
  if n <= 1: return n
  returm n * fact(n-1)

def main():
  num = int(input("Enter a Number, or parish like the rest"))
  while num != 0:
    factn = fact(num)
    print(f"{num}! = {factn}")
    num = int(input("Enter Number:"))

if __name__ == "__main__":
  main()
