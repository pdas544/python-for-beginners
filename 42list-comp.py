'''
List Comprehension
# List comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause,
# and can also include an optional if clause.

Syntax:
newlist = [expression for item in iterable if condition]
# Example: Create a list of squares of even numbers from 0 to 9
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
'''
# Example: Create a list of numbers from 0 to 9
nums = [x for x in range(10)]

print("numbers are")
print(nums)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#square of numbers
print("squares of numbers are")
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#squares of even numbers
print("squares of even numbers are")
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # Output: [0, 4, 16, 36, 64]

# Create a list of tuples (number, square) for numbers from 0 to 9
tuples = [(x, x**2) for x in range(10)]
print("tuples of numbers and their squares are")
print(tuples)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

'''
Practice Exercise:

'''
