import threading

class BankAccount(object):
    ThreadLock = threading.Lock()
    
    def __init__(self):
        self.money_on_account = 0
        self.is_account_open = False

    def get_balance(self):
        self.error_if_closed()
        return self.money_on_account

    def open(self):
        self.error_if_opened()
        self.is_account_open = True
    
    def deposit(self, amount):
        with BankAccount.ThreadLock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Cannot deposit negative money")
            else:
                self.money_on_account += amount

    def withdraw(self, amount):
        with BankAccount.ThreadLock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Cannot withdraw negative money")
            if self.money_on_account < amount:
                raise ValueError("Not enough money on the account")
            else:
                self.money_on_account -= amount

    def close(self):
        self.error_if_closed()
        self.money_on_account = 0
        self.is_account_open = False

    def error_if_closed(self):
        if not self.is_account_open:
           raise ValueError("Account is closed.")
    
    def error_if_opened(self):
        if self.is_account_open:
           raise ValueError("Account is opened.")