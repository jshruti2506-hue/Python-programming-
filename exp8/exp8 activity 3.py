# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:44:13 2026

@author: shruti jadhav
"""
try:
    total_bill = float(input("Enter total bill: "))
    people = int(input("Enter number of people: "))
    share = total_bill / people
    print("Each person pays:", share)
except ZeroDivisionError:
    print("Error: Cannot divide among zero people!")
