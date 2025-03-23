# account.py
class Account:
    def __init__(self, name, account_number, initial_balance=0.0):
        self.__name = name
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transactions = []

        if initial_balance > 0:
            self.__transactions.append(f"Initial Deposit: +${initial_balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit: +${amount:.2f}")
            return f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawn: -${amount:.2f}")
            return f"Withdrawn ${amount:.2f}. Remaining Balance: ${self.__balance:.2f}"
        return "Insufficient funds or invalid amount."

    def check_balance(self):
        return f"Current Balance: ${self.__balance:.2f}"

    def get_transaction_history(self):
        if not self.__transactions:
            return "No transactions yet."
        return "\n".join(self.__transactions)

    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

class CheckingAccount(Account):
    def __init__(self, name, account_number, initial_balance=0.0):
        super().__init__(name, account_number, initial_balance)

class SavingsAccount(Account):
    def __init__(self, name, account_number, initial_balance=0.0, interest_rate=0.02):
        super().__init__(name, account_number, initial_balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self._Account__balance * self.__interest_rate
        self._Account__balance += interest
        self._Account__transactions.append(f"Interest Added: +${interest:.2f}")
        return f"Interest of ${interest:.2f} added. New Balance: ${self._Account__balance:.2f}"