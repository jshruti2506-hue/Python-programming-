# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:52:17 2026

@author: shruti jadhav
"""

print("--- Multiplication Tables 1 to 10 ---")
for i in range(1, 11):
    print(f"\nTable of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
