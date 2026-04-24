word = input("Enter a word to check if it is a palindrome: ")

# text[::-1] reverses the string
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
