from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word.lower() for word in re.split(r'[!?\',;. ]', paragraph)]
        words = Counter(words)
        banned.append('')
        for bword in banned:
            if bword in words:
                words.pop(bword)
        return words.most_common(1)[0][0]