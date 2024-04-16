def fd(word):
  return word[::-1]

word = input("Enter a word: ")
fd = fd(word)
print("Flipped word:", fd)