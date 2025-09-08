from BankAccount import BankAccount
import time

valid_users = {
    "jeremy": BankAccount(1000),
    "john": BankAccount(5000),
    "jamal": BankAccount(10000),
    }


def validate_account():
    while True:
        sign_in = input("Enter your name: ").strip().lower()

        if sign_in in valid_users:
            valid_users[sign_in].check_balance()
            break
        elif sign_in not in valid_users:
            print("Not a valid user")
            for sec in range(3, 0, -1):
                print(f"Creating '{sign_in}' account. Please wait {sec} seconds...")
                time.sleep(0.5)
            valid_users[sign_in] = BankAccount(0)
        elif not sign_in:
            print("Entry cannot be empty")
        else:
            print("Invalid")

    return sign_in


def options(sign_in):
    while True:
        option = (
            "1. Deposit",
            "2. Withdraw",
            "3. Exit",
            )

        for line in option:
            print(line)
            time.sleep(0.2)

        try:
            option = int(input("> "))
            if option == 1:
                valid_users[sign_in].deposit(int(input("Enter your amount: ")))
            elif option == 2:
                valid_users[sign_in].withdraw(int(input("Enter your amount: ")))
            elif option == 3:
                for sec in range(3, 0, -1):
                    print(f"Exiting in {sec}...")
                    time.sleep(0.2)
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")


def main():
    sign_in = validate_account()
    options(sign_in)


main()
