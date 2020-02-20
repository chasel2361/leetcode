from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        for key, value in t.items():
            if key not in s.keys() or value != s.pop(key):
                return False
        if len(s.keys()) > 0:
            return False
        return True