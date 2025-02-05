'''
Operators in Python:

- Operators are symbols for performing operations
- Values operands
- Symbol: operator

For eg: 
a+b 
where +: operator, and a,b: operands

Different types of operators are as follows:

1. Arithmetic Operators:
   - Addition (+), Subtraction (-), Multiplication (*), Division (/)
   - Modulus (%), Exponentiation (**), Floor division (//)

2. Comparison Operators:
   - Equal (==), Not equal (!=), Greater than (>), Less than (<)
   - Greater than or equal to (>=), Less than or equal to (<=)

3. Logical Operators:
   - and, or, not

4. Assignment Operators:
   - Equals (=), Add and assign (+=), Subtract and assign (-=)
   - Multiply and assign (*=), Divide and assign (/=), etc.

5. Bitwise Operators:
   - AND (&), OR (|), XOR (^), NOT (~)
   - Shift left (<<), Shift right (>>)

6. Membership Operators:
   - in, not in

7. Identity Operators:
   - is, is not

These operators allow you to perform various operations on variables and values in your Python programs.
'''

# Arithmetic Operators
#input is taken from the user and converted to integer
a = int(input("Enter first number"))    
b = int(input("Enter second number"))

# Addition  
print(a + b)  # Output: 15

# Subtraction

print(a - b)  # Output: 5

# Multiplication

print(a * b)  # Output: 50

# Division

print(a / b)  # Output: 2.0

# Modulus

print(a % b)  # Output: 0

# Exponentiation

print(a ** b)  # Output: 1000

# Floor division

print(a // b)  # Output: 2

# Comparison Operators

print(a == b)  # Output: False

print(a!= b)  # Output: True

print(a > b)  # Output: True

print(a < b)  # Output: False

print(a >= b)  # Output: True

print(a <= b)  # Output: False

# Logical Operators

print(True and False)  # Output: False

print(True or False)  # Output: True

print(not True)  # Output: False

# Assignment Operators

c = a
print(c)  # Output: 10

c += b
print(c)  # Output: 15

c -= b

