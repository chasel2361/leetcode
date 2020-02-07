class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:  
            n = (l + r)//2
            if target < nums[n]:
                r = n - 1  # [1]
            elif target > nums[n]:
                l = n + 1  # [1]
            else:
                return n  # [2]
        return l  # [3]