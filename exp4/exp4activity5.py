# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:42:48 2026

@author: User
"""

contacts = ["9876543210", "8888888888", "9876543210", "7777777777", "8888888888"]

# Converting to a 'set' automatically removes duplicates
unique_contacts = list(set(contacts))

print(f"Original list size: {len(contacts)}")
print(f"Cleaned list: {unique_contacts}")