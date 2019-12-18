import sys
sys.path.append("../doubly_linked_list.py")
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.linked = DoublyLinkedList()
        #it should look like a dictionary of dictionaries, in theory.
        self.storage = {}
        
    # def make_cache(self, linked=self.linked):
    #     #for each item in the DoublyLinkedList we want to add the item to the storage dictionary
    #     current = linked.head
    #     i=1
    #     #starting at the head node, loop through all items
    #     while current is not None:
    #         #if below the limit, just add the item to the cache.
    #         if i <= (self.limit+1):
    #             #add the node value and a time counter to each cache entry
    #             self.storage["item"+str(i)]= dict(node=current.value, time_counter=i)
    #             current = current.next
    #             i += 1
    #         elif i > self.limit:
    #             #find the cache item with the lowest time_counter
    #             oldest_node = self.storage["item1"]
    #             for x in self.storage:
    #                 if x.time_counter < oldest_node.time_counter:
    #                     oldest_node = x
    #             #once located, replace the oldest_node values with the current node ones.
    #             oldest_node.node = current.value
    #             oldest_node.time_counter = i
    #             #update i and move to the next node
    #             i += 1
    #             current = current.next
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            # #move the requested item to the end of the linked list
            # current = self.linked.head
            # while self.storage[key].node is not current.value:
            #     current = current.next
            # self.linked.move_to_end(current) 
            # #rebuild the cache.
            # self.make_cache()
            self.linked.move_to_front(self.storage.get(key))
            return self.linked.head.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        
        if key in self.storage:
            self.storage.get(key).value=(key,value)
            self.linked.move_to_front(self.storage.get(key))
        else:
            self.linked.add_to_head((key,value))
            self.storage[key] = self.linked.head

            if self.current >= self.limit:
                self.storage.pop(self.linked.remove_from_tail()[0])
            else:
                self.current += 1
        
        # #if the given key exists, it overwrites the value, and moves it to the end of the cache
        # if self.storage[key] is not None:
        #     self.storage[key].node = value
        #     self.get(self.storage[key])
        # #if it doesnt exist, it creates a new node in the linked list and rebuilds the cache appropriately.
        # else:
        #     self.linked.add_to_tail(value)
        #     self.make_cache()
        
