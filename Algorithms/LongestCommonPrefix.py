class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = max(strs)
        s2 = min(strs)        
        for i, c in enumerate(s2):
            if c != s1[i]:
                return s2[:i]
        return s2