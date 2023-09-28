import streamlit as st 


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
st.title(" Cryptarithmetic puzzles 🧩 ")
container = st.container()

container.write(" cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols).Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified:")

container.write("For example: ")

with col1:
   st.header("A cat")


with col2:
   st.he("A dog")





# st.text(" ")

# variable_1 = st.text_input("Enter variable")

