class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList:
    def find_kth_to_last(self, node, pos):
        count = 0
        cur = node
        print(self.print_list(cur))
        print(pos)
        while count < pos:
            cur = cur.next
            count += 1
        return self.print_list(cur)

    def print_list(self, cur):
        data = ""
        while cur.next:
            data += str(cur.val) + "->"
            cur = cur.next
        return data + str(cur.val)





node1 = Node(1)
node1.next = Node(2)
node1.next.next = Node(3)
node1.next.next.next = Node(4)
node1.next.next.next.next = Node(5)
node1.next.next.next.next.next = Node(6)
l = LinkList()
print(l.find_kth_to_last(node1, 3))