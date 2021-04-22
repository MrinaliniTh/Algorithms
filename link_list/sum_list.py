class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def sum_list(self, node1, node2):
        reversed_node1 = self.reversed_num(node1)
        reversed_node2 = self.reversed_num(node2)
        num1 = self.get_num(reversed_node1)
        num2 = self.get_num(reversed_node2)
        sum_digit = int(''.join(num1)) +  int(''.join(num2))
        return sum_digit

    def reversed_num(self, node):
        prev = None
        cur = node
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def get_num(self, node):
        num = []
        while node:
            num.append(str(node.val))
            node = node.next
        return num

node1 = Node(7)
node1.next = Node(1)
node1.next.next = Node(6)

node2 = Node(5)
node2.next = Node(9)
node2.next.next = Node(2)

s = LinkedList()
print(s.sum_list(node1, node2))