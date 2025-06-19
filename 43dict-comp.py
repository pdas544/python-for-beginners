'''
Dictionary Comprehensions
- A dictionary comprehension is a compact way to process all or part of the elements in a collection and return a dictionary with the results.
- It consists of an expression pair (key: value) followed by a for clause, and can include multiple for clauses and if conditions.
'''
# Example: Create a dictionary with numbers and their squares
squares = {x: x**2 for x in range(10)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Example: Create a dictionary with numbers and their squares, but only for even numbers
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Example: Create a dictionary from a list of tuples
tuples = [('a', 1), ('b', 2), ('c', 3)]
dict_from_tuples = {key: value for key, value in tuples}
print(dict_from_tuples)  # Output: {'a': 1, 'b': 2, 'c': 3} 