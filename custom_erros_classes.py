class ATMException(Exception):
    pass

class InsufficientMoneyException(ATMException):
    pass

class ATMOutOfCashException(ATMException):
    pass

class ATMServerConnectionError(ATMException):
    pass

class ATMCardBlockedException(ATMException):
    pass

class ATMDailyLimitExceededException(ATMException):
    pass