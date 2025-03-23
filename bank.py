# bank.py
from account import Account, CheckingAccount, SavingsAccount

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, initial_balance=0.0, account_type="regular"):
        if account_number in self.accounts:
            return "Account number already exists. Please use a different number."
        
        # Validate account type
        if account_type not in ['regular', 'checking', 'savings']:
            return "Invalid account type. Please choose either 'regular', 'checking', or 'savings'."

        if account_type == 'checking':
            self.accounts[account_number] = CheckingAccount(name, account_number, initial_balance)
        elif account_type == 'savings':
            self.accounts[account_number] = SavingsAccount(name, account_number, initial_balance)
        else:
            self.accounts[account_number] = Account(name, account_number, initial_balance)

        return f"Account Created Successfully for {name} with Account Number: {account_number} and Account Type: {account_type}"
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def list_accounts(self):
        if not self.accounts:
            return "No accounts available."
        return "\n".join(
            [f"{acc.get_name()} - Account No: {acc.get_account_number()}" for acc in self.accounts.values()]
        )