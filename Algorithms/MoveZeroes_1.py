class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):  # [1]
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1