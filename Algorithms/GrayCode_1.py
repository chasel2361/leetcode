class Solution:
    def grayCode(self, n):
        res = [0]  # [1]
        add = 1  # [2]
        for _ in range(n):
            for i in range(add):
                res.append(res[add - 1 - i] | add)  # [3]
            add <<= 1  # [4]
        return res