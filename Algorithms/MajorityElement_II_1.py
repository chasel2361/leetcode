class Solution:
    def majorityElement(self, nums):
        if not nums: return []
        n1 = nums[0]
        n2 = None
        cnt_1 = 1
        cnt_2 = 0
        
        for i in range(1, len(nums)):
            if nums[i] == n1:
                cnt_1 += 1
            elif n2 == None:
                n2 = nums[i]
                cnt_2 = 1
            elif nums[i] == n2:
                cnt_2 += 1
            elif cnt_1 == 0:
                n1 = nums[i]
                cnt_1 = 1
            elif cnt_2 == 0:
                n2 = nums[i]
                cnt_2 = 1
            else:
                cnt_1 -= 1
                cnt_2 -= 1
        
        cnt_1, cnt_2 = 0, 0
        for n in nums:
            if n == n1:
                cnt_1 += 1
            if n == n2:
                cnt_2 += 1
        
        res = []
        if cnt_1 > len(nums) // 3:
            res.append(n1)
        if cnt_2 > len(nums) // 3:
            res.append(n2)