class Solution:
    def __init__(self):
        self.last = None
    def isValidBST(self, root) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False  # [1], [3]
        if self.last and root.val <= self.last.val: return False  # [2]
        self.last = root  # [4]
        return self.isValidBST(root.right)  # [5]