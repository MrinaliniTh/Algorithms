class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def level_order(self, root):
        q = []
        q.append(root)
        res = []
        while q:
            temp = q.pop(0)
            res.append(temp.val)
            if temp.left and temp.left not in q:
                q.append(temp.left)
            if temp.right and temp.right not in q:
                q.append(temp.right)
        return res
            
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
binary_tree = BinaryTree()
print(binary_tree.level_order(tree))