class Account:
    def __init__(self, name, account_number, initial_balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

        if initial_balance > 0:
            self.transactions.append(f"Initial Deposit: +${initial_balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit Amount: +${amount:.2f}")
            return f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}"
        return "Invalid Deposit Amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: -${amount:.2f}")
            return f"Withdrawn: ${amount:.2f}. Remaining Balance: ${self.balance:.2f}."
        return "Insufficient Balance."
    
    def check_balance(self):
        return f"Current Balance: + ${self.balance:.2f}"

    def transaction_history(self):
        if not self.transaction_history:
            return "No Transactions Yet"
        return "\n".join(self.transactions)