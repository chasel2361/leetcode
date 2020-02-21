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
        self.get_path(root, "", res)
        return res
    
    def get_path(self, root: TreeNode, path: str, res: list):
        """
        Paramaters:
            root: The TreeNode which need to get path.
            path: A temporary arg records the path to root.
            res: Result list obj which record all the path in this tree.
        """
        if not root.left and not root.right:
            res.append(path + str(root.val))            
        tmp = path + str(root.val) + "->" 
        if root.left:
            self.get_path(root.left, tmp, res)
        if root.right:
            self.get_path(root.right, tmp, res)