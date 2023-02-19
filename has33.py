# Task from the function and methods section
# The Complete Python Bootcamp from zero to hero by Jose Portilla
# Leven Two task: my solutions (1) and from the course (2)
# link: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/
# 03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

# (1) my soluiotn

def has33(checking_list):
    n = 0
    is_33 = False
    while n <= len(checking_list)-2:
        if checking_list[n] == checking_list[n+1]:
            is_33 = True
        else:
            pass
        n += 1
    return is_33


# check
list_a = [1, 3, 4, 3, 3]
list_b = [1, 2, 3, 4, 5]

print(has33(list_a))

# (2) from the course:


def has33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


# check
print(has33([0, 0, 3, 3, 2]))

# OR


def has33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+1] == [3, 3]:
            return True
        return False


# check
print(has33([0, 0, 3, 3, 2]))