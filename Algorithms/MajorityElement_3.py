class Solution:
    def majorityElement(self, nums):
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == res:
                count += 1
            elif count > 0:
                count -= 1
            else:
                res = nums[i]
                count += 1
        return res