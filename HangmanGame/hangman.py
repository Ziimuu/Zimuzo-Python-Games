# import random
import random


def select_word(category):
    # Selects a random word from the specified category.
    #
    # Args:
    #     category (str): The category of words to choose from.
    #
    # Returns:
    #     str: A randomly selected word from the specified category.

    words = {
        "DC characters": ["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN"],
        "Marvel characters": ["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
        "Nigerian Name": ["Esther", "Mustapha", "David", "Micheal", "John"],
    }
    return random.choice(words[category])


def displaying_word(word, guessed_letters):
    # Creates a display string for the word, showing guessed letters and underscores for unguessed letters.
    #
    # Args:
    #     word (str): The target word.
    #     guessed_letters (list): List of letters guessed by the player.
    #
    # Returns:
    #     str: The word with underscores for unguessed letters.

    display = ""
    for letter in word:
        if letter.upper() in guessed_letters or letter == ' ':
            display += letter
        else:
            display += "_"
    return display


def select_hint(word):
    # Selects two random letters from the word as a hint.
    #
    # Args:
    #     word (str): The target word.
    #
    # Returns:
    #     list: A list containing two randomly selected letters from the word.
    #
    hint_letters = random.sample(word, 2)
    return hint_letters


def hangman_game(word):

    # Implements the Hangman game logic.
    #
    # Args:
    #     word (str): The target word to guess.
    #
    # Returns:
    #     None

    # Initialize the game with the target word and set the number of chances
    word = word.upper()  # Convert the word to uppercase for consistency
    guessed_letters = []  # Create an empty list to store guessed letters
    chances = 6  # Set the maximum number of chances the player has

    # Start the game loop
    while chances > 0:
        # Display hangman art based on remaining chances
        print(hangman_art[6 - chances])

        # Display the word with guessed letters (showing underscores for unguessed letters)
        print("Word:", displaying_word(word, guessed_letters))
        print("'Hint' costs 1 life 🙂🙂🙂 ")
        print()

        # Get the player's guess (or other commands like 'hint' or 'quit')
        guess = input("Enter your guess (or type 'hint' for a hint or type '0' to quit): ").strip().upper()

        if guess == 'HINT':
            # Provide a hint by showing two random letters from the word
            hint = select_hint(word)
            chances -= 1
            print(f"{chances} chances left.😥😥\n\n")
            print("Hint:", ''.join(hint))
            print()
        if guess == "0":
            # Player wants to quit the game
            print("Try again next time!")
            print()
            break
        if len(guess) != 1 or not guess.isalpha():
            # Check if the input is a single letter
            print("Please enter a correct letter.")
            continue
        if guess in guessed_letters:
            # Check if the letter has already been guessed
            print("You've already guessed that letter.😥")
            continue
        else:
            # Add the guessed letter to the list
            guessed_letters.append(guess)

        if guess not in word:
            # Incorrect guess: reduce chances and inform the player
            chances -= 1
            print("❌Wrong guess!❌ You have", chances, "chances left.😥😥\n\n")
        elif all(letter in guessed_letters for letter in word):
            # Player guessed the entire word correctly
            print("Congratulations!🥳🥳 You guessed the word:", word, "🥂\n\n")
            break

    # Game over: display the correct word if chances run out
    if chances == 0:
        print("Game Over! The word was:", word)
        print()


hangman_art = [
    '''
     +--------+
     | |
     |
     |
     |
     |
  _______________
  ''',
    '''
     +--------+
     | |
     O |
       |
       |
       |
  _______________
  ''',
    '''
     +--------+
     | |
     O |
     | |
       |
       |
  _______________
  ''',
    '''
     +--------+
     | |
     O |
   --| |
       |
       |
  _______________
  ''',
    '''
     +--------+
     | |
     O |
   --| |--
       |
       |
  _______________
  ''',
    '''
     +--------+
     | |
     O |
   --| |--
    /  |
       |
  _______________
  ''',
    '''
     +--------+
     | |
     O |
   --| |--
    / \|
       |
  _______________
  '''
]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
