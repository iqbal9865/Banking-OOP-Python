from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, initial_balance = 0.0):
        if account_number in self.accounts:
            return "Account number already exists. Please use a different number."

        self.accounts[account_number] = Account(name, account_number, initial_balance)
        return f"Account Created Successfully for {name} with Account Number: {account_number}"
    
    def get_account(self, account_number):
        account_number = str(account_number)  
        return self.accounts.get(account_number, None)
