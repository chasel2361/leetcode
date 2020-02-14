class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        N1, N2 = m-1, n-1
        K = m+n-1
        
        while N2 >= 0:
            if N1 < 0 or nums1[N1] < nums2[N2]:
                nums1[K] = nums2[N2]
                N2 -= 1
                K -= 1
            else:
                nums1[K] = nums1[N1]
                N1 -= 1
                K -= 1