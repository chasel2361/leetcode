class Solution:
    def sortedSquares(self, A):
        len_A = len(A)
        i = len_A - 1
        r, l = i, 0
        res = [0] * len_A
        
        for i in range(len_A):
            A[i] = abs(A[i])
        
        while i >= 0:  # [1]
            Al, Ar = A[l], A[r]
            if Al > Ar:
                res[i] = Al ** 2
                l += 1
            else:
                res[i] = Ar ** 2
                r -= 1
            i -= 1
        return res