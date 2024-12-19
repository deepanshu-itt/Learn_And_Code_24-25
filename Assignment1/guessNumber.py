import random

def is_valid_input(userGuessNumber):
    if userGuessNumber.isdigit() and 1 <= int(userGuessNumber) <= 100:
        return True
    else:
        return False

def main():
    numbeToBeGuess = random.randint(1, 100)  
    guessed_correctly = False  
    totalUserGuess = 0  

    while not guessed_correctly:
        userGuessNumber = input("Guess a number between 1 and 100: ")  # Prompt user for a guess

        if not is_valid_input(userGuessNumber):  
            print("I won't count this one. Please enter a number between 1 to 100.")
            continue  

        totalUserGuess += 1  
        userGuessNumber = int( userGuessNumber)  

        if  userGuessNumber < numbeToBeGuess:
            print("Too Low. Guess again.")  
        elif  userGuessNumber > numbeToBeGuess:
            print("Too High. Guess again.")  
        else:
            print("You guessed it in", totalUserGuess, "guesses!")  
            guessed_correctly = True  

if __name__ == "__main__":
    main()  