from random import *

MIN = int(input("Number between (minimum) : "))
MAX = int (input("Maximum ? : "))
number = randint(MIN,MAX)
guess_counter = -1

# Need cheat ?
#print(number)

while (guess_counter != number) :

        guess_counter = int(input(f"Please, find a number between {MIN} and {MAX}: "))

        if(guess_counter==number ):
            print(" Won ! the number was %s " % number)
            break
        elif(guess_counter >  number ):
            print("Smaller")
        else:
            print("Bigger")

        

