# WARMUP from The Complete Python Bootcamp, Jose Portilla
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb


# W1 Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(5, 4))


# W2 ANIMAL CRACKERS: Write a function takes a two-word string and returns
# True if both words begin with same letter


def animal_crackers(text):
    text_list = text.lower().split()
    return text_list[0][0] == text_list[1][0]


print(animal_crackers('Anaconda antelope'))
print(animal_crackers('snake pinguin'))


# W3 MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False

def makes_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20


print(f'Ex1: {makes_twenty(10, 20)}')
print(f'Ex2: {makes_twenty(10, 10)}')
print(f'Ex3: {makes_twenty(20, 10)}')
print(f'Ex4: {makes_twenty(5, 10)}')
