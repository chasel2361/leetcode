import math

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = (-math.inf, 0)
        q = [root]
        depth = -1
        
        while q:
            ans = max(ans, (sum(node.val for node in q), depth))
            q = [n for node in q for n in [node.left, node.right] if n]
            depth -= 1
        return -ans[1]