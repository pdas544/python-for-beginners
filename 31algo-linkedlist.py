'''
Implementing Linked List in python

Linked List is a linear data structure where each element is a separate object.
Each element (node) of a list is comprising of two items - the data and a reference (link) to the next node in the list.
The last node has a reference to null.

Types of Linked List:
1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List
'''
# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    '''
    Initialize the linked list 

    '''
    def __init__(self):
        self.head = None

    '''
        Append a new node at the end of the list
        Time Complexity: O(n)
        Space Complexity: O(1)
        where n is the number of nodes in the linked list
    '''
    def insertNode(self, data):
        '''
        Three Cases
        1) Insert at the beginning
        2) Insert at the end
        3) Insert at a specific position

        
        '''
        #insert at the beginning

        new_node = Node(data)
        # print(new_node.data)

        #initially the list is empty
        #new node will be the head

        if not self.head:
            self.head = new_node
            new_node.next = None
            
        else:
            #list is not empty
            #insert at the end
            '''
            1) Traverse to the end of the list
            2) make current_node.next = new_node
            3) new_node.next = None
            '''
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = None

            # #insert at a specific position
            # '''
            # 1) Go to the 
            # 2) When appropriate position is found
            # 3) prev_node.next = new_node
            # 4) new_node.next = current_node

            # '''
            # current_node = self.head
            # prev_node = self.head
            # while new_node.data > prev_node.data and new_node.data < current_node.data:
            #     prev_node = current_node
            #     current_node = current_node.next
            
            # prev_node.next = new_node
            # new_node.next = current_node
            

    '''
        Traversing the linked list
        Time Complexity: O(n)
        Space Complexity: O(1)
        where n is the number of nodes in the linked list
        
    '''
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if not current_node:
            return
        prev_node.next = current_node.next
        current_node = None


    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertNode(1)
    ll.insertNode(2)
    ll.insertNode(4)
    ll.print_list()
    print(f'Found : {ll.search(2)}')
   
