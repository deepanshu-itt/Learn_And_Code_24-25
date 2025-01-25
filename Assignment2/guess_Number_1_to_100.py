import random

def guessNumberGame():
    gameConstants = getgameConstants()
    random_Genratednumber = generateRandomNumber(gameConstants["min_Value"], gameConstants["max_Value"])    
    numberOfUserGusses = is_Guess_Correctly(random_Genratednumber)
    print_Success_Message(numberOfUserGusses)

def getgameConstants():
    return {
        "min_Value": 1,
        "max_Value": 100,
        "low_Guess_Prompt": "Too low. Guess again.",
        "high_Guess_Prompt": "Too high. Guess again.",
        "userInput_Prompt_Message": "Guess a number between 1 and 100: ",
        "invalid_userInput_Message": "Invalid input. Please enter a number between 1 and 100.",
    }

def generateRandomNumber(minValue, maxValue):
    return random.randint(minValue, maxValue)

def getUserInput(prompt_Message):
    userInputNumber = input(prompt_Message)
    return userInputNumber

def isValidUserInput(userInputNumber):
    gameConstants = getgameConstants()
    is_Valid_Input = False
    if userInputNumber.isdigit() and gameConstants["min_Value"] <= int(userInputNumber) and int(userInputNumber) <= gameConstants["max_Value"]:
         is_Valid_Input = True
    return is_Valid_Input

def print_Success_Message(numberOfUserGusses):
    print("You guessed it in", numberOfUserGusses, "guesses!")

def getValidUserInput(numberOfUserGusses):
    gameConstants = getgameConstants()
    is_valid_user_input = False
    while not is_valid_user_input:
        userInputNumber = getUserInput(gameConstants["userInput_Prompt_Message"])
        if not isValidUserInput(userInputNumber):
            userInputNumber = getUserInput(gameConstants["invalid_userInput_Message"])
        else:
            numberOfUserGusses += 1  
            is_valid_user_input = True

    return int(userInputNumber), numberOfUserGusses

def isUserInputNearRandomNumber(random_Genratednumber, userInputNumber, numberOfUserGusses):
    is_User_Guessed_Correctly = False
    gameConstants = getgameConstants()
    if userInputNumber < random_Genratednumber:
        print(gameConstants["low_Guess_Prompt"])
    elif userInputNumber > random_Genratednumber:
        print(gameConstants["high_Guess_Prompt"])  
    else:
        is_User_Guessed_Correctly = True  

    return is_User_Guessed_Correctly, userInputNumber, numberOfUserGusses

def is_Guess_Correctly(random_Genratednumber):
    numberOfUserGusses = 0
    is_User_Guessed_Correctly = False
    while not is_User_Guessed_Correctly:
        userInputNumber, numberOfUserGusses = getValidUserInput(numberOfUserGusses)
        is_User_Guessed_Correctly, userInputNumber, numberOfUserGusses = isUserInputNearRandomNumber(random_Genratednumber, userInputNumber, numberOfUserGusses)

    return numberOfUserGusses


def main():
    guessNumberGame()

main()
