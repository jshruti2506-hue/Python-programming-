# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:51:48 2026

@author: shruti jadhav
"""

from datetime import date

# Fetch today's date
today = date.today()

# Format: Day Month Year
formatted_date = today.strftime("%d-%b-%Y")
print(f"Hospital Appointment System | Date: {formatted_date}")
