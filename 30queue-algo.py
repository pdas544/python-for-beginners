'''
Algorithms for queue data structure
1. Queue using list
Operations:
    - Enqueue
    - Dequeue
    - Peek
    - is_empty
    - size
'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue:", q.queue)  # Output: Queue: [1, 2, 3]
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 1
    print("Peek:", q.peek())  # Output: Peek: 2
    print("Is empty:", q.is_empty())  # Output: Is empty: False
    print("Size:", q.size())  # Output: Size: 2