class Solution:
    def preorderTraversal(self, root):
        traversal = []
        stack = [root]
        if not root: return traversal
        
        while stack:
            node = stack.pop()
            if node.right: 
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
            traversal.append(node.val)
        return traversal