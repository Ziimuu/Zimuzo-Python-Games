import random
import sys

def guess_number(name = "Zimu"):
    player_wins = 0
    game_count = 0
    
    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        
        player_choice = input(f"\n\n {name}, guess which number I'm thinking of... 1, 2, or 3.\n\n ")
        if player_choice not in["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2 or 3.")
            return play_guess_number()
        
        computer_choice = random.choice("1,2,3")
        
        print(f"\n{name}, you choose{player_choice}.")
        print(f"I was thinking about the number {computer_choice}.\n")
        
        player = int(player_choice)
        computer = int(computer_choice)
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
        
            if player == computer:
                player_wins += 1
                return f"\n{name}, you win!🎉🥳"
            else:
                return f"\nSorry, {name}, Better luck next time😥😥"
            
        game_result = decide_winner(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame Count: {game_count}")
        print(f"\nPlayer Wins: {player_wins}")
        print(f"\nYour Winning Percentage:{player_wins/game_count:.2%}")
        
        print(f"\n{name}, Play again?")
        
        while True:
            playagain = input("\nY for Yes or \nQ for Quit.\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
                return play_guess_number()
        else:
                print("\n🎉🥳🎉🥳🎉🥳\nThanks for playing")
                
                if __name__ =="__main__":
                    sys.exit(f"\nBye {name}!👋")
                else:
                    return
                
    return play_guess_number

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides personalized game experience"
    )
    
    parser.add_argument(
        "-n", "--name", metavar="name", 
        required=True, help="Name of the persoon playing the game"
    )
    
    args = parser.parse_args()
    
    guess_number_game = guess_number(args.name)
    guess_number_game()
            
        