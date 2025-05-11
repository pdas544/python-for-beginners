'''
Introduction to Algorithms
- Algorithm: A step-by-step procedure for solving a problem.
- Algorithm Analysis: The study of the efficiency of algorithms in terms of time and space complexity.
- Time Complexity: The amount of time an algorithm takes to complete as a function of the size of the input.
- Space Complexity: The amount of memory an algorithm uses as a function of the size of the input.
- Big O Notation: A mathematical notation used to describe the upper bound of an algorithm's time or space complexity.
- O(1): Constant time complexity. The algorithm takes the same amount of time regardless of the input size.
- O(log n): Logarithmic time complexity. The algorithm takes time proportional to the logarithm of the input size.
- O(n): Linear time complexity. The algorithm takes time proportional to the input size.
- O(n log n): Linearithmic time complexity. The algorithm takes time proportional to the input size times the logarithm of the input size.
- O(n^2): Quadratic time complexity. The algorithm takes time proportional to the square of the input size.
'''
# Example of Big O Notation
def example_function(n):
    # O(1) - Constant time complexity
    print("Hello, World!")  # This takes the same amount of time regardless of n

example_function(10)  # O(1)
#space complexity
# O(1) - Constant space complexity

# O(log n) - Logarithmic time complexity
def display_logarithmic(n):
    i = 1
    while i < n:
        print(i)
        i *= 2  # This doubles i each time, so it takes log(n) iterations

display_logarithmic(10)  # O(log n)
# O(n) - Linear time complexity
def display_linear(n):
    for i in range(n):
        print(i)  # This takes n iterations
display_linear(10)  # O(n)

# O(n^2) - Quadratic time complexity
def display_quadratic(n):
    for i in range(n):
        for j in range(n):
            print(i, j)  # This takes n^2 iterations
display_quadratic(10)  # O(n^2)
# O(n log n) - Linearithmic time complexity
def display_linearithmic(n):
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j *= 2  # This takes log(n) iterations for each i
display_linearithmic(10)  # O(n log n)