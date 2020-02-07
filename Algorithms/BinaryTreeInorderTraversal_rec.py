class Solution:
    def __init__(self):
        self.traversal = []
    def inorderTraversal(self, root):
        if not root: return []
        if root.left:
            self.inorderTraversal(root.left)
        self.traversal.append(root.val)
        self.inorderTraversal(root.right)
        return self.traversal