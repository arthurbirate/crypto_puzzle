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

# letters = []

# for char in user_input:
#     if char.isalpha():
#         letters.append(char)
def extract(input_user):

    letters = set()

    # to_set = set(letters)
    
    variables = input_user

    for char in variables:
        if char.isalpha():
            letters.add(char)
    
    return letters
     
    # letters = []
    # set_letters = set(letters)
    # to_list = list(set_letters)
    # for char in input_user:
    #     if char.isalpha():
    #         letters.append(char)
    
    # return to_list

user_variables = extract(user_input)

domains = {}

for word in new_input:
  for variable in user_variables:
      if word.startswith(variable):
        domains[variable] =list(range(1,10))
      else:
        domains[variable] =list(range(0,10))
       
       
    
    


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





st.write(domains)










# st.text(" ")

