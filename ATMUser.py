from database import ATMDatabase
from ATM import ATM
from custom_erros_classes import (
    ATMException
)


class ATMUser:

    @staticmethod
    def update_user_balance(user_id, new_balance):
            conn = ATMDatabase.get_atm_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET balance = %s WHERE user_id = %s", (new_balance, user_id))
            conn.commit()
            conn.close()


    @staticmethod
    def process_withdrawal(user_bank_atm: ATM, user: dict):
        amount_to_withdraw = float(input("Enter amount to withdraw: "))
        updated_balance = user_bank_atm.withdraw(amount_to_withdraw, user['balance'])
        ATMUser.update_user_balance(user['user_id'], updated_balance)
        print(f"Account balance: ${updated_balance}")
        return updated_balance


    @staticmethod
    def process_deposit(user_bank_atm: ATM, user: dict):
        amount_to_deposit = float(input("Enter amount to deposit: "))
        updated_balance = user_bank_atm.deposit(amount_to_deposit, user['balance'])
        ATMUser.update_user_balance(user['user_id'], updated_balance)
        print(f"Account balance: ${updated_balance}")
        return updated_balance


    @staticmethod
    def handle_process_withdrawal(user_bank_atm: ATM, user: dict):
        updated_balance = user['balance']
        try:
            updated_balance = ATMUser.process_withdrawal(user_bank_atm, user)
        except ATMException as error:
            print(f"ATM ERROR: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")
        return updated_balance


    @staticmethod
    def get_user_card():
        user = None
        card_number = input("Enter your Card Number: ").strip()
        user = ATMUser.fetch_user_data_by_card(card_number)
        if not user:
            print("Card not found.")
        return user


    @staticmethod
    def fetch_user_data_by_card(card_number):
            db_connection =  ATMDatabase.get_atm_db_connection()
            cursor = db_connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE card_number = %s", (card_number,))
            user = cursor.fetchone()
            db_connection.close()
            return user