from collections import Counter
class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        return max(count, key = count.get)