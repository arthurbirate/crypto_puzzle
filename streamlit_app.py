import streamlit as st
import re
from simpleai.search import CspProblem, backtrack

# Set Streamlit page config
st.set_page_config(layout="centered")
st.title("Cryptarithmetic Puzzles 🧩")
st.divider()
container = st.container()

# Explanation and user input
container.write("A cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented "
                "by letters (or symbols). Each letter represents a unique digit. The goal is to find the digits such "
                "that a given mathematical equation is verified.")
container.markdown(""" For example: 
           $$
             TWO
           + TWO
              =
             FOUR
           $$
           
           which will result to  :      
             734 +   734  = 1468
        
""")

st.info('Not all combination can work or will work', icon="ℹ️")

formbtn = st.button("Try out your puzzle")

if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False
if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True
    st.snow()
    with st.form(key='user_info'):

        user_input = st.text_input("Enter Your Puzzle", type="default")
        new_input = re.split(r'\s+', user_input)

        submit_form = st.form_submit_button(label="launch", help="Click to submit !")


        # st.write(submit_form)

        # Extract unique letters from the input
        def extract(input_user):
            letters = set()

            for word in new_input:
                for char in word:
                    if char.isalpha():
                        letters.add(char)
            return letters


        user_variables = extract(user_input)

        convert_to_tuple = tuple(user_variables)

        # Define domains for variables (initially 0-9 for all)
        domains = {variable: list(range(0, 10)) for variable in user_variables}

        # Update domains for variables found at the beginning of words to [1-9]
        for variable in convert_to_tuple:
            for word in new_input:
                if variable == word[0]:
                    domains[variable] = list(range(1, 10))


        # Define constraints
        def constraint_unique(variables, values):
            return len(values) == len(set(values))  # Check for unique values


        def constraint_add(variables, values):
            # Create a dictionary to map variables to their assigned values
            value_dict = dict(zip(variables, values))

            # Extract the words from user_input
            words = re.findall(r'\b\w+\b', user_input)

            # Extract the first two words and the result word
            word1, word2, result = words[0], words[1], words[2]

            # Calculate the numerical values of the first two words and the result word
            value_word1 = 0
            for char in word1:
                if char.isalpha():
                    value_word1 = value_word1 * 10 + value_dict[char]

            value_word2 = 0
            for char in word2:
                if char.isalpha():
                    value_word2 = value_word2 * 10 + value_dict[char]

            value_result = 0
            for char in result:
                if char.isalpha():
                    value_result = value_result * 10 + value_dict[char]

            # Check if the sum of the first two words equals the third word
            return value_word1 + value_word2 == value_result


        constraints = [
            (convert_to_tuple, constraint_unique),
            (convert_to_tuple, constraint_add),
        ]

        problem = CspProblem(user_variables, domains, constraints)

        solutions = backtrack(problem)

        with st.container():
            for solution in solutions:
                st.write(solution, " = ", solutions[solution])
