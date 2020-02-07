class Solution:
    def searchBST(self, root, val):
        if not root or val == root.val: return root
        
        if root.val < val: 
            return self.searchBST(root.right, val)
        else: 
            return self.searchBST(root.left, val)