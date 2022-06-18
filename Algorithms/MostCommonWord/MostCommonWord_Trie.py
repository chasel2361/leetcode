from collections import Counter
import re

class Solution:
    def __init__(self):
        self.res = ''
        self.maxcnt = 0
    
    class TrieNode():
        def __init__(self):
            self.word = ''
            self.cnt = 0
            self.links = [None] * 26
        
    def insert(self, r: TrieNode, s: str):
        ptr = r
        for i in s:
            index = ord(i) - ord('a')
            if not ptr.links[index]:
                node = self.TrieNode()
                node.word = ptr.word + i
                ptr.links[index] = node
            ptr = ptr.links[index]
        ptr.cnt += 1

    def ban(self, r: TrieNode, s: str):
        ptr = r
        for i in s:
            index = ord(i) - ord('a')
            if not ptr.links[index]: return
            ptr = ptr.links[index]
        ptr.cnt = 0

    def findMax(self, ptr: TrieNode):
        if not ptr: return
        if ptr.cnt > self.maxcnt:
            self.res = ptr.word
            self.maxcnt = ptr.cnt
        for i in range(len(ptr.links)):
            self.findMax(ptr.links[i])
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        root = self.TrieNode()
        words = re.findall(r'\w+', paragraph.lower())
        for word in words:
            self.insert(root, word)
        for s in set(banned):
            self.ban(root, s)
        self.findMax(root)
        return self.res