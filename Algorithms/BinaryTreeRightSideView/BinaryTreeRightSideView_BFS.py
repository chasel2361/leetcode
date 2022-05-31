from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque([root,])
        while q:
            cnt = len(q)
            for _ in range(cnt):
                ptr = q.popleft()
                if ptr.left:
                    q.append(ptr.left)
                if ptr.right:
                    q.append(ptr.right)
            res.append(ptr.val)
        return res