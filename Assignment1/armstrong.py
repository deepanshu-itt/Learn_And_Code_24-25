def isArmstrongNumber(userArmstrongNumber):
    sumOfDigitPowers = 0
    numberOfDigits = 0
    possibleArmstrongNumber = userArmstrongNumber

    while possibleArmstrongNumber > 0:
        numberOfDigits += 1
        possibleArmstrongNumber //= 10

    possibleArmstrongNumber = userArmstrongNumber
    for _ in range(numberOfDigits):
        lastDigit =possibleArmstrongNumber % 10
        sumOfDigitPowers += lastDigit ** numberOfDigits
        possibleArmstrongNumber //= 10

    return sumOfDigitPowers == userArmstrongNumber


userArmstrongNumber = int(input("\nPlease Enter the Number to Check for Armstrong: "))


if isArmstrongNumber(userArmstrongNumber):
    print("\n%d is an Armstrong Number.\n" % userArmstrongNumber)
else:
    print("\n%d is Not an Armstrong Number.\n" % userArmstrongNumber)