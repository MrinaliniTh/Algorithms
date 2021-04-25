class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.tree = None

    def print_binary_tree(self):
        if self.tree:
            self.get(self.tree)

    def get(self, node):
        if node:
            self.get(node.left)
            print(str(node.val) + ' ')
            self.get(node.right)

    def find_sum_root_to_leaf(self):
        res = []
        self.find_sum(self.tree, res, 0)
        return sum(res)

    def find_sum(self, node, res, cur):
        if not node:
            return 0
        cur = cur * 10 + node.val
        if not node.left and not node.right:
            res.append(cur)
            return
        self.find_sum(node.left, res, cur)
        self.find_sum(node.right, res, cur)

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)
bt = BinaryTree()
bt.tree = node
bt.print_binary_tree()
print(bt.find_sum_root_to_leaf())