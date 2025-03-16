from bank import Bank

bank = Bank()

def main():
    while True:
        print("\n=== Simple Bank Account System ===")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            name = input("Enter Your Name: ")
            account_number = input("Enter Your Account Number: ")
            initial_balance = float(input("Enter Your Initial Balance: "))
            print(bank.create_account(name, account_number, initial_balance))

        elif choice == "2":
            account_number = input("Enter Your Account Number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Deposit Amount: "))
                print(account.deposit(amount))
            else:
                print('Account Not Found!')

        elif choice == "3":
            account_number = input("Enter Your Account Number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Withdrawal Amount: "))
                print(account.withdraw(amount))
            else:
                print('Account Not Found!')

        elif choice == "4":
            account_number = input("Enter Your Account Number: ")
            account = bank.get_account(account_number)
            if account:
                print(account.check_balance())
            else:
                print('Account Not Found!')

        elif choice == "5":
            account_number = input("Enter Your Account Number: ")
            account = bank.get_account(account_number)
            if account:
                print("\n=== Transaction History ===")
                print(account.transaction_history())
            else:
                print('Account Not Found!')
            
        elif choice == "6":
            print("Exiting... Thank you for using our banking system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

