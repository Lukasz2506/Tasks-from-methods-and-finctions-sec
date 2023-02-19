# Task from the function and methods section
# The Complete Python Bootcamp from zero to hero by Jose Portilla
# Leven Two task: my solutions (1) and from the course (2)
# link: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/
# 03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally,
# if the sum (even after adjustment) exceeds 21, return 'BUST'

# (1) my solution

def is_3_args(number_tuple):
    # Check is the length ok
    return len(number_tuple) != 3


def is_in_range(number_tuple):
    # Check is the values in range
    for number in number_tuple:
        result = number > 11 or number < 1
    return result


def count_numbers(number_tuple):
    # counting all of the numbers form the tuple
    n = 0
    for number in number_tuple:
        if number == 11 and sum(number_tuple) > 21:
            n += 1
        else:
            n += number
    return n


def blackjack(*args):
    if is_3_args(args):
        print('3 numbers required!')
    elif is_in_range(args):
        print('permitted values from 1 to 11!')
    else:
        n = count_numbers(args)
        if n > 21:
            print('BUST')
        else:
            print(n)


blackjack(10, 11, 5)


# (2) from the course:

def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c])-10
    else:
        'BUST'
