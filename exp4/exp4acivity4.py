# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:41:53 2026

@author: User
"""

review = "the food was good and the staff was very good"
word_to_find = "good"

# count() is case-sensitive; use .lower() for better accuracy
count = review.lower().split().count(word_to_find)

print(f"The word '{word_to_find}' appears {count} times.")