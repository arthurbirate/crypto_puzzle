from constraint import *
import streamlit as st
import re


st.set_page_config(layout="centered")

st.title("Cryptarithmetic puzzles 🧩")
st.divider()
container = st.container()

container.write("Cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols). Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified.")

container.write("For example:")
user_input = st.text_input("Enter Your Puzzles ")

new_input = re.split(r'\s+', user_input)


def extract(input_user):
    letters = set()
    for word in new_input:
        for char in word:
            if char.isalpha():
                letters.add(char)
    return letters


user_variables = extract(user_input)

domains = {}

for variable in user_variables:
    domains[variable] = list(range(0, 10))

# Update domains for variables found at the beginning of words to [1, 2, 3, 4, 5, 6, 7, 8, 9]
for variable in user_variables:
    for word in new_input:
        if variable == word[0]:
            domains[variable] = list(range(1, 10))

# Define constraints
problem = Problem()

# Add variables and domains
for variable, domain in domains.items():
    problem.addVariable(variable, domain)

# Define the equation as a constraint
equation = "".join(new_input)
problem.addConstraint(lambda *args: eval(equation, {var: val for var, val in zip(user_variables, args)}), user_variables)

# Solve the problem using backtracking
solutions = problem.getSolutions()

if solutions:
    st.write("Solutions:")
    for solution in solutions:
        st.write({var: val for var, val in solution.items()})
else:
    st.write("No solutions found.")
