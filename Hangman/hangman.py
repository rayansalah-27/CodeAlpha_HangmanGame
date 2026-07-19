import random

# ============================
# 1. Predefined list of 5 words
# ============================
WORD_LIST = ["apple", "house", "river", "music", "smile"]

# ============================
# 2. Helper function to display the word
# ============================
def display_word(word, guessed_letters):
    """
    Returns a string showing the word with guessed letters revealed.
    Example: word="python", guessed=['p', 't'] -> "p _ t _ _ _"
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# ============================
# 3. Main game function
# ============================
def play_hangman():
    # Pick a random secret word
    secret_word = random.choice(WORD_LIST)
    
    # Track the letters the player has correctly guessed
    guessed_letters = []
    # Track all letters the player has tried (to avoid duplicates)
    used_letters = []
    # Player starts with 6 attempts
    attempts_left = 6

    print("\n" + "="*40)
    print("      WELCOME TO HANGMAN GAME!")
    print("="*40)
    print(f"You have {attempts_left} attempts to guess the word.")
    print(f"The word has {len(secret_word)} letters.\n")

    # Main game loop
    while attempts_left > 0:
        # Show current progress
        current_display = display_word(secret_word, guessed_letters)
        print(f"WORD: {current_display}")
        print(f"Attempts left: {attempts_left}")
        print(f"Letters used: {', '.join(sorted(used_letters)) if used_letters else 'None'}")

        # Ask for a letter
        guess = input("Please enter a letter: ").lower().strip()

        # --- Input Validation ---
        # Check if it's a single alphabet character
        if len(guess) != 1 or not guess.isalpha():
            print("✗ Invalid input. Please enter a single letter (a-z).\n")
            continue

        # Check if the letter was already used
        if guess in used_letters:
            print(f"✗ You already tried '{guess}'. Choose a different letter.\n")
            continue

        # Add the guess to the used letters list
        used_letters.append(guess)

        # --- Check the guess ---
        if guess in secret_word:
            # Correct guess
            guessed_letters.append(guess)
            print(f"✓ Correct! '{guess}' is in the word.\n")

            # Check if the player has won
            if all(letter in guessed_letters for letter in secret_word):
                print("="*40)
                print(f"🎉 CONGRATULATIONS! You guessed the word: {secret_word}")
                print("="*40)
                break
        else:
            # Wrong guess
            attempts_left -= 1
            print(f"✗ Wrong! '{guess}' is NOT in the word. Attempts left: {attempts_left}\n")

            # Check if the player has lost
            if attempts_left == 0:
                print("="*40)
                print(f"💀 GAME OVER! The word was: {secret_word}")
                print("="*40)
                break

# ============================
# 4. Replay loop
# ============================
def main():
    while True:
        play_hangman()
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/y or no/n): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
