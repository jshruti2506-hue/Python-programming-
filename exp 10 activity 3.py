# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 06:01:53 2026

@author: shruti jadhav
"""
import streamlit as st

st.title("🎓 Student Result Calculator")

math = st.number_input("Maths Marks", 0, 100)
science = st.number_input("Science Marks", 0, 100)
english = st.number_input("English Marks", 0, 100)

if st.button("Get Results"):
    total = math + science + english
    avg = total / 3
    
    if avg >= 90: grade = "A+"
    elif avg >= 75: grade = "A"
    elif avg >= 60: grade = "B"
    elif avg >= 35: grade = "C"
    else: grade = "Fail"
    
    st.write(f"**Total Marks:** {total}/300")
    st.write(f"**Average:** {avg:.2f}%")
    st.metric(label="Final Grade", value=grade)

