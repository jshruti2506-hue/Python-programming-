# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:40:11 2026

@author: shruti jadahv
"""
# Program to calculate Simple Interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

# Calculation
si = (p * r * t) / 100

print(f"Simple Interest is: {si}")


