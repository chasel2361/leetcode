class Solution:
    def rotate(self, nums, k):
        def reverse(start, end):
            while start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1
        if k:
            k = k % len(nums)
            reverse(0, len(nums) - 1)
            reverse(0, k - 1)
            reverse(k, len(nums) - 1)