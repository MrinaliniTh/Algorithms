class Solution:
    def maxLevelSum(self, root) -> int:
        queue = [root]
        max_sum = root.val
        level_count = 1
        max_level = 1     
        while queue:
            level_sum = 0
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                level_sum += node.val
            queue = new_queue
            if level_sum > max_sum:
                max_level = level_count
                max_sum = level_sum
            level_count += 1
        return max_level