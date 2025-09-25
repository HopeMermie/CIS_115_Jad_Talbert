#This program determines if input word is a palindrome.
word = input("Please enter word: ")
def reverse_word(word):
    reverse_word = word[::-1]
    return reverse_word
if reverse_word (word) == word:
    print(f"{word} is a palindrome.")
else: 
    print(f"{word} is not a palindrome.")