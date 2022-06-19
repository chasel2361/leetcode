# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cond1 = root.val == p.val or root.val == q.val
        cond2 = p.val < root.val and root.val < q.val
        cond3 = p.val > root.val and root.val > q.val
        
        if cond1 or cond2 or cond3:
            return root
        if root.val > p.val and root.val > q.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
        