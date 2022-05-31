class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            level = [root]
            while level:
                res += [level[-1].val]
                level = [kid for node in level for kid in [node.left, node.right] if kid]
        return res