import mysql.connector

class ATMDatabase:
    
    @staticmethod
    def get_atm_db_connection():
        return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="atm_db"
    )