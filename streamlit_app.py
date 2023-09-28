import streamlit as st 


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

st.title(" Cryptarithmetic puzzles 🧩 ")
st.divider()
container = st.container()
buff, col, buff2 = st.beta_columns([1,3,1])

container.write(" cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols).Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified:")

container.write("For example: ")



user_input = col.text_input("Enter Your Puzzl ")









# st.text(" ")

# variable_1 = st.text_input("Enter variable")

