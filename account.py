class Account:
    def __init__(self, account_number, name, password, balance=0):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance

    def display_account_info(self):
        print("\n===== Account Information =====")
        print(f"Account Number : {self.account_number}")
        print(f"Name           : {self.name}")
        print(f"Balance        : {self.balance} Tk")

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "balance": self.balance
        }