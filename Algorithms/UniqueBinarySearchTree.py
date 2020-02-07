class Solution:
    def numTrees(self, n):
        res = [0] * (n + 1)
        res[0] = 1

        for i in range(1, n + 1):  # [2]
            for j in range(i):  # [1]
                res[i] += res[j] * res[i - j - 1]
        return res[n]