class Solution:
    def reverseBetween(self, head, m, n):
        if m == n: return head  # [1]
        
        stack = []
        left, node = None, head
        
        if m != 1:
            for _ in range(1, m - 1):
                node = node.next
            left = node
            node = node.next
        
        for _ in range(m, n + 1):
            stack.append(node)  # [2]
            node = node.next
        
        l1, l2 = stack.pop(), None
        if m == 1:
            head = l1  # [3]
        else:
            left.next = l1  # [4]
        
        while stack:
            l2 = stack.pop()
            l1.next = l2
            l1 = l2
        l1.next = node  # [5]
        return head