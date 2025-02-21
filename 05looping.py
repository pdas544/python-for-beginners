'''
Looping Statements

- Execute a block of code repeatedly

- Syntax:
    for variable in sequence:
    # Code block to execute for each iteration
    For eg:
    for i in range(5):
        print("Hello")  #to display Hello 5 times (0 to 4)
- Types of looping statements
    - for loop
    - while loop

'''

# Example of a for loop
print("For Loop Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example of a while loop
print("\nWhile Loop Example:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1