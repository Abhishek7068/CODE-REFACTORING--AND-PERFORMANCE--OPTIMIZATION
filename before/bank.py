# bank_account.py
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account(name={self.name}, balance={self.balance})"

def main():
    account = BankAccount("John Doe", 1000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)
    print(f"Final balance: {account.get_balance()}")

if __name__ == "__main__":
    main()