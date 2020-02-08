class Solution:
    def twoSum(self, nums, target):
        numMap = {} # [1]
        for i, num in enumerate(nums):
            if (target - num) not in numMap:
                numMap[num] = i # [2]
            else:
                return [numMap[target - num], i]