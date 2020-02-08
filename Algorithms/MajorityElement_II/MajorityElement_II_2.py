from collections import Counter
class Solution:
    def majorityElement(self, nums):
        numMap = Counter(nums)
        res = []
        for k, v in numMap.items():
            if v > len(nums) // 3:
                res.append(k)
        return res