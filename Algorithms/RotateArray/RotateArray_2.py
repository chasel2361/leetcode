class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        l = [None] * n
        for i in range(n):
            l[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = l[i]