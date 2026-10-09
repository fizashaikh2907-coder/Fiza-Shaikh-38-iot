sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = sum(1 for char in sentence.lower() if char in "aeiou")
spaces = sentence.count(" ")
digits = sum(1 for char in sentence if char.isdigit())

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)
