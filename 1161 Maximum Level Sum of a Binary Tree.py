# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        answer = (-math.inf, 0)
        queue = [root]
        depth = -1

        while queue:
            answer = max(answer, (sum(node.val for node in queue), depth))
            queue = [child for node in queue for child in (node.left, node.right) if child]
            depth -= 1

        return -answer[1]
