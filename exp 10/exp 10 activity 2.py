# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 06:01:00 2026

@author: shruti jadhav
"""
import streamlit as st

st.title("⚖️ BMI Health Checker")

weight = st.number_input("Enter your weight (in kg)", min_value=1.0)
height = st.number_input("Enter your height (in meters)", min_value=0.1)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")
    
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Category: Normal Weight")
    elif 25 <= bmi < 30:
        st.info("Category: Overweight")
    else:
        st.error("Category: Obese")

