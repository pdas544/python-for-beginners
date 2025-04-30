'''
practice questions on tuples
1. Create a tuple of numbers from 1 to 10 and print the tuple.
2. Create a tuple of numbers and find the sum of all the numbers in the tuple.
3. Create a tuple of numbers and find the maximum and minimum numbers in the tuple.
'''
# #1. Create a tuple of numbers from 1 to 10 and print the tuple.
numbers = tuple(range(1, 11))
print("Tuple of numbers from 1 to 10:", numbers)
# #2. Create a tuple of numbers and find the sum of all the numbers in the tuple.
numbers = (1, 2, 3, 4, 5)
sum_of_numbers = sum(numbers)
print("Sum of numbers:", sum_of_numbers)
# #3. Create a tuple of numbers and find the maximum and minimum numbers in the tuple.
numbers = (1, 2, 3, 4, 5)
max_number = max(numbers)
min_number = min(numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)