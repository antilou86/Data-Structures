import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if the value passed in is greater/less than self.value
        #in either direction/outcome, check if the next node exists
        #if it does exist, move to that node and check again
        if self.contains(value):
            return
        elif value <= self.value and self.left is not None:
            #calls itself on the next node
            self.left.insert(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        elif value <= self.value and self.left is None:
            #sets the empty spot to a bst
            self.left = BinarySearchTree(value)
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right == None:
            return False
        elif target < self.value and self.left == None:
            return False
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #if there is a right, go right
        if self.right is not None:
            return self.right.get_max()
        #if not, return the value     
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        cb(self.value)

        #if there is a node on the right, recur on that.
        if self.right is not None:
            self.right.for_each(cb)

        #if there is a node on the left, recur on that.
        if self.left is not None:
            self.left.for_each(cb)
        #this should hit all nodes, theoretically.

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #initial thoughts for tomorrow's first probo
        listicle = []
        cb = lambda x: listicle.append(x)
        self.for_each(cb)
        new_arr = listicle.sort()
        for i in new_arr:
            print(f"{i}\n")

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
