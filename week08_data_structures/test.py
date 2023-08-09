import random

# List of words to choose from
words = ["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"]


def play_game():
    # Select a random word from the list
    word = random.choice(words)
    # Convert word to a list of characters
    word_letters = list(word)
    # Create a list of asterisks with the same length as the word
    display_letters = ["*" for _ in range(len(word))]
    # Initialize miss count to 0
    misses = 0

    # Loop until the word is guessed or the user quits
    while True:
        # Print the current state of the word
        print(" ".join(display_letters))
        # Prompt the user to enter a letter
        guess = input("(Guess) Enter a letter in the word ").lower()

        # Check if the guess is in the word
        if guess in word_letters:
            # Replace the asterisks with the guessed letter
            for i in range(len(word_letters)):
                if word_letters[i] == guess:
                    display_letters[i] = guess
            # Check if the word has been completely guessed
            if "*" not in display_letters:
                print(f"Congratulations! The word is {word}. You missed {misses} time(s).")
                break
        else:
            # Increment the miss count
            misses += 1
            print(f"{guess} is not in the word")
            # Check if the user has used up all their guesses
            if misses == 6:
                print(f"Sorry, you lost. The word was {word}.")
                break

        # Prompt the user to continue or quit
        choice = input("Do you want to guess another word? Enter y or n: ").lower()
        if choice == "n":
            break


# Call the play_game function to start the game
play_game()
