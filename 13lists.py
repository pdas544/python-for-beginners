'''
List data structures
1. A list is a collection of items that can be of different types.
2. Lists are mutable, meaning you can change their contents.
3. Lists are ordered, meaning the items have a defined order.
4. Lists can contain duplicate items.
5. Lists are defined using square brackets [].
6. Lists can be nested, meaning you can have lists within lists.

'''
# Step-1: Create a list
my_list = [1, 2, 3, 4, 5]
# Step-2: Access elements using indexing
print(my_list[0])  # Output: 1
# Step-3: Modify elements using indexing
my_list[0] = 10


#methods to perform operations on lists
# Step-4: Add elements using append() method
my_list.append(6)   #output: [10, 2, 3, 4, 5, 6]
# Step-5: Remove elements using remove() method
my_list.remove(10)  #output: [2, 3, 4, 5, 6]
# Step-6: Sort elements using sort() method
my_list.sort()  #output: [2, 3, 4, 5, 6]
# Step-7: Iterate through elements using a for loop
for item in my_list:
    print(item)  # Output: 2 3 4 5 6
# Step-8: List Comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [4, 9, 16, 25, 36]
# Step-9: Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
# Accessing elements in a nested list
print(nested_list[0][1])  # Output: 2