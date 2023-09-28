from simpleai.search import CspProblem, backtrack
import streamlit as st 
import re
st.set_page_config(layout="centered")


st.title(" Cryptarithmetic puzzles 🧩 ")
st.divider()
container = st.container()


container.write(" cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols).Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified:")

container.write("For example: ")
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
          

# st.write(domains) 
    
    # for variable in user_variables:
    #     if word.startswith(variable):
    #         domains[variable] = list(range(1, 10))
    #     if not word.startswith(variable):
    #         domains[variable] = list(range(0, 10))
       
    
    


# st.write(new_input)
def constraint_unique(variables, values):
    return len(values) == len(set(values))  # remove repeated values and count

def constraint_add(variables, values):
    # Create a dictionary to map variables to their values
    variable_to_value = {var: val for var, val in zip(variables, values)}

    # Calculate the sum based on new_input
    total = 0
    current_number = ''
    for item in new_input:
        if item.isalpha():
            current_number += str(variable_to_value[item])
        else:
            total += int(current_number)
            current_number = ''
    total += int(current_number)  # Add the last number if any
    return total



constraints = [
    (user_input, constraint_unique),
    (user_input, constraint_add),
]

problem = CspProblem(user_input, domains, constraints)

output = backtrack(problem)

st.write(output)
















# st.text(" ")

