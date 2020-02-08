from ListNode import ListNode

class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next        
        pre.next = None  #[1]
        n1 = self.sortList(head)  #[2]
        n2 = self.sortList(slow)  #[2]
        return self.merge(n1, n2)   
        
    def merge(self, n1, n2):
        n = ListNode(0)
        itr = n
        while n1 and n2:
            if n1.val < n2.val:
                itr.next = n1
                n1 = n1.next
            else:
                itr.next = n2
                n2 = n2.next
            itr = itr.next
        if n1: itr.next = n1
        if n2: itr.next = n2        
        return n.next