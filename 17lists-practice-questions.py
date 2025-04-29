'''
practice questions on lists
1. Create a list of numbers from 1 to 10 and print the list.
2. Create a list of numbers and find the sum of all the numbers in the list.
3. Create a list of numbers and find the maximum and minimum numbers in the list.
4. Create a list of numbers and find the average of all the numbers in the list.
5. Create a list of numbers and find the second largest number in the list.
'''
#1. Create a list of numbers from 1 to 10 and print the list.
numbers = list(range(1, 11))
print("List of numbers from 1 to 10:", numbers)
#2. Create a list of numbers and find the sum of all the numbers in the list.
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print("Sum of numbers:", sum_of_numbers)
#3. Create a list of numbers and find the maximum and minimum numbers in the list.
numbers = [1, 2, 3, 4, 5]
max_number = max(numbers)
min_number = min(numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)
#4. Create a list of numbers and find the average of all the numbers in the list.
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print("Average of numbers:", average)
#5. Create a list of numbers and find the second largest number in the list.
numbers = [1, 2, 3, 4, 5]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
else:
    second_largest = None
print("Second largest number:", second_largest)
