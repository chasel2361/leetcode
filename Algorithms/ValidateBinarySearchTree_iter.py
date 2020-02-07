class Solution:
    def isValidBST(self, root):
        last = float('-inf')  # [1]
        stack = []
        while stack or root:  # [2]
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()  # [3]
            
            if root.val <= last:
                return False
            last = root.val
            root = root.right  # [4]
            
        return True