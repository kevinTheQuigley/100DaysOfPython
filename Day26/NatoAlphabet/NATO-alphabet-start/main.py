import pandas as pd


#student_dict = {
#    "student": ["Angela", "James", "Lily"], 
#    "score": [56, 76, 98]
#}
#
##Looping through dictionaries:
#for (key, value) in student_dict.items():
#    #Access key and value
#    pass
#student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#    #Access index and row
#    #Access row.student or row.score
#    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#Globals
NATO_CSV

nato_df = pd.read_csv(NATO_CSV)

nato_dict = {nato_df.letter:nato_df.code for (index,row) in nato_df.iterrows()}

print(nato_dict("a"))

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

