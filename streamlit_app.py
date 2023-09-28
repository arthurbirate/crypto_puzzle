import streamlit as st 
st.set_page_config(layout="centered")


st.title(" Cryptarithmetic puzzles 🧩 ")
st.divider()
container = st.container()


container.write(" cryptarithmetic puzzle is a mathematical exercise where the digits of some numbers are represented by letters (or symbols).Each letter represents a unique digit. The goal is to find the digits such that a given mathematical equation is verified:")

container.write("For example: ")
user_input = st.text_input("Enter Your Puzzles ")


# letters = []

# for char in user_input:
#     if char.isalpha():
#         letters.append(char)
def extract(input_user):
    return input_user
    # letters = []
    # set_letters = set(letters)
    # to_list = list(set_letters)
    # for char in input_user:
    #     if char.isalpha():
    #         letters.append(char)
    
    # return to_list

user_letters = extract(user_input)


# print(letters)
st.write(user_letters)











# st.text(" ")

