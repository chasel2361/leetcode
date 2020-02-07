class Solution:
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a
        
        if a[-1] == '0' and b[-1] == '0':  # [1]
            return self.addBinary(a[:-1], b[:-1]) + '0'  # [2]
        elif a[-1] == '1' and b[-1] == '1':  # [1]
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'  # [3]
        else:  # [1]
            return self.addBinary(a[:-1], b[:-1]) + '1'  # [4]