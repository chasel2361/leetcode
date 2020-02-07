class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.isSym(root.left, root.right)
        
    def isSym(self, l, r):
        if not l and not r: return True
        if (not l and r) or (not r and l): return False        
        return l.val == r.val and self.isSym(l.left, r.right) and self.isSym(l.right, r.left)