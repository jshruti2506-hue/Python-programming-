# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:47:03 2026

@author: shruti jadhav
"""
import math

point1 = (2, 3)
point2 = (5, 7)

# distance = sqrt((x2-x1)^2 + (y2-y1)^2)
distance = math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))

print(f"Distance between points: {distance:.2f}")

