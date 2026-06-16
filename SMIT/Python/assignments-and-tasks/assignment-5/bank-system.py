class BankAccount:

    def __init__(self, holder_name, account_number, balance, account_type):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")

    def display_account(self):
        print("\n---------------------------")
        print(f"Holder Name   : {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type  : {self.account_type}")
        print(f"Balance       : Rs.{self.balance}")
        print("---------------------------")


# List to store all accounts
accounts = []


def create_account():
    name = input("Enter Account Holder Name: ")
    acc_no = input("Enter Account Number: ")
    balance = float(input("Enter Initial Balance: "))
    acc_type = input("Enter Account Type (Saving/Current/Student): ")

    # Create object
    account = BankAccount(name, acc_no, balance, acc_type)
    # Store object in accounts list
    accounts.append(account)

    print("Account Created Successfully!")


def find_account(acc_no):
    # Search account in accounts list
    for account in accounts:
        if account.account_number == acc_no:
            return account
    # Return None if not found
    return None


def deposit_money():
    acc_no = input("Enter Account Number: ")

    # Find account
    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)
    else:
        print("Account not found.")


def withdraw_money():
    acc_no = input("Enter Account Number: ")

    # Find account
    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Withdrawal Amount: "))
        account.withdraw(amount)
    else:
        print("Account not found.")


def check_account_balance():
    acc_no = input("Enter Account Number: ")

    # Find account
    account = find_account(acc_no)

    if account:
        account.check_balance()
    else:
        print("Account not found.")


def display_all_accounts():

    if not accounts:
        print("No accounts found.")
        return

    # Loop through accounts
    for account in accounts:
        account.display_account()


# Main Menu
while True:

    print("\n===== Mini Banking System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        check_account_balance()

    elif choice == "5":
        display_all_accounts()

    elif choice == "6":
        print("Thank you for using the Banking System.")
        break
    else:
        print("Invalid choice. Try again.")