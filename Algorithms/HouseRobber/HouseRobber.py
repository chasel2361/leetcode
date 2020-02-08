class Solution:
    def rob(self, nums):
        l = len(nums)
        if l == 0: return 0
        if l <= 2: return max(nums)
        house = 0
        previous = max(nums[1], nums[0])
        m_previous = nums[0]
        for i in range(2, l):
            house = max(previous, m_previous + nums[i])
            m_previous = previous
            previous = house
        return house