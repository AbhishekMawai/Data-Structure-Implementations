"""Implementation of singly Linked List in python.
    There are two classes, Node and LinkedList containing
    functions for common operations"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.get_next() is not None:
                cur = cur.get_next()
            cur.set_next(new_node)

    def list_elements(self):
        current = self.head
        while current:
            print(current.data)
            current = current.get_next()

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        if current is None:
            return "Empty List"
        else:
            while current.get_data() != data:
                current = current.get_next()
                if current is None:
                    raise ValueError("Data not in list")
            return current

    def reverse(self):

        prev = None
        cur = self.head

        while cur is not None:
            next = cur.get_next()  # Pointer to the next node
            # Setting pointer of current node to the previous one to reverse
            cur.set_next(prev)
            prev = cur  # prev now has pointer to the value stored in cur
            # cur now has pointer to cur.get_next() which was stored in next.
            cur = next
        self.head = prev

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.get_data() == data:
                break
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
