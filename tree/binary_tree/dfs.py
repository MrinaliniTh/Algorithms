# time complexity: O(n), because each node is visited only once
# In depth first search, there are 3 ways of traversals
# 1. inorder => left -> root -> right(this is in sorted order in binary search tree)
# 2. preorder => root -> left -> right
# 3. postorder => left -> right -> root
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:

    def inorder_traversal(self, root, res):
        if root:
            res = self.inorder_traversal(root.left, res)
            res += str(root.val) + "-"
            res = self.inorder_traversal(root.right, res)
        return res

    def preorder_traversal(self, root, res):
        if root:
            res += str(root.val) + "-"
            res = self.preorder_traversal(root.left, res)
            res = self.preorder_traversal(root.right, res)
        return res

    def postorder_traversal(self, root, res):
        if root:
            res = self.postorder_traversal(root.left, res)
            res = self.postorder_traversal(root.right, res)
            res += str(root.val) + "-"
        return res

    def inorder_iterartive(self, root):
        res = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
            while root is None and stack:
                cur = stack.pop()
                res.append(cur.val)
                root = cur.right
        return res

    def preorder_iterative(self, root):
        res = []
        stack = []
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
            while root is None and stack:
                cur = stack.pop()
                root = cur.right
        return res

    def postorder_iterative(self, root):
        stack = []
        visited = set()
        res = []
        while root:
            stack.append(root)
            root = root.left
            while root is None and stack:
                cur = stack.pop()
                if cur.right and cur.val not in visited:
                    visited.add(cur.val)
                    stack.append(cur)
                    root = cur.right
                else:
                    res.append(cur.val)
                    root = None
        return res

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
binary_tree = BinaryTree()
print(binary_tree.inorder_traversal(tree, ""))
print(binary_tree.preorder_traversal(tree, ""))
print(binary_tree.postorder_traversal(tree, ""))
print(binary_tree.inorder_iterartive(tree))
print(binary_tree.preorder_iterative(tree))
print(binary_tree.postorder_iterative(tree))