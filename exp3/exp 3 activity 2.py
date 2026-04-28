# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:50:07 2026

@author: shruti jadhav
"""
def calculate_emi(principal, annual_rate, years):
    r = annual_rate / (12 * 100)  # Monthly interest rate
    n = years * 12                # Total number of months
    
    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return emi

# Example usage
p = 500000  # Loan amount
rate = 8.5  # Interest rate
t = 5       # Years
print(f"Monthly EMI: {calculate_emi(p, rate, t):.2f}")
