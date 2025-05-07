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
            raise ATMCardBlockedException("Card is blocked Because of 3 invalid attempts.")
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


def initialize_atm():
    user_bank_atm = ATM(atm_cash=10000, daily_limit=2000)
    user_account = 20000
    correct_pin = "1234"
    return user_bank_atm, user_account, correct_pin


def is_pin_verified(atm: ATM, correct_pin: str):
    pin_verified = False
    while not pin_verified:
        try:
            user_pin = input("Enter your PIN: ")
            atm.verify_pin(user_pin, correct_pin)
            pin_verified = True
        except ValueError as error:
            print(f"ERROR: {error} - Try again.")
        except ATMCardBlockedException as error:
            print(f"ERROR: {error}")
            break
    return pin_verified


def handle_process_withdrawal(user_bank_atm: ATM, user_account: float):
    updated_balance = user_account
    try:
        updated_balance = process_withdrawal(user_bank_atm, user_account)
    except ATMException as error:
        print(f"ATM ERROR: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")
    return updated_balance


def process_withdrawal(user_bank_atm: ATM, user_account: float):
    amount_to_withdraw = float(input("Enter amount to withdraw: "))
    updated_balance = user_bank_atm.withdraw(amount_to_withdraw, user_account)
    print(f"Account balance: ${updated_balance}")
    return updated_balance


def main():
    user_bank_atm, user_account, correct_pin = initialize_atm()
    pin_verified = is_pin_verified(user_bank_atm, correct_pin)

    if not pin_verified:
        return

    continue_session = True
    while continue_session:
        user_account = handle_process_withdrawal(user_bank_atm, user_account)
        user_input = input("Do you want to continue? (yes/no): ").strip().lower()
        continue_session = user_input == 'yes'


if __name__ == "__main__":
    main()
