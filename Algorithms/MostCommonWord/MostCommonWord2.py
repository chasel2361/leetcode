from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        words = Counter([word for word in words if word not in banned])
        return words.most_common(1)[0][0]