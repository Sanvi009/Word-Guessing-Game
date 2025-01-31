import random

def get_word():
    words = ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "strawberry", "pineapple", "mango", "peach"]
    return random.choice(words)

def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    max_guesses = 10  # Move inside the function

    while len(word_letters) > 0 and max_guesses > 0:
        print("\nYou have", max_guesses, "guesses left.")
        print("Used letters:", " ".join(sorted(used_letters)))
        print("Word:", " ".join([letter if letter in used_letters else "_" for letter in word]))

        user_letter = input("Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                max_guesses -= 1  # Now properly updates

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Please enter a valid letter.")

    # Final results
    if len(word_letters) == 0:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n❌ Sorry, you ran out of guesses. The word was:", word)

# Start the game
play_game()
