'''
Iterators in python
Iterators are objects that allow you to iterate over a collection of items, such as lists, tuples, or dictionaries, without needing to know the underlying structure of the collection. They implement two methods: `__iter__()` and `__next__()`.
- `__iter__()` returns the iterator object itself.
- `__next__()` returns the next item from the iterator. When there are no more items to return, it raises a `StopIteration` exception.
'''
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Example usage of the iterator
data = [1, 2, 3, 4, 5]
my_iterator = MyIterator(data)

print(next(my_iterator)) # Output: 1
