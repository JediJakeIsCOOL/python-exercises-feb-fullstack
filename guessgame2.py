print("I will try to guess your number 1 to 100")
compguess = 50
guesses = 0
print("is your number" , compguess)
while True:
    userinp =input("Is the answer higher,lower, or correct?")
    if userinp == "higher":
        compguess = compguess + 1
        guesses = guesses + 1
        print("Is it" ,compguess)
    elif userinp == "lower":
        compguess = compguess - 1
        guesses = guesses + 1
        print("is it", compguess)
    elif userinp ==  "correct":
        guesses = guesses + 1
        print("I got it")
        break
print("It took" ,guesses, "tries to find your number!")

