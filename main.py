student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format from the csv
{"A": "Alfa", "B": "Bravo"}

df_nato_phonetic_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
dict_nato_phonetic_alphabet = {row.letter:row.code for (index, row) in df_nato_phonetic_alphabet.iterrows()}
dict_nato_phonetic_alphabet[' '] = ' '


# Create a list of the phonetic code words from a word that the user inputs.


def phonetic_translate():
    user_word = input('Please enter word/ phrase: \n').upper()
    try:
        user_word_nato_phonetic_list = [dict_nato_phonetic_alphabet[letter] for letter in list(user_word)]
    except KeyError:
        print('please enter valid characters for word/phrase (No special characters :@!@#$%^, etc)')
        phonetic_translate()
    else:
        print(user_word_nato_phonetic_list)


phonetic_translate()

