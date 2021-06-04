class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def get_left_view(self, node):
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

    def get_right_view(self, node):
        queue = [node]
        res = []
        while queue:
            current_val = []
            next_level = []
            for n in queue:
                current_val.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            res.append(current_val)
            queue = next_level
        right_view = ''
        for node in res:
            right_view += str(node[-1]) + ' '
        return right_view

    def left_and_right_view_recusion(self, node, view):
        temp_dict = {}
        if view == "left":
            self.left_view(node, temp_dict, 1)
        else:
            self.right_view(node, temp_dict, 1)
        for k, v in temp_dict.items():
            print(v, end=" ")

    def left_view(self, root, temp_dict, level):
        if not root:
            return
        if level not in temp_dict:
            temp_dict[level] = root.val
        self.left_view(root.left, temp_dict, level + 1)
        self.left_view(root.right, temp_dict, level + 1)

    def right_view(self, root, temp_dict, level):
        if not root:
            return
        if level not in temp_dict:
            temp_dict[level] = root.val
        self.right_view(root.right, temp_dict, level + 1)
        self.right_view(root.left, temp_dict, level + 1)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
tree.left.left.left = Node(8)
tree.left.left.left.left = Node(9)
binary_tree = BT()
# print(binary_tree.get_left_view(tree))
print(binary_tree.get_right_view(tree))
print(binary_tree.left_and_right_view_recusion(tree, "right"))