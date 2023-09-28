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
     domain_updated = False  # Flag to check if the domain has been updated
     for word in new_input:
        if variable == word[0] and not domain_updated:
            domains[variable] = list(range(1, 10))
            domain_updated = True
        else:
            domains.setdefault(variable, []).extend(list(range(0, 10)))
          

st.write(domains) 
    
    # for variable in user_variables:
    #     if word.startswith(variable):
    #         domains[variable] = list(range(1, 10))
    #     if not word.startswith(variable):
    #         domains[variable] = list(range(0, 10))
       
    
    


# st.write(new_input)
# def constraint_unique(variables, values):
#     return len(values) == len(set(values))  # remove repeated values and count

# def constraint_add(variables, values):
#     factor = int(str(values[1]) + str(values[3]) + str(values[5]))
#     result = int(str(values[0]) + str(values[5]) + str(values[2]) + str(values[4]))
#     return (factor + factor) == result

# constraints = [
#     (('F', 'T', 'U', 'W', 'R', 'O'), constraint_unique),
#     (('F', 'T', 'U', 'W', 'R', 'O'), constraint_add),
# ]

# problem = CspProblem(variables, domains, constraints)

# output = backtrack(problem)
# print('\nSolutions:', output)
















# st.text(" ")

