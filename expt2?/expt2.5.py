# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:36:41 2026

@author: shruti,priti
"""
marks = int(input("Enter student marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")