class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None
        if left and right:
            return root
        if left and not right:
            return left
        return right