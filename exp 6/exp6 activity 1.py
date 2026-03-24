# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:24:45 2026

@author: shruti jadhav
"""
def add_expense(amount, description):
    with open("expenses.txt", "a") as file:
        file.write(f"{description}: {amount}\n")

# Example usage:
add_expense(50.50, "Groceries")
add_expense(15.00, "Transport")
