import sys


def main(args):
  if len(args) <= 0:
    print('hello')
    return
  print('hello', args)
  for arg in args:
    print(arg) 


if __name__ == "__main__":
  main(sys.argv)