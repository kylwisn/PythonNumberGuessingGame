import random

# Built using Python 3.10 & PyCharm
# This is random number generator guessing game
# The scope is that it will roll a random number between x to y
# and you have to guess it.
#
# Function to do the roll that will set the variable
# Function to enter your guess
# Function to check your guess against the roll and check if you guessed right.
# You can choose to try a new roll or not and if not the program will end
# A clearConsole command that will add blank lines to PyCharm to separate the guesses.

clearConsole = lambda: print('\n' * 150)

def number_generator():
    global numberGen
    numberGen = random.randint(1,5)
    user_input()

def user_input():
    global userGuess
    userGuess = input("Guess the number 1 to 5: ")
    print ("You guessed: " + str(userGuess))
    number_checker()

def number_checker():
    if int(userGuess) == int(numberGen):
        print("Good job you guessed it!")
        tryAgain()
    elif int(userGuess) < int(numberGen):
        print("Your guess was too low")
        tryAgain()
    elif int(userGuess) > int(numberGen):
        print("Your guess was too high")
        tryAgain()
    else:
        print("I don't understand your input...")
        tryAgain()

def tryAgain():
    userCommand = input("Do you want to try again? (Y/N): ")
    if str(str.lower(userCommand)) == "y":
        clearConsole()
        number_generator()
    elif str(str.lower(userCommand)) == "n":
        print("Goodbye!")
        quit()
    else:
        print("I don't understand your input...")
        clearConsole()
        tryAgain()

#This line starts the program
number_generator()
