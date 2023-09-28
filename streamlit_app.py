import streamlit as st 


st.set_page_config(layout="wide")

buff, col, buff2 = st.beta_columns([1,6,1])
st.title(" Cryptarithmetic puzzles 🧩 ")
st.divider()
container = st.container()


container.write(" cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols).Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified:")

container.write("For example: ")


col.text_input("Enter Your Puzzl ")









# st.text(" ")

# variable_1 = st.text_input("Enter variable")

