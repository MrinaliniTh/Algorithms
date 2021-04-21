
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_link_list(self, val): # O(n) time complexity
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val)

    def print_link_list(self): # O(n) time complexity
        temp = self.head
        data = ""
        while temp is not None:
            if temp.next is None:
                data += str(temp.val)
                temp = temp.next
            else:
                data += str(temp.val) + '->'
                temp = temp.next
        return data

    def insert_at_beginning(self, val): # O(1) time complexity
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, val): # O(n) time complexity
        temp = self.head
        while temp:
            if not temp.next:
                temp.next = Node(val)
                temp = temp.next
            temp = temp.next

    def insert_at_pos(self, val, pos): # O(n) time complexity
        count = 1
        temp = self.head
        while count < pos:
            count += 1
            temp = temp.next
        new_node = Node(val)
        next_nodes = temp.next
        temp.next = new_node
        new_node.next = next_nodes

    def delete_node(self, val):
        temp = self.head
        if temp.val == val:# O(1) time complexity
            deleted_node = temp
            self.head = temp.next
            deleted_node = None
        else:
            while temp.next.val != val:# O(n) time complexity
                temp = temp.next
            deleted_node = temp.next
            temp.next = temp.next.next
            deleted_node = None

    def reverse_list(self):
        # import pdb;pdb.set_trace()
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
            

node = LinkedList()
# creation of link list
node.create_link_list(1)
node.create_link_list(2)
node.create_link_list(3)
node.create_link_list(4)
node.create_link_list(5)
print(node.print_link_list())

# insert at beginning
# node.insert_at_beginning(0)
# print(node.print_link_list())

# insert at end
# node.insert_at_end(6)
# print(node.print_link_list())

# insert at position
# node.insert_at_pos(10, 2)
# print(node.print_link_list())

# delete node
# node.delete_node(0)
# print(node.print_link_list())

#reverse link list
node.reverse_list()
print(node.print_link_list())


