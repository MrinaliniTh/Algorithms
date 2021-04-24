class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_link_list(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(val)
            temp.next = new_node

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

    def end_to_first(self):
        # import pdb;pdb.set_trace()
        current = self.head
        while current.next.next:
            current = current.next
        temp = current.next
        current.next = None
        temp.next = self.head
        self.head = temp

    def end_to_first_and_remove_first_node(self):
        current = self.head
        while current.next.next:
            current = current.next
        temp = current.next
        current.next = None
        temp.next = self.head.next
        self.head = temp

node = LinkedList()
# creation of link list
node.create_link_list(1)
node.create_link_list(2)
node.create_link_list(3)
node.create_link_list(4)
node.create_link_list(5)
node.create_link_list(6)
print(node.print_link_list())
# node.end_to_first()
# print(node.print_link_list())
node.end_to_first_and_remove_first_node()
print(node.print_link_list())