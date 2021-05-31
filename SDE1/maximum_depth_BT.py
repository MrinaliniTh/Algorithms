class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)