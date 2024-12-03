import sys
import random
from enum import Enum

def rps(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0
   
    
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
             Rock = 1
             Paper = 2
             Scissors = 3 

        playerchoice = input(f"\n {name}, Enter...\n1 for ROCK🪨\n2 for PAPER📃 or\n3 for SCISSORS✂️\n\n")

        # if playerchoice < 1 or playerchoice > 3:
        #     sys.exit("Kindly Enter 1, 2 or 3") 
        
        if playerchoice not in ["1", "2", "3"]:
            print(f" {name}, Please enter 1, 2 or 3")
            return play_rps()  
            
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose " + str(RPS(player)).replace("RPS.","."))
        print(f"Python chose " + str(RPS(computer)).replace("RPS.",".\n"))
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            
            if player == 1 and computer ==3:
                player_wins +=1
                return f"{name}, you Win!🥳🥳"
            
            elif player == 2 and computer ==1:
                player_wins +=1
                return f"{name}, you Win!🥳🥳"
            
            elif player == 2 and computer ==2:
                player_wins +=1
                return f"{name}, you Win!🥳🥳"
            
            elif player == computer:
                return "Tie Game!😲"
            
            else:
                python_wins +=1
                return f"Python Wins!🐍🐍\n Sorry, {name} 😥"                
            
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\n Game Count: {game_count}")
        print(f"\n {name}'s Wins: {player_wins}")
        print(f"\n Python Wins: {python_wins}")
            
    
        print(f"\nPlay Again, {name}?")
        
        while True:
           playagain = input ("\n Y for Yes or \n Q for Quit\n")
           if playagain.lower() =="Y":
               continue
           else:
               break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thanks for playing")
                 
            if __name__ =="__main__":
                    sys.exit(f"\nBye {name}!👋")
            else:
                    return
                
    return play_rps

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a Personalized Game Experience."
    )
    
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the Game."
    )
    
    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
        
 