class Solution:
    def inorderTraversal(self, root):
        if not root: return []
        traversal = []
        stack = []        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            traversal.append(root.val)
            root = root.right
        return traversal