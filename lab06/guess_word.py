import random

def wordgame():
    words = ["write", "program", "that", "receive", "positive",
         "change", "study", "excellent", "nice"]
    random.choice(words)
    correctletter = []
    wrongletter = []

    while len(correctletter) < len(words):
        correctletter = ""
        for letter in words:
            if letter in correctletter:
                correctletter += letter
            else:
                correctletter += "*"

        guesstest = input("(Guess) a letter in the word " + correctletter + ": ")

        if guesstest in words:
            correctletter.append(guesstest)
        else:
            wrongletter.append(guesstest)
            wrongletter += 1

    if len(correctletter) == len(words):
        print("The word is {}. You missed {} times".format(words, wrongletter))

    choice = input("Do you want to guess another word? Enter y or n: ")
    if choice == "n":
        break

wordgame()