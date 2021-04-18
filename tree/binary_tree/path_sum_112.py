class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def path_sum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right and target- root.val == 0:
            return True
        return self.path_sum(root.left, target-root.val) or self.path_sum(root.right, target-root.val)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
binary_tree = BinaryTree()
print(binary_tree.path_sum(tree, 8))