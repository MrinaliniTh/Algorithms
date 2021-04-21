import math

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

    def delete_node_at_middle(self):
        slow = self.head
        fast = self.head
        prev = None
        if not self.head:
            return None
        if not self.head:
            self.head = None
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

    # def find_lenght(self):
    #     count = 1
    #     temp = self.head
    #     if not temp:
    #         return 0
    #     while temp.next:
    #         temp = temp.next
    #         count += 1
    #     return count

    # def delete_node_at_middle(self):
    #     size = self.find_lenght()
    #     mid_size = math.ceil(size / 2)
    #     print(mid_size)
    #     count = 1
    #     if not self.head:
    #         return "link list is empty"
    #     else:
    #         temp = self.head
    #         while (count < mid_size-1):
    #             temp = temp.next
    #             count += 1
    #         next_nodes = temp.next.next
    #         deleted_node = temp.next
    #         temp.next = next_nodes
    #         deleted_node = None


node = LinkedList()
# creation of link list
node.create_link_list(1)
node.create_link_list(2)
node.create_link_list(3)
node.create_link_list(4)
node.create_link_list(5)
# node.create_link_list(6)
print(node.print_link_list())

# print(node.find_lenght())

node.delete_node_at_middle()
print(node.print_link_list())