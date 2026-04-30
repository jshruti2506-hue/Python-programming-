# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 05:58:50 2026

@author: shruti jadhav
"""
import streamlit as st

st.title("🛒 Grocery Bill Calculator")

if 'items' not in st.session_state:
    st.session_state.items = []

with st.form("item_form"):
    name = st.text_input("Item Name")
    price = st.number_input("Price", min_value=0.0, step=0.01)
    submitted = st.form_submit_button("Add Item")
    
    if submitted and name:
        st.session_state.items.append({"name": name, "price": price})

if st.session_state.items:
    st.write("### Your Cart")
    total = 0
    for item in st.session_state.items:
        st.write(f"- {item['name']}: ${item['price']:.2f}")
        total += item['price']
    
    st.divider()
    st.subheader(f"Total: ${total:.2f}")
    if st.button("Clear List"):
        st.session_state.items = []
        st.rerun()

