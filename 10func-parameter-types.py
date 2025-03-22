'''
Types of parameters:
1. Positional parameters
2. Keyword parameters
3. Default parameters
4. Variable-length parameters

'''

# 1. Positional parameters: sequency of parameters should be same as the function definition
def greet(name,msg):
    print(f"{msg}, {name}!")

greet("John","Good Morning") # Good Morning, John!

# 2. Keyword parameters: order of parameters can be changed
greet(msg="Good Morning",name="John") # Good Morning, John!

# 3. Default parameters: default value is assigned to the parameter
def greet(name,msg="Good Morning"):
    print(f"{msg}, {name}!")

greet("John") # Good Morning, John!
greet("John","Good Night") # Good Night, John!

# 4. Variable-length parameters: *args and **kwargs
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)  # Output: 1 2 3 4

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York