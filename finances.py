class PersonalFinanceApp:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        self.display_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
            self.display_balance()
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Current balance:", self.balance)


def main():
    finance_app = PersonalFinanceApp()

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            finance_app.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            finance_app.withdraw(amount)
        elif choice == "3":
            finance_app.display_balance()
        elif choice == "4":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
