import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # because it gives us a list with a built in order of operations. 
            # if we're queueing up items that need to be processed as they came in this would be excellent

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.value = value
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size==0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
