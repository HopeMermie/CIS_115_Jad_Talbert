#
mySentence = input("Please enter a sentence: ")
def word_frequency(mySentence):
    words = mySentence.split()
    for key, value in mySentence.split():
        print(f"{key}: {value}")
word_frequency(mySentence)
