import random

# Choice
ROCK = 0
PAPER = 1
SCISSORS = 2

# Play again
while True:
    
    choice = [ROCK,PAPER,SCISSORS]
    
    # Gamers
    user = int(input("Make your choice : Rock[0], Paper[1] or Scissors[2] ? "))
    computer = random.choice(choice)

    print(f"You chose {user}, computer chose {computer}")
    
    if( user <= 2 ):
        if user == computer:
            print("Tie ! Try again")
        elif user == ROCK:
            if computer == PAPER:
                print("You lost.. Computer use %s " % PAPER)
            else:
                print("You win ! Computer use %s n" % SCISSORS)       
        elif user == PAPER:
            if computer == ROCK:
                print("You win ! Computer use %s " % ROCK)
            else:
                print("You lost .. Computer use %s " % SCISSORS) 
        elif user == SCISSORS:
            if computer == PAPER:
                print("You win ! Computer use %s " % PAPER)
            else:
                print("You lost .. Computer use %s " % ROCK)
    else:
        print("Choice doesn't exist !")  
               
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        break

