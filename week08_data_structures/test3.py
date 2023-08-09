import random

# List of words to choose from
words = ["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to initialize the display word with asterisks
def init_display_word(word):
    return '*' * len(word)

# Function to update the display word with correctly guessed letters
def update_display_word(word, display_word, letter):
    new_display_word = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_display_word += letter
        else:
            new_display_word += display_word[i]
    return new_display_word

# Main game loop
def play_game():
    # Choose a random word
    word = choose_word()
    # Initialize display word with asterisks
    display_word = init_display_word(word)
    # Initialize misses count
    misses = 0
    # Loop until the word is guessed or the player runs out of misses
    while True:
        # Display current state of the word
        print(display_word)
        # Prompt the player for a guess
        guess = input('Guess a letter: ').lower()
        # Check if the guess is correct
        if guess in word:
            # Update the display word with the correct guess
            display_word = update_display_word(word, display_word, guess)
        else:
            # Increment misses count if guess is incorrect
            misses += 1
            print(f'{guess} is not in the word.')
        # Check if the word has been guessed
        if display_word == word:
            print(f'Congratulations, you guessed the word {word} with {misses} misses!')
            break
        # Check if the player has run out of misses
        if misses >= 6:
            print(f'Sorry, you ran out of misses. The word was {word}.')
            break
    # Ask the player if they want to continue playing
    choice = input('Do you want to play again? (y/n) ').lower()
    if choice == 'y':
        play_game()

# Start the game
play_game()
