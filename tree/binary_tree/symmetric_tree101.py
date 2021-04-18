class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def is_symmetric(self, root):
        if not root:
            return False
        return self.check_symmetric(root.left, root.right)

    def check_symmetric(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and not t2:
            return False
        if not t1 and t2:
            return False
        if t1.val != t2.val:
            return False
        left = self.check_symmetric(t1.left, t2.right)
        right = self.check_symmetric(t1.right, t2.left)
        return left and right


tree = Node(1)
tree.left = Node(2)
tree.right = Node(2)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.left = Node(4)
tree.right.right = Node(3)
binary_tree = BinaryTree()
print(binary_tree.is_symmetric(tree))