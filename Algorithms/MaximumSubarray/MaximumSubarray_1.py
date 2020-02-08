class Solution:
    def maxSubArray(self, nums):
        l = len(nums)
        if l == 0: return 0
        res = cur = nums[0]
        for i in range(1, l):
            if cur > 0:
                cur += nums[i]  # [1]
            else:
                cur = nums[i]  # [2]
        
            if cur > res:
                res = cur
        return res