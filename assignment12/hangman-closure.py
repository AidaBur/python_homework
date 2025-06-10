def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        all_guessed = True

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
                all_guessed = False

        print(display)
        return all_guessed

    return hangman_closure


# Main program
if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower()
    game = make_hangman(secret)

    print("\nLet's play Hangman!\n")
    while True:
        guess = input("Guess a letter: ").lower()
        if game(guess):
            print("\nYou guessed the word! 🎉")
            break
