# Task from the function and methods section
# The Complete Python Bootcamp from zero to hero by Jose Portilla
# Leven Two task: my solution
# link: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/
# 03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# Ex1 SPY GAME: Write a function that takes
# in a list of integers and returns True if it contains 007 in order


def spy_game(nums):
    spy_list = []
    for num in nums:
        if num == 0 and spy_list == []:
            spy_list.append(num)
        elif spy_list == [0] and num == 0:
            spy_list.append(num)
        elif spy_list == [0,0] and num == 7:
            spy_list.append(num)
    return len(spy_list) == 3

print(spy_game([1, 6, 0, 7, 0]))
print(spy_game([0, 6, 2, 0, 7, 0]))