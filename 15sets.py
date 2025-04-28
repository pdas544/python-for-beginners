'''
Sets: 
- A set is a collection of unique elements.
- Sets are unordered, meaning the items do not have a defined order.
- Sets are mutable, meaning you can change their contents.
- Sets are defined using curly braces {} or the set() function.
- Sets do not support indexing or slicing.
- methods in sets:
1. add(): Adds an element to the set.
2. remove(): Removes an element from the set.
3. discard(): Removes an element from the set if it is present.
4. pop(): Removes and returns an arbitrary element from the set.
5. clear(): Removes all elements from the set.
'''
# Step-1: Create a set
my_set = {1, 2, 3, 4, 5}
# Step-2: Add elements using add() method
my_set.add(6)  # Output: {1, 2, 3, 4, 5, 6}
# Step-3: Remove elements using remove() method
my_set.remove(1)  # Output: {2, 3, 4, 5, 6}
# Step-4: Check membership using in operator
print(2 in my_set)  # Output: True
# Step-5: Iterate through elements using a for loop
for item in my_set:
    print(item)  # Output: 2 3 4 5 6
# Step-6: Set operations

#pop the element
popped_element = my_set.pop()  # Output: 2 (or any other element)
print(popped_element)  # Output: 2 (or any other element)
# Step-7: Clear the set using clear() method
my_set.clear()  # Output: set()
