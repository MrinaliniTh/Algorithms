class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def max_depth(self, root):
        return self.helper(root, 0)

    def helper(self, root, sum):
        if not root:
            return sum
        left = self.helper(root.left, sum+1)
        right = self.helper(root.right, sum+1)

        return max(left, right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.left = Node(5)
tree.right.right = Node(6)
tree.right.left.left = Node(7)
tree.right.left.right = Node(8)
binary_tree = BinaryTree()
print(binary_tree.max_depth(tree))