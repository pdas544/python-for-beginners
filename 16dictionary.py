'''
Dictionary:
- A collection of key-value pairs.
- Keys must be unique.
- Values can be of any data type.
- Dictionaries are mutable, meaning you can change their contents.
- Dictionaries are defined using curly braces {} or the dict() function.
- Dictionaries support indexing and slicing.
- Methods in dictionaries:
1. keys(): Returns a view object that displays a list of all the keys in the dictionary.
2. values(): Returns a view object that displays a list of all the values in the dictionary.
3. items(): Returns a view object that displays a list of all the key-value pairs in the dictionary.
4. get(): Returns the value for a specified key.
5. pop(): Removes the specified key and returns the corresponding value.
6. clear(): Removes all elements from the dictionary.
7. update(): Updates the dictionary with the specified key-value pairs.
8. popitem(): Removes and returns the last inserted key-value pair.
9. del: Deletes the specified key-value pair.
10. len(): Returns the number of items in the dictionary.

'''
# Step-1: Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Step-2: Access elements using keys
print(my_dict['name'])  # Output: John
# Step-3: Add elements using assignment
my_dict['country'] = 'USA'  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
# Step-4: Remove elements using pop() method
removed_value = my_dict.pop('age')  # Output: 30
print(removed_value)  # Output: 30
# Step-5: Check membership using in operator
print('name' in my_dict)  # Output: True
# Step-6: Iterate through elements using a for loop
for key, value in my_dict.items():
    print(key, value)  # Output: name John, city New York, country USA
# Step-7: Dictionary operations
# Step-8: Get all keys using keys() method
keys = my_dict.keys()  # Output: dict_keys(['name', 'city', 'country'])
print(keys)  # Output: dict_keys(['name', 'city', 'country'])
# Step-9: Get all values using values() method
values = my_dict.values()  # Output: dict_values(['John', 'New York', 'USA'])
print(values)  # Output: dict_values(['John', 'New York', 'USA'])
# Step-10: Get all items using items() method
items = my_dict.items()  # Output: dict_items([('name', 'John'), ('city', 'New York'), ('country', 'USA')])
print(items)  # Output: dict_items([('name', 'John'), ('city', 'New York'), ('country', 'USA')])