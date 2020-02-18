from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        dic = Counter(chars)
        n = 0
        for word in words:
            good = True
            dic_c = Counter(word)
            for key, value  in dic_c.items():
                if key not in dic.keys() or value > dic[key]:
                    good = False
                    break
            if good == True:
                n += len(word)
        return n