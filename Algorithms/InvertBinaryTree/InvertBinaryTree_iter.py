# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        q = deque([root])
        while q:
            ptr = q.pop()
            ptr.left, ptr.right = ptr.right, ptr.left
            if ptr.left: q.appendleft(ptr.left)
            if ptr.right: q.appendleft(ptr.right)
        return root