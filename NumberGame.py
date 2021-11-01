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

# Using this in PyCharm it will add blank lines as a way to clear the console screen when playing the game
clearConsole = lambda: print('\n' * 150)

# Sets variable NumberGen to equal a random number between x and y
# Then loads the user input function
def number_generator():
    global numberGen
    numberGen = random.randint(1,5)
    user_input()

# Sets variable userGuess to equal the user's input of what they are guessing the number to be
# Then loads the number checking function
def user_input():
    global userGuess
    userGuess = input("Guess the number 1 to 5: ")
    print ("You guessed: " + str(userGuess))
    number_checker()

# Checks the user's guess against the generated random number and tells you if you are correct, high, or low.
# If your input is incorrect, it will say it didn't understand your input.
# Then you will be prompted if you want to try again.
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

# Function to ask the user if they want to try again.
# An incorrect user input here will repeat the function
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
