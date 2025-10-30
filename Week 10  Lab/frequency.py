#

mySentence = input("Please enter a sentence: ")
def word_frequency(Mysentence):
    wordcount = {}
    words = Mysentence.split()
    for word in words:
        wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount
yes = word_frequency(mySentence)
print(f"{yes}")
