'''
secret_number = 5
print("I am thinking of a number between 1 and 10.")
while True:
    userinp = int(input ("Guess a number? "))
    if userinp == secret_number:
        print("you win")
        break
    else:
        print("Nope, try again.") 

secret_number = 5
print("I am thinking of a number between 1 and 10.")
while True:
    userinp = int(input ("Guess a number? "))
    if userinp == secret_number:
        print("you win")
        break
    elif userinp < 5:
        print("A little higher")
    elif userinp > 5: 
        print("A little lower")    

import random
secret_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
while True:
    userinp = int(input ("Guess a number? "))
    if userinp == secret_number:
        print("you win")
        break
    elif userinp < secret_number:
        print("A little higher")
    elif userinp > secret_number: 
        print("A little lower")
    else:
        print("Nope, try again")
'''
import random
secret_number = random.randint(1, 10)
max_guesses = 0
play_again = 'y'
while play_again == 'y':

    print("I am thinking of a number between 1 and 10.")
    while True:
        guess_left = 5 - max_guesses
        print("you have {} guess left".format(guess_left))
        max_guesses = max_guesses + 1
        if max_guesses == 5:
            print("you are out of guesses")
            break
        userinp = int(input ("Guess a number? "))
        if userinp == secret_number:
            print("you win")
            break
        elif userinp < secret_number:
            print("A little higher")
        elif userinp > secret_number: 
            print("A little lower")
        else:
            print("Nope, try again")
    while True:
        userask = input("Do you want to play again? y or n?")
        if userask != "y" and userask != "n":
            print("That is not an input")
        else:
            break
        