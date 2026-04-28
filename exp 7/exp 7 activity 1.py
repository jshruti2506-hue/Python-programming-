# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:23:03 2026

@author:shruti jadhav
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Example Usage
account = BankAccount("Alice", 500)
print(account.deposit(200))
print(account.withdraw(100))

