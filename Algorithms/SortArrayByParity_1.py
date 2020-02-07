class Solution:
    def sortArrayByParity(self, A):
        if not A: return []
        i, j = 0, len(A) - 1
        while i < j:
            while A[i] % 2 == 0 and i < j:
                i += 1
            while A[j] %2 == 1 and i < j:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        return A