# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:24:12 2026

@author: shruti jadhav
"""
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self, bonus):
        total_salary = self.base_salary + bonus
        return f"Employee: {self.name} | Total Salary: ${total_salary}"

# Example Usage
emp = Employee("Bob", 5000)
print(emp.calculate_salary(500))

