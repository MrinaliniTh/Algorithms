class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def find_height_of_BT(self, root):
        if not root:
            return 0
        left = 1 + self.find_height_of_BT(root.left)
        right = 1 + self.find_height_of_BT(root.right)
        return max(left, right)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
tree.left.left.left = Node(10)
binary_tree = BinaryTree()
print(binary_tree.find_height_of_BT(tree))