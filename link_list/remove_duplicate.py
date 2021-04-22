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

    #12->11->12->21->41->43->21 --> 12->11->21->41->43.
    def remove_duplicates(self):
        hash = set()
        head = self.head
        hash.add(head.val)
        while head.next:
            if head.next.val in hash:
                head.next = head.next.next
            else:
                hash.add(head.next.val)
                head = head.next

node = LinkedList()
# creation of link list
node.create_link_list(12)
node.create_link_list(12)
node.create_link_list(12)
node.create_link_list(12)
node.create_link_list(41)
node.create_link_list(43)
node.create_link_list(21)
# node.create_link_list(6)
print(node.print_link_list())

node.remove_duplicates()
print(node.print_link_list())