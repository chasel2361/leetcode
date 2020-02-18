from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        def check(word):
            dic_check = Counter(word)
            for key, value in dic_check.items():
                if key not in dic.keys() or value > dic[key]:
                    return 0
            return len(word)
        
        dic = Counter(chars)
        n = 0
        for word in words:
            n += check(word)
        return n