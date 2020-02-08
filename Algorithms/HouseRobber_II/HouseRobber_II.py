class Solution:
    def rob(self, nums):
        l = len(nums)
        if l == 0: return 0
        if l <= 3: return max(nums)
        
        pre_1, now_1 = 0, nums[0]
        pre_2, now_2 = 0, nums[1]
        
        for i in range(1, l-1):
            pre_1, now_1  = now_1, max(pre_1 + nums[i], now_1)
            pre_2 ,now_2 = now_2, max(pre_2 + nums[i+1], now_2)
            
        return max(now_1, now_2)