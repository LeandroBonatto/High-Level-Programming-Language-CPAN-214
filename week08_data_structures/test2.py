import random

def hangman_game():
    # create a list of words
    words = ["write", "program", "that"]

    # randomly select a word from the list
    word = random.choice(words)

    # initialize the number of misses to 0
    misses = 0

    # initialize the list of correctly guessed letters to an empty list
    correct_guesses = []

    # initialize the list of incorrectly guessed letters to an empty list
    incorrect_guesses = []

    # loop until the word is completely guessed or the number of misses exceeds 6
    while len(correct_guesses) < len(word) and misses < 6:
        # display the current progress, with asterisks for unguessed letters
        progress = ""
        for letter in word:
            if letter in correct_guesses:
                progress += letter
            else:
                progress += "*"

        # display the number of misses and the incorrectly guessed letters
        print("Misses:", misses)
        print("Incorrect guesses:", " ".join(incorrect_guesses))

        # prompt the user to guess a letter
        guess = input("Guess a letter in the word " + progress + ": ").lower()

        # if the guess is correct, add it to the list of correct guesses
        if guess in word:
            correct_guesses.append(guess)

        # if the guess is incorrect, add it to the list of incorrect guesses and increment the number of misses
        else:
            incorrect_guesses.append(guess)
            misses += 1

    # if the word is completely guessed, display a message and the number of misses
    if len(correct_guesses) == len(word):
        print("Congratulations! You correctly guessed the word", word)
        print("It took you", misses, "misses.")

    # if the number of misses exceeds 6, display a message and the word
    else:
        print("Sorry, you were unable to guess the word", word)

# start the game
hangman_game()

# ask the user if they want to play again
while input("Would you like to play again (y/n)? ").lower() == "y":
    hangman_game()