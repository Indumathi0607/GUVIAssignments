# Base class BankAccount
class BankAccount:

    # Used encapsulation to keep the balance attribute private
    def __init__(self, account_number, balance):
        self.account_number = account_number  # public variable
        self.__balance = balance  # private variable

    # Method to return balance after deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} and current balance is: {self.__balance}")
            return self.__balance
        else:
            print("Deposit amount should be positive value")

    # Method to return balance after withdraw
    def withdraw(self, amount):
        if self.__balance > 0 and self.__balance - amount > 0:
            self.__balance -= amount
            print(f"New balance after withdraw: {self.__balance}")
            return self.__balance
        else:
            print(f"Withdraw amount {amount} exceeds current balance {self.__balance}")

    # Method to access private attribute 'balance' outside the base class
    def get_balance(self):
        return self.__balance


# SavingsAccount sub class inherited from BankAccount base class
class SavingsAccount(BankAccount):

    def __init__(self, acc_number, balance, interest_rate):
        super().__init__(acc_number, balance)  # inheriting the attributes from base class using super
        self.interest_rate = interest_rate

    def calc_interest(self, years):
        interest = (self.get_balance() * years * self.interest_rate) / 100
        print(f'Calculated interest is {interest}')
        return interest


# CurrentAccount sub class inherited from BankAccount base class
class CurrentAccount(BankAccount):
    def __init__(self, acc_number, balance, minimum_balance):
        super().__init__(acc_number, balance)  # inheriting the attributes from base class using super
        self.min_balance = minimum_balance

    def withdraw(self, amount):
        if amount < 0:
            print(f"Withdraw amount is negative {amount}")
        elif self.get_balance() - amount > self.min_balance:
            super().withdraw(amount)
        else:
            print(f"Withdraw amount {amount} exceeds min balance {self.min_balance}")


# creating object for SavingsAccount and accessing self and base class methods
saving_account = SavingsAccount("S_7284712", 20000, 8)
saving_account.deposit(10000)
saving_account.withdraw(5000)
saving_account.calc_interest(2)
saving_account.withdraw(30000)

# creating object for CurrentAccount and accessing self and base class methods
current_account = CurrentAccount("C_123123", 50000, 20000)
current_account.deposit(2000)
current_account.withdraw(10000)
current_account.withdraw(35000)
current_account.withdraw(-40000)
current_account.withdraw(40000)
