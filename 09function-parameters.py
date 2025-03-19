'''
Function Parameters:

1) Allows us to pass data to a function.
2) Parameters are variables which are written inside the parentheses of the function.
3) Parameters are separated by commas.
4) Values must be passed when calling the function otherwise it will throw an error.
For eg:

def greet(name):
    print(f"Hello, {name}!")

name: is a parameter which must be passed when calling the function.

greet("John")  # Output: Hello, John!

'''
#Step-1 Define a function with two parameters
def calculate_area(length, width):
    area = length * width
    print(f"The area of the rectangle is {area} square units.")

# Function call with arguments
calculate_area(10, 5)  # Output: The area of the rectangle is 50 square units.