# Task from the function and methods section
# The Complete Python Bootcamp from zero to hero by Jose Portilla
# Leven Two task: my solutions (similar to this from the course (I'm proud of myself :)))
# link: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/
# 03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb


# PAPER DOLL: Given a string, return a string where for every character
# in the original there are three characters

def paper_doll(word):
    new_word = ''
    for letter in word:
        new_word += letter*3
    return new_word


print(paper_doll('abc'))

