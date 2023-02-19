# Tasks from the function and methods section
# The Complete Python Bootcamp from zero to hero by Jose Portilla
# Leven One tasks: my solutions
# link: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# Exercise 1: OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# -------------------- 1st solution---------------------------

def cap_edges(name):
    cap_name = ''
    n = 0
    for letter in name:
        if n == 0 or n == 3:
            cap_name += letter.upper()
        else:
            cap_name += letter.lower()
        n += 1
    return cap_name


# check
b = cap_edges('something')
print(b)


# Ex2. Master Yoda: Given a sentence, return a sentence with the words reversed


def reversed_sentence(sentence):
    word_list = sentence.split()
    new_list = []
    n = len(word_list)-1
    while n >= 0:
        new_list.append(word_list[n])
        n -= 1
    new_sentence = ' '.join(new_list)
    return new_sentence


# check
print(reversed_sentence('I am Lukasz'))


# Ex3 Almost there: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(number):
    number_list = [100, 200]
    bool_var = False
    for element in number_list:
        min_element = element - 10
        max_element = element + 10
        if min_element <= number <= max_element:
            bool_var = True
    return bool_var


# check
print('89:', almost_there(89))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))