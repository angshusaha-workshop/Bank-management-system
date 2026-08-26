from bank import Bank


bank = Bank()


while True:

    print("\n========== Bank Management System ==========")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        bank.create_account()

    elif choice == "2":

        bank.login()

    elif choice == "3":

        print("Thank you for using our Bank Management System.")
        break

    else:

        print("Invalid Choice!")