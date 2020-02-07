class Solution:
    def __init__(self):
        self.res = 0
        
    def maxPathSum(self, root):
        if not root: return 0
        self.res = root.val
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        l = self.dfs(node.left) if node.left else 0
        r = self.dfs(node.right) if node.right else 0
        m = max(node.val, node.val + l, node.val + r)  #[1]
        self.res = max(self.res, m, l + r + node.val)  # [2]
        return m  # [3]