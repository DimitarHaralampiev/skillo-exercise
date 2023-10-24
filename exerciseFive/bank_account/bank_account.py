# Define a class named BankAccount to represent a simple bank account.

class BankAccount:
    # Initialize the BankAccount with a bank account name and an initial balance.
    def __init__(self, bank_account, balance):
        self.__bank_account = bank_account  # Private attribute to store the bank account name
        self.__balance = balance  # Private attribute to store the account balance

    # Getter property for retrieving the bank account name.
    @property
    def bank_account(self):
        return self.__bank_account

    # Getter property for retrieving the account balance.
    @property
    def balance(self):
        return self.__balance

    # Setter property for setting the account balance, with validation to ensure non-negativity.
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Invalid balance. Please enter a non-negative value.')
        self.__balance = value

    # Method to deposit money into the account, updating the balance.
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Invalid amount. Please enter a positive value.')
        self.balance += amount  # Calls the setter property to update the balance
        return self.balance

    # Method to withdraw money from the account, with checks for negative amount and insufficient funds.
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError ('Invalid withdrawal amount. Please enter a positive value.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')
        self.balance -= amount  # Calls the setter property to update the balance
        return f'Withdrew {amount}lv. New balance: {self.balance:.2f}lv.'

    # Custom string representation for the BankAccount.
    def __str__(self):
        return f'Account holder: {self.bank_account}, Balance: {self.balance:.2f}lv.'


# Create an instance of the BankAccount class with an initial balance.
account = BankAccount("Ivan Ivanov", 1000.0)

# Perform operations on the account, including deposits and withdrawals.
print(account.deposit(500))
print(account.withdraw(300))
print(account.withdraw(1500))

# Change the balance directly using the setter property.
account.balance = 3500
account.balance = -300
print(account.deposit(500))
print(account.withdraw(300))
print(account.withdraw(1500))
