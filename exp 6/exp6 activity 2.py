# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:28:07 2026

@author: shruti jadhav
"""
def calculate_total():
    total = 0.0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                # Splitting the string to extract the numerical part
                parts = line.split(":")
                if len(parts) == 2:
                    total += float(parts[1].strip())
    except FileNotFoundError:
        return 0.0
    return total

print(f"Total Monthly Expense: ${calculate_total():.2f}")
