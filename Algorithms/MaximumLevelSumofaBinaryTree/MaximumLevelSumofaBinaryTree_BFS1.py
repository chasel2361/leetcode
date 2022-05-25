from collections import deque
class Solution:
    def maxLevelSum(self, root):
        """
        Arg:
            maxsum(int): maximum summation of level for now
            res(int): the level of maximum summation
            level(int): processing level
            q(quene): quene record a level of nodes
            total(int): summation of level
            cnt(int): count of nodes of level
        """
        maxsum = 0
        res = 0
        level = 1
        
        q = deque()
        q.append(root)
        
        while q:
            cnt = len(q)
            total = 0
            
            # 處理每層節點
            while cnt > 0:
                node = q.popleft()
                total += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cnt -= 1
            
            if total > maxsum:
                maxsum = total
                res = level
                
            level += 1
        return res