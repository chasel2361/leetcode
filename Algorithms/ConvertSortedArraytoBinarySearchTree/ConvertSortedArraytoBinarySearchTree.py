from TreeNode import TreeNode

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums or len(nums) == 0: return None
        return self.getNode(0, len(nums) - 1, nums)
        
    def getNode(self, l, r, nums):
        if l > r: return None  # [4]
        m = (l + r) // 2  # [1]
        root = TreeNode(nums[m])
        root.left = self.getNode(l, m - 1, nums)  # [2]
        root.right = self.getNode(m + 1, r, nums)  # [3]
        return root