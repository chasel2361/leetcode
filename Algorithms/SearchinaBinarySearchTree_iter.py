class Solution:
    def searchBST(self, root, val):
        if not root or val == root.val: return root

        while root.val != val:
            node = root.val
            if node > val:
                root = root.left
            else:
                root = root.right
                
            if not root: return None
        return root