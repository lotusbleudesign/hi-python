# use words.py as module
import random,words

word = random.choice(words.english_words)
chances = 7
again = True

while again :

    chanceCpt = chances
    display = ""

    # Need cheat ?
    #print(word)

    blanks = ['_'] * len(word)
    nbLetters = len(word)

    while chanceCpt > 0 : 
        print("Guess the word : ","".join(blanks))
        user_letter = input("Give a letter : ").lower()

        if user_letter in word:
            for i in range(len(word)):
                if (word[i] ==  user_letter):
                    blanks[i] = user_letter
        else:
            chanceCpt -= 1
            print("Try again , chance : ", chanceCpt)
            
        if not "_" in blanks :
            print(word.capitalize(), "You win ! " )
            break
        
        if chanceCpt == 0:
            choice = input("Lost .. Would you try again ? y or n ? ").lower()
            if choice == 'n':
                again = False
