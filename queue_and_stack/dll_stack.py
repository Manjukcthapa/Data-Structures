import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        #adding item to the tail
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # removing item from tail
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None    

    def len(self):
        return self.size
