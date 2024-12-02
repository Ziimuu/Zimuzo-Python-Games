from hangman import select_word, displaying_word, hangman_game, logo

print(logo)
print()

print()
print("-----------------------------------------")
print("\t\tGAME MENU")
print("-----------------------------------------")
print()


def play_hangman():
    while True:
        print("Welcome to Hangman Game!🚀🚀")
        print("Please select a category to play:")
        print("1. DC characters🦸")
        print("2. Marvel characters🦸")
        print("3. Nigerian Name📃")
        print("Press 'Q' to Quit")

        choice = input("Enter your choice (1-3): ").strip()
        if choice.lower() == 'q':
            print("Thank you for playing!")
            break

        if choice not in ['1', '2', '3']:
            print()
            print("Invalid choice! Please enter a number between 1 and 3.")
            print()
            continue

        category = {
            '1': "DC characters",
            '2': "Marvel characters",
            '3': "Nigerian Name",
        }[choice]

        word = select_word(category)
        print()
        print(f"Category: {category}")
        print("Guess the Word:", displaying_word(word, []))
        print()
        hangman_game(word)


if __name__ == '__main__':
    play_hangman()
