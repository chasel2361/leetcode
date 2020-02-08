class Solution:
    def postorderTraversal(self, root):
        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            
        return traversal[::-1]