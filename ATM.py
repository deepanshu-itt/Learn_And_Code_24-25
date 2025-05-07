from custom_erros_classes import (
    ATMCardBlockedException, ATMDailyLimitExceededException,
    ATMException, ATMOutOfCashException, ATMServerConnectionError,
    InsufficientMoneyException
)


class ATM:
    def __init__(self, atm_cash: float, daily_limit: float):
        self.atm_cash = atm_cash
        self.daily_limit = daily_limit
        self.server_connected = True
        self.pin_attempts = 0
        self.max_pin_attempts = 3
        self.withdrawn_today = 0

    def verify_pin(self, pin: str, correct_pin: str):
        if self.pin_attempts == self.max_pin_attempts:
            raise ATMCardBlockedException("Card is blocked because of 3 invalid attempts.")
        if pin != correct_pin:
            self.pin_attempts += 1
            raise ValueError("Invalid PIN.")
        self.pin_attempts = 0

    def connect_to_server(self):
        if not self.server_connected:
            raise ATMServerConnectionError("Unable to connect with the server.")

    def withdraw(self, amount: float, account_balance: float):
        self.connect_to_server()
        if amount > self.atm_cash:
            raise ATMOutOfCashException("Insufficient cash available in ATM.")
        if amount > account_balance:
            raise InsufficientMoneyException("Insufficient funds in account.")
        if self.withdrawn_today + amount > self.daily_limit:
            raise ATMDailyLimitExceededException("Daily withdrawal limit exceeded.")
        self.atm_cash -= amount
        self.withdrawn_today += amount
        account_balance -= amount
        print(f"Withdrawal successful: ${amount}")
        return account_balance

    def deposit(self, amount: float, account_balance: float):
        self.connect_to_server()
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account_balance += amount
        print(f"Deposit successful: ${amount}")
        return account_balance