import json
import random

from account import Account


class Bank:

    def __init__(self):
        print("===== Bank System Started =====")

    def load_accounts(self):
        try:
            with open("database.json", "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_accounts(self, accounts):
        with open("database.json", "w") as file:
            json.dump(accounts, file, indent=4)

    def generate_account_number(self, accounts):
        while True:
            account_number = str(random.randint(100000, 999999))

            if account_number not in accounts:
                return account_number

    def create_account(self):

        print("\n===== Create Account =====")

        name = input("Enter your name: ")
        password = input("Enter your password: ")

        accounts = self.load_accounts()

        account_number = self.generate_account_number(accounts)

        account = Account(
            account_number,
            name,
            password
        )

        accounts[account_number] = account.to_dict()

        self.save_accounts(accounts)

        print("\nAccount Created Successfully!")
        print(f"Your Account Number: {account_number}")

    def login(self):

        print("\n===== Login =====")

        account_number = input("Enter Account Number: ")
        password = input("Enter Password: ")

        accounts = self.load_accounts()

        if not accounts:
            print("No accounts found.")
            return

        if (
            account_number in accounts
            and accounts[account_number]["password"] == password
        ):

            print(
                f"\nWelcome {accounts[account_number]['name']}!"
            )

            self.account_menu(account_number, accounts)

        else:
            print("Invalid Account Number or Password.")

    def account_menu(self, account_number, accounts):

        while True:

            print("\n===== Account Menu =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Account Information")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":

                balance = accounts[account_number]["balance"]

                print(f"Current Balance: {balance} Tk")

            elif choice == "2":

                amount = float(
                    input("Enter deposit amount: ")
                )

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                accounts[account_number]["balance"] += amount

                self.save_accounts(accounts)

                print("Deposit Successful!")

            elif choice == "3":

                amount = float(
                    input("Enter withdraw amount: ")
                )

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                balance = accounts[account_number]["balance"]

                if amount <= balance:

                    accounts[account_number]["balance"] -= amount

                    self.save_accounts(accounts)

                    print("Withdraw Successful!")

                else:
                    print("Insufficient Balance!")

            elif choice == "4":

                account = Account(
                    account_number,
                    accounts[account_number]["name"],
                    accounts[account_number]["password"],
                    accounts[account_number]["balance"]
                )

                account.display_account_info()

            elif choice == "5":

                print("Logged Out Successfully.")
                break

            else:
                print("Invalid Choice.")