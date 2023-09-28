import streamlit as st
import re
from simpleai.search import CspProblem, backtrack

# Set Streamlit page config
st.set_page_config(layout="centered")
st.title("Cryptarithmetic Puzzles 🧩")
st.divider()
container = st.container()

# Explanation and user input
container.write("A cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols). Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified.")
container.write("For example:")
user_input = st.text_input("Enter Your Puzzle")

new_input = re.split(r'\s+', user_input)

# Extract unique letters from the input
def extract(input_user):
    letters = set()
    for word in new_input:
        for char in word:
            if char.isalpha():
                letters.add(char)
    return letters

user_variables = extract(user_input)

# Define domains for variables (initially 0-9 for all)
domains = {variable: list(range(0, 10)) for variable in user_variables}

# Update domains for variables found at the beginning of words to [1-9]
for variable in user_variables:
    for word in new_input:
        if variable == word[0]:
            domains[variable] = list(range(1, 10))

# Define constraints
def constraint_unique(variables, values):
    return len(values) == len(set(values))  # Check for unique values

def constraint_add(variables, values):
    variable_to_value = {var: val for var, val in zip(variables, values)}

    total = 0
    current_number = ''
    for item in new_input:
        if item.isalpha():
            current_number += str(variable_to_value[item])
        else:
            total += int(current_number)
            current_number = ''
    total += int(current_number)
    return total

constraints = [
    (user_variables, constraint_unique),
    (user_variables, constraint_add),
]

problem = CspProblem(user_variables, domains, constraints)

# Solve the CSP problem
output = backtrack(problem)

st.write(output)
