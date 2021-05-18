import random


def guessing():
    # Getting in inputs from user for the maxmimum number that the cumputer will generate to... and the maximum
    # attempts that the player has
    max_nbr = int(input("what will be the maximum number for guessing ? >"))
    trys = int(input("What would be the maximum attemps that you'll have to guess the number ? >"))
    # Generating the random number
    random_nbr = random.randint(0, max_nbr)
    print("The cumputer generated a number between 0 and " + str(max_nbr) + "\
    \ntry to guess that number , you have " + str(trys) + " chances")
    guess = 0
    # Verifying if the guess is correct
    while guess != random_nbr:
        if trys == 0:
            print("You've lost")
            break
        guess = int(input("Enter you're guess >"))
        if guess == random_nbr:
            print("You succefuly guessed the number")
            break
        else:
            print("You answer is false")
            trys = trys - 1


guessing()
print("press any key to exit")
input()
# Made by Omar Sarsar
