# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:22:27 2026

@author: shruti jadhav
"""
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

