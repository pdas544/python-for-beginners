'''
Generators are used to create iterators in Python.
# They allow you to iterate through a sequence of values without storing the entire sequence in memory.
Generators are a simpler way to create iterators using the `yield` statement. When a function contains a `yield` statement, it becomes a generator function. Each time the generator's `__next__()` method is called, the function runs until it hits a `yield` statement, returning the yielded value and pausing its state until the next call.
'''
def my_generator(data):
    for item in data:
        yield item
# Example usage of the generator
data = [1, 2, 3, 4, 5]
my_gen = my_generator(data)
print(next(my_gen))  # Output: 1
print(next(my_gen))  # Output: 2
print(next(my_gen))  # Output: 3
# You can also iterate through the generator using a for loop
for value in my_gen:
    print(value)  # Output: 4, 5
# Note: After the for loop, the generator is exhausted, and calling next(my_gen) will raise StopIteration.
# To reset the generator, you need to create a new instance
