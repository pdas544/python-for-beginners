'''
Functions are reusable blocks of code that perform a specific task. 
 - Improving readability
 - Avoiding repetition
 - Promotes reusability

Syntax:
def function_name(parameters):
    # function body
    # code to be executed

    
Two Steps:
1) define a function
2) call the function


Example:
#Step-1 Define a function

def greet(name):
    return f"Hello, {name}!"

#Step-2 Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

Types of Functions:
1. Built-in functions: print(), len(), type(), etc.
2. User-defined functions: Functions created by the user.


'''
#Step-1 Define a function
def greet(name):
    print(f"Hello, {name}!")

#Step-2 Calling the function
print(greet("Alice"))  # Output: Hello, Alice!