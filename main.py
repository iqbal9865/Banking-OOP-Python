# main.py
from bank import Bank

bank = Bank()

def main():
    while True:
        print("\n=== Simple Bank System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. List All Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Your Name: ")
            account_number = input("Enter Account Number: ")

            # Ensure the initial balance is a valid float
            while True:
                try:
                    initial_balance = float(input("Enter Initial Deposit: "))
                    if initial_balance < 0:
                        print("Initial deposit cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number for the initial deposit.")
            
            account_type = input("Enter Account Type (regular/checking/savings): ").lower()
            print(bank.create_account(name, account_number, initial_balance, account_type))

        elif choice == "2":
            account_number = input("Enter Account Number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Deposit Amount: "))
                print(account.deposit(amount))
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter Account Number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Withdrawal Amount: "))
                print(account.withdraw(amount))
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter Account Number: ")
            account = bank.get_account(account_number)
            if account:
                print(account.check_balance())
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = input("Enter Account Number: ")
            account = bank.get_account(account_number)
            if account:
                print("\n=== Transaction History ===")
                print(account.get_transaction_history())
            else:
                print("Account not found.")

        elif choice == "6":
            print("\n=== List of Accounts ===")
            print(bank.list_accounts())

        elif choice == "7":
            print("Exiting... Thank you for using our banking system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()