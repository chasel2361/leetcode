# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        if not root:
            return []        
        res = []
        path = []
        self.get_path(root, path, res)
        return res
    
    def get_path(self, root: TreeNode, path: list, res: list):
        """
        Parameters:
            root: The TreeNode which need to get path.
            path: A temporary arg records the path to root which will be delete when 
                the root turns out to be leaf.
            res: Result list obj which record all the path in this tree.
        """
        path.append(str(root.val))
        if root.left:
            self.get_path(root.left, path, res)
        if root.right:
            self.get_path(root.right, path, res)
        if not root.left and not root.right:
            res.append("->".join(path))
        path.pop()