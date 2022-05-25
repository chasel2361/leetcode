from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level, res = 1, 1
        maxsum = root.val
        
        while q:
            total = 0
            cnt = len(q)
            while cnt > 0:
                ptr = q.popleft()
                total += ptr.val
                if ptr.left: q.append(ptr.left)
                if ptr.right: q.append(ptr.right)
                cnt -= 1
            
            if total > maxsum:
                maxsum, res = total, level
            level += 1
        return res