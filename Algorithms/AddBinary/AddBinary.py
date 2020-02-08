class Solution:
    def addBinary(self, a, b):
        c = bin(int(a, 2) + int(b, 2))  # [1]
        return c[2:]  # [2]