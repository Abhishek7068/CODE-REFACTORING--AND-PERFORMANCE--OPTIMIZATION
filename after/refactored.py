# bank_account_refactored.py
import logging

class BankAccount:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = balance
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        logging.info(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            logging.warning("Insufficient funds!")
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        logging.info(f"Withdrew {amount}. New balance: {self._balance}")

    def __str__(self):
        return f"Account(name={self._name}, balance={self._balance})"

def main():
    try:
        account = BankAccount("John Doe", 1000)
        print(account)
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(2000)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print(f"Final balance: {account.balance}")

if __name__ == "__main__":
    main()