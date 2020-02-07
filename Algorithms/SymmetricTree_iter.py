from collections import deque
class Solution:
    def isSymmetric(self, root):
        if not root: return True  # [1]
        quene = deque([(root.left, root.right)])  # [2]
        while quene:
            l, r = quene.popleft()
            if not l and not r: continue  # [3]
            if l and r and l.val == r.val:  # [4]
                quene.append((l.left, r.right))
                quene.append((l.right, r.left))
            else:
                return False
        return True