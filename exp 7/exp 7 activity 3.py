# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:25:41 2026

@author: shruti jadhav
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        elif self.score >= 60: return "D"
        else: return "F"

# Example Usage
student = Student("Charlie", 85)
print(f"{student.name}'s Grade: {student.get_grade()}")
