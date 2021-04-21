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

    def reverse(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def find_mid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # time complexity: O(n) and space: O(1)
    def is_palindrome(self):
        mid = self.find_mid(self.head)
        reverse_list = self.reverse(mid)
        head = self.head
        while head and reverse_list:
            if head.val != reverse_list.val:
                return False
            head =  head.next
            reverse_list = reverse_list.next
        return True


node = LinkedList()
# creation of link list
node.create_link_list(1)
node.create_link_list(2)
node.create_link_list(3)
node.create_link_list(7)
node.create_link_list(1)
# node.create_link_list(6)
print(node.print_link_list())

print(node.is_palindrome())