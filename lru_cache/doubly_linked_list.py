"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        self.length += 1

        if self.head != None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        
        self.head=new_node


    def remove_from_head(self):
        if self.head == None:
            return None
        
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        if self.tail == None:
            self.add_to_head(value)
        else:
            new_node = ListNode(value, self.tail, None)
            self.tail.next= new_node
            self.tail = new_node        
        self.length += 1

    def remove_from_tail(self):
        if self.tail == None:
            return None
        else: 
            value = self.tail.value
            self.delete(self.tail)
            return value

    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        else: 
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    def delete(self, node):
        if not self.head and not self.tail:
            return
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        if self.head == None:
            return None
        else: 
            current = self.head
            max_value = current.value
            while current is not None:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            return max_value
