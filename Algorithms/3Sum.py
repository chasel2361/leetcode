class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)        
        for i in range(n-2): # [1]
            if nums[i] > 0: break # [2]
            if i > 0 and nums[i] == nums[i-1]: continue # [3]
            
            left = i + 1
            right = n - 1 # [4]
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1 # [5]
                elif total < 0:
                    left += 1 # [6]
                else:
                    res.append([nums[i], nums[left], nums[right]]) # [7]
                    
                    while left < right and nums[left+1] == nums[left]: # [8]
                        left += 1
                    while left < right and nums[right-1] == nums[right]: # [8]
                        right -= 1                    
                    left += 1
                    right -= 1
        return res