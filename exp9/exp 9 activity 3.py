# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:54:55 2026

@author: shruti jadhav
"""
import datetime

# Get current timestamp
now = datetime.datetime.now()

# Get weekday name (e.g., Monday)
weekday = now.strftime("%A")

print(f"Office Attendance Log | Day: {weekday}")

