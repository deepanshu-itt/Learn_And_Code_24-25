from custom_erros_classes import (
    ATMCardBlockedException
)
from ATM import ATM
from ATMUser import ATMUser


def atm_application_start():
    user = ATMUser.get_user_card()

    bank_atm = ATM(atm_cash=10000, daily_limit=2000)

    if not is_pin_verified(bank_atm, user['pin']):
        return

    continue_session = True
    
    while continue_session:
        print_menu()
        choice = input("Enter choice (1/2/3): ").strip()
        continue_session = execute_choice(choice, user, bank_atm)


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


def print_menu():
    print("\nSelect an option:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Exit")



def execute_choice(choice, user, bank_atm):
    continue_session = True
    
    if choice == '1':
        user['balance'] = ATMUser.handle_process_withdrawal(bank_atm, user)
    elif choice == '2':
        user['balance'] = ATMUser.process_deposit(bank_atm, user)
    elif choice == '3':
        print("Session ended.")
        continue_session = False
    else:
        print("Invalid choice. Try again.")
        
    return continue_session


def main():
    atm_application_start()
        

if __name__ == "__main__":
    main()
