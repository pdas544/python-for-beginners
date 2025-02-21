'''
Conditional Statements:
- Execute the program based on some condition
Syntax:
    if condition:
    # Code block to execute if condition is True
    else:
    # Code block to execute if condition is False
    
- can be of two types:
    - if-else (simple expression)
    - if-elif-else-if (nested expression)

'''

# Define a variable
number = 10

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# nested if else statement
marks = 30

if marks >= 60:
    print("First Class")
elif marks < 60 and marks >=40:
    print("Second Class")
else:
    print("Pass")
