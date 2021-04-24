class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.tree = None

    def creation(self, val):
        if self.tree:
            self.add(self.tree, val)
        else:
            self.tree = Node(val)

    def add(self, node, val):
        if val < node.val:
            if node.left:
                self.add(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self.add(node.right, val)
            else:
                node.right = Node(val)

    def print_binary_tree(self):
        if self.tree:
            self.get(self.tree)

    def get(self, node):
        if node:
            self.get(node.left)
            print(str(node.val) + ' ')
            self.get(node.right)

bt = BinaryTree()
bt.creation(1)
bt.creation(2)
bt.creation(3)
bt.creation(4)
bt.creation(5)
bt.creation(6)
bt.creation(7)
bt.print_binary_tree()
