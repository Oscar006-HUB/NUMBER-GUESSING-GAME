import random

def guessing_Game():
    # SETTING UP PARAMETERS
    target_number = random.randint(1,100)
    max_attempts = 7
    attempts_taken = 0 
    
    print("---Welcome to the Number Guessing Game Challange!---")
    print(f"I'm thinking of a number between 1 an 100.You have {max_attempts} chances. ")
    
    # Logic of Game
    while attempts_taken < max_attempts:
        try:  
            # Take user input an increment attempt counter
            Guess =int(input(f"\n Attempt {attempts_taken +1}:Enter Your Guess Please:"))
            attempts_taken +=1
            
            if Guess < target_number:
                print("Too Low ! Please Try A Higher Number .")
            elif Guess > target_number:
                print("Too High Please Try A Lower Number.")
            else:
                print(f"🪶Congratulations!🪶 You have Have Guessed it in {attempts_taken}attempts.")
                return  # Exiting the function When guess is correct   
    
    # Feedback on Number Of Chances Left 
            remaining = max_attempts - attempts_taken
            if remaining >0:
                print(f"Remaining attempts:{remaining}")
        except ValueError:
            print("Invalid Input\n.Please Enter A whole Number.")
    # When the loop ends without a return ,the user lost
    print(f"\n Game Over! You Have Run Out of Chances.The Number was {target_number}.")
if __name__ == "__main__":
    guessing_Game()       