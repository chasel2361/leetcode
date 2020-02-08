class Solution:
        def isSameTree(self, p, q):
            if not p and not q: return True # [1]
            if (p and not q) or (q and not p): return False # [2]
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # [3]