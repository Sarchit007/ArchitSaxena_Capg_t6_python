# units = int(input("Enter units consumed: "))

# bill = 0

# if units <= 100:
#     bill = units * 5

# elif units <= 300:
#     bill = (100 * 5) + (units - 100) * 7

# else:
#     bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# print("Total Bill Amount:", bill)



# Small bank management system:-

class Bank:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def display_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient balance.")

# Example usage:
if __name__ == "__main__":
    account = Bank(100)  # Start with 100
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()  


