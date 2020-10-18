#Reverse Link list
# solution::
# Iterative approach: time:O(n), space:O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class ReverseLinlList:
    def __init__(self):
        self.head = None

    def push_nodes(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        self.head = prev

llist = ReverseLinlList()
llist.push_nodes(10)
llist.push_nodes(20)
llist.push_nodes(30)
llist.push_nodes(40)
print("Given list")
llist.print_list()
print("List after reverse")
llist.reverse_list()
llist.print_list()