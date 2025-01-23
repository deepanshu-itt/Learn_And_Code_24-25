def isArmstrongNumber(userInputArmstrongNumber):
    sumOfDigitPowers = 0
    numberOfDigits = 0
    possibleArmstrongNumber = userInputArmstrongNumber

    while possibleArmstrongNumber > 0:
        numberOfDigits += 1
        possibleArmstrongNumber //= 10

    possibleArmstrongNumber =userInputArmstrongNumber
    for _ in range(numberOfDigits):
        lastDigit =possibleArmstrongNumber % 10
        sumOfDigitPowers += lastDigit ** numberOfDigits
        possibleArmstrongNumber //= 10

    return sumOfDigitPowers == userInputArmstrongNumber


userInputArmstrongNumber = int(input("\nPlease Enter the Number to Check for Armstrong: "))


if isArmstrongNumber(userInputArmstrongNumber):
    print("\n%d is an Armstrong Number.\n" % userInputArmstrongNumber)
else:
    print("\n%d is Not an Armstrong Number.\n" % userInputArmstrongNumber)