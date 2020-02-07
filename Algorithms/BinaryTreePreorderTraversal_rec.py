class Solution:
    def __init__(self):
        self.traversal = []
    def preorderTraversal(self, root):
        if not root: return []
        
        self.traversal.append(root.val)        
        self.preorderTraversal(root.left)            
        self.preorderTraversal(root.right)
        
        return self.traversal