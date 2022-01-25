# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)
#     pass

import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
student_data_dict = {code.letter: code.code for(letter, code) in student_data_frame.iterrows()}
print(student_data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("what's the word ? ")
alpha = [alphabet.upper() for alphabet in user_input]
result = [student_data_dict[x] for x in alpha if x in student_data_dict.keys()]
print(result)
