'''
file handling in python
- file handling is the process of reading from and writing to files in a program.
- we can perform various operations on files
    - open, read, write, append, close
- file modes:
    - 'r': read mode (default)
    - 'w': write mode (overwrites the file)
    - 'a': append mode (adds to the end of the file)
    - 'x': exclusive creation (fails if the file already exists)
    - 'b': binary mode (for non-text files)
    - 't': text mode (default)
'''
# open a file in read mode
file = open("example.txt", "r")
# read the contents of the file
content = file.read()
# print the contents of the file
print(content)
# close the file
file.close()

#using with statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#writing to a file
'''
1. open a file in write mode
2. write to the file using the write() method
3. close the file

previous contents of the file will be overwritten
'''
with open("example.txt", "w") as file:
    file.write("Hello, World!")
    file.write("\nThis is a new line.")
    file.write("\nThis is another new line.")

# append to a file
'''
1. open a file in append mode
2. write to the file using the write() method
3. close the file
previous contents of the file will be preserved
'''
with open("example.txt", "a") as file:
    file.write("\nThis line is appended to the file.")
    file.write("\nThis is another appended line.")