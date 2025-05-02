'''
- an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
- exception is divided into two types:
    - built-in exceptions: these are exceptions that are pre-defined in Python, such as ZeroDivisionError, ValueError, etc.
    - user-defined exceptions: these are exceptions that are defined by the user using the class keyword.
- exception handling is a mechanism to handle runtime errors in a program.
- the try-except block is used to catch and handle exceptions in Python.
- the try block contains the code that may raise an exception, and the except block contains the code to handle the exception.
- the else block is optional and contains code that will run if no exception occurs in the try block.
- the finally block is also optional and contains code that will always run, regardless of whether an exception occurred or not.
syntax:
try:
    # code that may raise an exception
except ExceptionType:
    # code to handle the exception
else:
    # code to run if no exception occurs
finally:
    # code that will always run, regardless of exceptions
'''
# example 1
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("Execution completed.")

#user-defined exception
class AgeException(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def checkAge(self, age):
        if age < 18:
            raise AgeException("Age must be at least 18.")
        else:
            print("Age is valid.")

#use the custom exception
try:
    age = int(input("Enter your age: "))
    custom_error = AgeException("Custom error occurred.")
    custom_error.checkAge(age)
except AgeException as e:
    print(e.message)

