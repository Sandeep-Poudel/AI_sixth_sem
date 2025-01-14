class BankAccount:
    def __init__(self, accountNumber, balance=0):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount},new balance is {self.__balance}.")
        else:
            print("insufficient fund.")

    def get_balance(self):
        return self.__balance


    def get_accountNumber(self):
        return self.__accountNumber

# Example usage:
account = BankAccount("hanuman", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account balance: {account.get_balance()}")