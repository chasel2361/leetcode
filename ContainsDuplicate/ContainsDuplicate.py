from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        if cnt.most_common(1)[0][1] > 1:
            return True
        return False