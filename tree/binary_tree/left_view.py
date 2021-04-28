class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def left_view(self, node):
        que = [node]
        res = []
        while que:
            cur_val = []
            next_level = []
            for n in que:
                cur_val.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            res.append(cur_val)
            que = next_level
        ans = ""
        for val in res:
            ans += " " + str(val[0])
        return ans


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
binary_tree = BT()
print(binary_tree.left_view(tree))