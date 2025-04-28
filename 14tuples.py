'''
Tuples
Tuples are immutable sequences, typically used to store collections of heterogeneous data.
1. Tuples are immutable, meaning you cannot change their contents after creation.
2. Tuples are ordered, meaning the items have a defined order.
3. Tuples can contain duplicate items.
4. Tuples are defined using parentheses ().
Example: store account number which does not change
'''
# Step-1: Create a tuple
my_tuple = (1, 2, 3, 4, 5)
# Step-2: Access elements using indexing
print(my_tuple[0])  # Output: 1
# Step-3: Attempt to modify elements (will raise an error)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
# Step-4: Add elements (will raise an error)
# my_tuple.append(6)  # AttributeError: 'tuple' object has no attribute 'append'
# Step-5: Remove elements (will raise an error)
# my_tuple.remove(1)  # AttributeError: 'tuple' object has no attribute 'remove'

#loop through elements
for item in my_tuple:
    print(item)  # Output: 1 2 3 4 5