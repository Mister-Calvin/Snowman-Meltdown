from ascii_art import STAGES
import random


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    """ Display the snowman stage for the current number of mistakes."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    """
    Runs one full round of the Snowman Meltdown game:
    - Selects a random secret word
    - Handles user input and validates guesses
    - Updates and displays game state after each guess
    - Ends the game with a win or loss message
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    # Main game loop
    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")

        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes >= len(STAGES) - 1:
            print("Game over! The snowman has melted. The word was:", secret_word)
            break

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman!")
            break
