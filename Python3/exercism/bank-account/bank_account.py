import threading


class BankAccount(object):
    """ Implements a basic functionality for a bank account.

    An account can be open or closed, only an open account supports operations.
    You can deposit and withdraw money from an account.
    Deposits and withdraws support concurrent transactions. 
    """
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
        """ Reserves a thread and executes a deposit."""
        with BankAccount.ThreadLock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("You cannot deposit negative money.")
            else:
                self.money_on_account += amount

    def withdraw(self, amount):
        """ Reserves a thread and executes a withdrawal."""
        with BankAccount.ThreadLock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("You cannot withdraw negative money.")
            if self.money_on_account < amount:
                raise ValueError("Not enough money on the account.")
            else:
                self.money_on_account -= amount

    def close(self):
        self.error_if_closed()
        self.money_on_account = 0
        self.is_account_open = False

    def error_if_closed(self):
        if not self.is_account_open:
           raise ValueError("Account is currently closed.")
    
    def error_if_opened(self):
        if self.is_account_open:
           raise ValueError("Account is currently opened.")