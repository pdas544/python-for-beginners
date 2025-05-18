'''
Algorithm: Stack
- A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
- The last element added to the stack is the first one to be removed.
- Stack operations:
  - Push: Add an element to the top of the stack.
  - Pop: Remove the top element from the stack.
  - Peek/Top: Get the top element without removing it.
- IsEmpty: Check if the stack is empty.
- Size: Get the number of elements in the stack.
- Applications of stacks:
  - Function call management in programming languages.
  - Undo mechanisms in text editors.
  - Expression evaluation and syntax parsing.
'''
# Stack implementation using a list using TOP as the last element
class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty stack

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item from the stack
        else:
            raise IndexError("Pop from an empty stack")  # Raise an error if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it
        else:
            raise IndexError("Peek from an empty stack")  # Raise an error if the stack is empty

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def size(self):
        return len(self.items)  # Return the number of items in the stack
    
# Example usage
if __name__ == "__main__":
    stack = Stack()  # Create a new stack
    stack.push(1)  # Push 1 onto the stack
    stack.push(2)  # Push 2 onto the stack
    stack.push(3)  # Push 3 onto the stack

    print(f"Stack contents: {stack.items}")  # Output: Stack contents: [1, 2, 3]

    print("Top element:", stack.peek())  # Output: Top element: 3
    print("Stack size:", stack.size())  # Output: Stack size: 3

    print("Popped element:", stack.pop())  # Output: Popped element: 3
    print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2

    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

    print(f"Stack contents: {stack.items}")  # Output: Stack contents: [1, 2]