class Solution:
    def productExceptSelf(self, nums: list) -> list:
        """
        Example:
            nums    1        2        3        4
            res     2*3*4    1*3*4    1*2*4    1*2*3
            left             1        1*2      1*2*3
            right   2*3*4      3*4        4
        
        Args:
            n: number of nums
            sol: left -> res
            tmp: right
        """        
        n = len(nums)
        sol = [1] * n
        for i in range(1, n):
            sol[i] = sol[i-1] * nums[i-1]
        tmp = 1
        for i in range(n-1, -1, -1):
            sol[i] *= tmp
            tmp *= nums[i]        
        return sol