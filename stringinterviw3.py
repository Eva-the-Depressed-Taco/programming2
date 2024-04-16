def are_anagrams():
  word1 = input("Enter the first word: ").lower().replace(" ", "")
  word2 = input("Enter the second word: ").lower().replace(" ", "")
  return sorted(word1) == sorted(word2)

if are_anagrams():
  print("The words are anagrams.")
else:
  print("The words are not anagrams.")
