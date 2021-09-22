from random import *

number = randint(1,100)
guess_counter = -1

# Need cheat ?
# print(number)

while (guess_counter != number) :
    
    guess_counter = int(input("Please, find a number between 0 and 100: "))

    if(guess_counter >  number ):
        print("Smaller")
    else:
        print("Bigger")
        
    if(guess_counter==number ):
        print(" Won ! the number was %s " % number)