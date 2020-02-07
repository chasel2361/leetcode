class Solution:
    def sortArrayByParity(self, A):
        B, C = [], []
        for num in A:
            if num % 2 == 0:
                B.append(num)
            else:
                C.append(num)
        return B + C