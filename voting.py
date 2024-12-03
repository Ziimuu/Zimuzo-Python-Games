

class voters:
    def __init__(self):
        self.name = input("What is your name: ")
        self.get_age()
        self.gender = input("What is your Gender? (Male/Female): ").capitalize()
        self.get_nationality()
        
    def get_age(self):
        while True:
            try:
                age = int(input("How old are you? " ))
                if age <= 17:
                    print("Not eligible to vote")
                    return
                elif age == 17:
                    print("come back next year.")
                    return
                else:
                    self.age = age
                    break
            except ValueError:
                print("Please enter a valid age.")
                
    def get_nationality(self):
        while True:
            nationality = input("What is your nationality? (Nationality): ")
            if nationality == "nigerian":
                self.nationality = nationality
                break
            else:
                 print(f"Sorry {self.name}, You are not eligible to vote, Only Nationality of Nigeria can vote")
                 return
                
            
    def voting(self):
        if hasattr(self, 'age') and hasattr(self, 'nationality'):
            print(f"Welcome {self.name}, You are eligible to vote")
            print("Thank you for your cooperation.")
        
            options = ["Peter Obi", "Asiwaju Bola Tinubu", "Abubakar Atiku", "Goodluck Jonathan", "Mohamadu Buhari"]
            
            print("Please vote one of the following candidates for Nigerian President by entering the corresponding number ")
            
            for i, options in enumerate(options, start=1):
                print(f"{i}.{options}")
                
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    if 1 <= choice <= len(options):
                        selected_name = options[choice-1]
                        print(f"You have voted for {selected_name}")
                        break
                    else:
                        print("Invalid choice, Please try again.")
                except ValueError:
                    print("Invalid choice, Please enter a valid number.")
        else: 
            print("You are not eligible to vote")
            
voter = voters()
voter.voting()
    
    
