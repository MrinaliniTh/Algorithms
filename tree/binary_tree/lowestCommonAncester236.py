class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def lowest_common_ancester(self, root, p, q):
        if not root:
            return None
        if root.val == p or root.val == q:
            return root.val
        left = self.lowest_common_ancester(root.left, p, q)
        right = self.lowest_common_ancester(root.right, p, q)
        if not left and not right:
            return None
        if left and right:
            return root.val
        if left and not right:
            return left
        return right
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
tree.right.left.left = Node(8)
tree.right.left.right = Node(9)
binary_tree = BinaryTree()
print(binary_tree.lowest_common_ancester(tree, 3, 9))