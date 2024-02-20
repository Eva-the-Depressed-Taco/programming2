def find_gcd(a, b):
  while b:
      a, b = b, a % b
  return a

def main():
  try:
      num1 = int(input("Enter the first non-negative number: "))
      num2 = int(input("Enter the second non-negative number: "))

      if num1 < 0 or num2 < 0:
          raise ValueError("Please enter two numbers (must be poitive).")

      gcd = find_gcd(num1, num2)

      print(f"The greatest common denominator of {num1} and {num2} is: {gcd}")

  except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()