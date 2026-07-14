import random

def play_hangman():
    # 1. Setup: List of words and initial variables
    word_list = ["python", "coding", "intern", "alpha", "script"]
    word_to_guess = random.choice(word_list)
    guessed_letters = []
    attempts_left = 6
    
    print("Welcome to Hangman!")

    # 2. Game Loop
    while attempts_left > 0:
        # Display current word status
        display_word = [letter if letter in guessed_letters else "_" for letter in word_to_guess]
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Attempts left: {attempts_left}")
        
        # Check for win condition
        if "_" not in display_word:
            print("Congratulations! You guessed the word.")
            break
            
        guess = input("Guess a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        # Check guess against word
        if guess in word_to_guess:
            print("Good guess!")
        else:
            attempts_left -= 1
            print("Wrong guess.")
            
    if attempts_left == 0:
        print(f"\nGame Over! The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()
