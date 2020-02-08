from TreeNode import TreeNode

class Solution:
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        len_n = len(nums)
        if len_n == 0: return None
        root = self.getNode(0, len_n - 1, nums)
        return root
    
    def getNode(self, l, r, nums):
        if l > r: return None
        m = (r + l) // 2
        root = TreeNode(nums[m])
        root.left = self.getNode(l, m - 1, nums)
        root.right = self.getNode(m + 1, r, nums)
        return root