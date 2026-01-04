# game_logic.py
# Main game logic for Snowman Meltdown

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""

    # Clamp mistakes so no IndexError
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"Mistakes: {mistakes}/{len(STAGES) -1}")
    print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "-")
    print("Word:", display_word)
    print("\n")
    print("-" * 30)

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    # Initialize mistake counter
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    # -------------------------
    # Main game loop
    # -------------------------
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win Check ✅
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman! ⛄")
            break

        # Lose Check ⛄🔥
        if mistakes >= max_mistakes:
            print("The snowman melted! ❄️💧")
            print("The word was:", secret_word)
            break

        # Prompt user for one guess
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")

        # Ignore repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Please try again.")
            continue

        guessed_letters.append(guess)

        # Increase mistakes if guess is incorrect.
        if guess not in secret_word:
            mistakes += 1

        print("You guessed:", guess)